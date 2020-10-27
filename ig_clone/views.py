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
