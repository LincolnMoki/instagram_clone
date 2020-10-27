from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from vote.models import VoteModel


class Image(VoteModel,models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=50)
    image_caption = models.CharField(max_length=50)
    likes = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    @classmethod    
    def update_caption(cls,id,new_caption):
        cls.objects.filter(pk = id ).update(image_caption = new_caption)
        new_caption_object = cls.objects.get(image_caption=new_caption)
        new_caption = new_caption_object.image_caption
        return new_caption
    
    @classmethod
    def get_single_photo(cls,id):
        image = cls.objects.get(pk=id)
        return image
    
    def __str__(self):
        
        return self.image_name