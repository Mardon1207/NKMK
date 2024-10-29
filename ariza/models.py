from django.db import models
from ckeditor.fields import RichTextField

class Application(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    Ismi = models.CharField(max_length=100,)
    email = models.EmailField( blank=True, null=True)
    telfon_raqami = models.CharField(max_length=15)
    lavozimi = models.CharField(max_length=100,blank=True, null=True)
    body = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.Ismi}"


class Qabul(models.Model):
    STATUS_CHOICES = [
        ('kutish', 'Kutish'),
        ('tasdiqlandi', 'Tasdiqlandi'),
        ('rad etildi', 'Rad etildi'),
    ]
    PK = models.ForeignKey(Application, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now_add=True)
    javob=models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='kutish', blank=True, null=True)

    def __str__(self):
        return f"{self.PK} - {self.status}"
