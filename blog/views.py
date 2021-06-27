from datetime import date
from django.shortcuts import render

# dummy data until I build the db
all_posts = [
    {
        "slug": "new-river-gorge",
        "image": "bridge_burst.jpeg",
        "author": "Amanda",
        "date": date(2021, 6, 27),
        "title": "New River Gorge",
        "excerpt": "As of publication, New River Gorge is the newest National Park on the list. And one day a year, people line up to jump 800+ feet to the ground below the bridge.",
        "content": """
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Cumque culpa praesentium earum fugiat repudiandae laboriosam voluptates optio officiis, nobis, maiores tempore esse harum facere. Dolor provident quasi beatae voluptatibus impedit! 
        
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Cumque culpa praesentium earum fugiat repudiandae laboriosam voluptates optio officiis, nobis, maiores tempore esse harum facere. Dolor provident quasi beatae voluptatibus impedit! 
        
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Cumque culpa praesentium earum fugiat repudiandae laboriosam voluptates optio officiis, nobis, maiores tempore esse harum facere. Dolor provident quasi beatae voluptatibus impedit!
        """
    },
    {
        "slug": "fairy-trail",
        "image": "fairy_trail.jpeg",
        "author": "Amanda",
        "date": date(2021, 5, 1),
        "title": "Mason Dixon Park",
        "excerpt": "Tucked within Mason Dixon Historical Park, you'll find an enchanted trail that's home to all sorts of fae folk.",
        "content": """
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Cumque culpa praesentium earum fugiat repudiandae laboriosam voluptates optio officiis, nobis, maiores tempore esse harum facere. Dolor provident quasi beatae voluptatibus impedit! 
        
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Cumque culpa praesentium earum fugiat repudiandae laboriosam voluptates optio officiis, nobis, maiores tempore esse harum facere. Dolor provident quasi beatae voluptatibus impedit! 
        
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Cumque culpa praesentium earum fugiat repudiandae laboriosam voluptates optio officiis, nobis, maiores tempore esse harum facere. Dolor provident quasi beatae voluptatibus impedit!
        """
    },
    {
        "slug": "holly-river",
        "image": "holly-river.jpeg",
        "author": "Amanda",
        "date": date(2021, 6, 1),
        "title": "Holly River State Park",
        "excerpt": "Nestled in a narrow valley, you're sure to find contentment somewhere on the 8,000+ acres that make up Holly River State Park.",
        "content": """
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Cumque culpa praesentium earum fugiat repudiandae laboriosam voluptates optio officiis, nobis, maiores tempore esse harum facere. Dolor provident quasi beatae voluptatibus impedit! 
        
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Cumque culpa praesentium earum fugiat repudiandae laboriosam voluptates optio officiis, nobis, maiores tempore esse harum facere. Dolor provident quasi beatae voluptatibus impedit! 
        
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Cumque culpa praesentium earum fugiat repudiandae laboriosam voluptates optio officiis, nobis, maiores tempore esse harum facere. Dolor provident quasi beatae voluptatibus impedit!
        """
    }
]

# Create a quick way to kind of grab the dates from all the posts.
def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date) # Sort them by date
    latest_posts = sorted_posts[-3:] # Grab the 3 most recent (from the end, go 3 posts back, and get everything from there to the end)
    return render(request, 'blog/index.html', {'posts': latest_posts}) # send that data to the index page for render

def posts(request):
    return render(request, 'blog/all-posts.html', {'posts': all_posts})

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
      "post": identified_post
    })
