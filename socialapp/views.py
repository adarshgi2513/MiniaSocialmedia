from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . models import  Profile
from.models import Post,likepost
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from.forms import CommentForm
from django.http import JsonResponse
from.models import Commenttt


# Create your views here.




def signup(request):
 try:
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        emailid=request.POST.get('emailid')
        pwd=request.POST.get('pwd')
        print(fnm,emailid,pwd)
        my_user=User.objects.create_user(fnm,emailid,pwd)
        my_user.save()
        user_model = User.objects.get(username=fnm)
        new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
        new_profile.save()
        if my_user is not None:
            login(request,my_user)
            return redirect('/')
        return redirect('/loginn')
    
        
 except:
        invalid="User already exists"
        return render(request, 'signup.html',{'invalid':invalid})
  
    
 return render(request, 'signup.html')
        
         
def loginn(request):
 
  if request.method == 'POST':
        fnm=request.POST.get('fnm')
        pwd=request.POST.get('pwd')
        print(fnm,pwd)
        userr=authenticate(request,username=fnm,password=pwd)
        if userr is not None:
            login(request,userr)
            return redirect('/')
        
 
        invalid="Invalid Credentials"
        return render(request, 'loginn.html',{'invalid':invalid})
               
  return render(request, 'loginn.html')




@login_required(login_url='/loginn')
def logoutt(request):
    logout(request)
    return redirect('/loginn')

@login_required(login_url='/loginn')     
def upload(request):
    if request.method == 'POST':
        User=request.user.username
        image=request.FILES.get('image_upload')
        caption=request.POST['caption']
        new_post=Post.objects.create(user=User,image=image,caption=caption)
        new_post.save()
        return redirect('/')
    else:
        return redirect('/')

@login_required(login_url='/loginn')
def home(request):
    post = Post.objects.all().order_by('created_at')
    profile= Profile.objects.get(user=request.user)
    com_form = CommentForm()

    comments = Commenttt.objects.filter(post__in=post)
    context={
        'post':post,
        'profile':profile,
        'comments': comments,
        'com_form': com_form
    }

    return render(request,'main.html',context)


    

@login_required(login_url='/loginn')
def likes(request, id):
    if request.method == 'GET':
        username = request.user.username
        post = get_object_or_404(Post, id=id)

        like_filter = likepost.objects.filter(post_id=id, username=username).first()

        if like_filter is None:
            new_like = likepost.objects.create(post_id=id, username=username)
            post.no_of_likes = post.no_of_likes + 1
        else:
            like_filter.delete()
            post.no_of_likes = post.no_of_likes - 1

        post.save()

        # Generate the URL for the current post's detail page
        print(post.id)

        # Redirect back to the post's detail page
        return redirect('/#'+id)
 
def explore(request):
    post=Post.objects.all().order_by('-created_at')
    profile =  Profile.objects.get(user=request.user)
    
    context={
        'post':post,
        'profile':profile

    }
    return render(request,'explore.html',context)

@login_required(login_url='/loginn')
def profile(request,id_user):
    user_object=User.objects.get(username=id_user)
    profile=Profile.objects.get(user=request.user)
    user_profile=Profile.objects.get(user=user_object)
    user_post=Post.objects.filter(user=id_user).order_by('-created_at')
    user_post_length=len(user_post)
    context={
        'user_object':user_object,
        'user_profile':user_profile,
        "user_post":user_post,
        'user_post_length':user_post_length,
        'profile':profile
    }
    if request.user.username ==id_user:
        if request.method=='POST':
            if request.FILES.get('image')==None:
                image=user_profile.profileimg
                bio=request.POST['bio']
                loacation=request.POST['location']

                user_profile.profileimg=image
                user_profile.bio=bio
                user_profile.location=loacation
                user_profile.save()
            if request.FILES.get('image')!=None:
                image=request.FILES.get('image')
                bio=request.POST['bio']
                loacation=request.POST['location']

                user_profile.profileimg=image
                user_profile.bio=bio
                user_profile.location=loacation
                user_profile.save()
                return redirect('/profile/'+id_user)
            else:
                return render(request,'profile.html',context)
            
    return render(request,'profile.html',context)
@login_required(login_url='/loginn')
def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()

    return redirect('/profile/'+ request.user.username)


@login_required(login_url='/loginn')
def search_results(request):
    query = request.GET.get('q')

    users = Profile.objects.filter(user__username__icontains=query)
    posts = Post.objects.filter(caption__icontains=query)

    context = {
        'query': query,
        'users': users,
        'posts': posts,
    }
    return render(request, 'search_user.html', context)


def save_comment(request):
    if request.method == 'POST':
        post_id = request.POST.get('postid')
        post = Post.objects.get(id=post_id)
        com_form = CommentForm(request.POST)

        if com_form.is_valid():
            new_comment = com_form.save(commit=False)
            new_comment.post = post
            new_comment.username = request.user.username 
            new_comment.save()
            return redirect('/#'+post_id)
        else:
            return redirect('/#'+post_id)

    return redirect('/#'+post_id)
