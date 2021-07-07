from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post, User
from .forms import CommentForm, NewUserForm
from django.views import View 
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

class StartingPageView(ListView):
    template_name = 'blog/index.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

class AllPostsView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'

class SinglePostView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        fav = bool
        if post.favorites.filter(id=request.user.id).exists():
            fav = True
            
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "fav": fav
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        
        request.user.profile.posts.add(post)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id")
        }
        return render(request, "blog/post-detail.html", context)

# User Views

def signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully')
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = NewUserForm()
        return render(request, 'blog/signup.html', {'form': form})
    
# if post, then authenticate (user submitted username and password)
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print('The account has been disabled.')
                    return HttpResponseRedirect('/login')
        else:
            print('The username and/or password is incorrect.')
            return HttpResponseRedirect('/login')
    else: # it was a get request so send the emtpy login form
        form = AuthenticationForm()
        return render(request, 'blog/login.html', {'form': form})
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def favorite_add(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.favorites.filter(id=request.user.id).exists():
        post.favorites.remove(request.user)
    else:
        post.favorites.add(request.user)
    return HttpResponseRedirect(reverse("detail-page", args=[slug]))

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    favorites = Post.objects.filter(favorites=user.id)
    return render(request, 'blog/profile.html', {'username': username, 'favorites': favorites})

