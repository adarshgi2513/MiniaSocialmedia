from django.contrib import admin
from django.urls import path
from socialmedia import settings
from socialapp import views
from django.conf.urls.static import static



urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('loginn/',views.loginn,name='loginn'),
    path('logoutt/',views.logoutt,name='logout'),
    path('upload/',views.upload,name='upload'),
    path('like-post/<str:id>',views.likes,name='like-post'),
    path('explore/',views.explore,name='explore'),
    path('profile/<str:id_user>',views.profile,name='profile'),
    path('delete/<uuid:id>/', views.delete, name='delete-post'),
    path('search-results/', views.search_results, name='search_results'),
    path('save_comment/', views.save_comment, name='comment_save'),
   
 
 


]