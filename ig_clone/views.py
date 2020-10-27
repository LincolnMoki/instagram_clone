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
        return render(request,'socioapp/upload.html', {"form":form})