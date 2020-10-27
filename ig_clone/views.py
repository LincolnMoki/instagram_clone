from django.shortcuts import render,redirect
from . forms import ImageUploadForm,ImageProfileForm,CommentForm
from .models import *
from django.contrib.auth.decorators import login_required
from vote.managers import  VotableManager

votes = VotableManager()

@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.all()
    
    
   
    
    return render(request, 'instagram/index.html',{"images":images})

def image_upload(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageUploadForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('home')

    else:
        form = ImageUploadForm()
        return render(request,'instagram/upload.html', {"form":form})

def profile_info(request):
    
    current_user=request.user
    profile_info = Profile.objects.filter(user=current_user).first()
    posts =  request.user.image_set.all()
    
    
    return render(request,'instagram/profile.html',{"images":posts,"profile":profile_info,"current_user":current_user})

def profile_edit(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageProfileForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('profile')

    else:
        form = ImageProfileForm()
        return render(request,'instagram/edit.html',{"form":form})
def add_comment(request,id):

    current_user = request.user
    image = Image.get_single_photo(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        print(form)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.image_id = id
            comment.save()
        return redirect('home')

    else:
        form = CommentForm()
        return render(request,'instagram/new_comment.html',{"form":form,"image":image})   

def comments(request,id):
    comments = Comments.get_comments(id)
    number = len(comments   )
    
    return render(request,'instagram/comments.html',{"comments":comments,"number":number}