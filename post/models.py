from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255, blank=True)
    body = RichTextField()
    photo = models.ImageField(upload_to='images', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])