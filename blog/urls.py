from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.StartingPageView.as_view(), name='starting-page'),
    path('posts', views.AllPostsView.as_view(), name='posts-page'),
    path('posts/<slug:slug>', views.SinglePostView.as_view(), name='detail-page'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup, name='signup'),
    path('user/<username>/', views.profile, name='profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
