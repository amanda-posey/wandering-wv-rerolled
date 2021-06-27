from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField() # Inbuilt field that validates email addresses


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=250)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True) #Updates date on every update of the post
    slug = models.SlugField(unique=True, db_index=True) # Forces unique slug, and allows us to query by slug easier
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='posts')
    tags = models.ManyToManyField(Tag)