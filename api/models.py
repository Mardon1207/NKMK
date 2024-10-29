from django.db import models
from django.utils import timezone


class Branch(models.Model):
    id=models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
class Department(models.Model):
    id=models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
class Positions(models.Model):
    id=models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=700)

    def __str__(self):
        return self.name

class Spravochniks(models.Model):
    id=models.BigAutoField(primary_key=True)
    FullName=models.CharField(max_length=200, verbose_name="F.I.SH", help_text="F.I.SHni kiriting")
    Branch=models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Tashkilot", help_text="Tashkilotni tanlang")
    Department=models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    Positions=models.ForeignKey(Positions, on_delete=models.SET_NULL, null=True, blank=True)
    Stationary=models.CharField(max_length=250, verbose_name="F.I.SH", help_text="F.I.SHni kiriting")
    Mobile=models.CharField(max_length=250)
    creator=models.CharField(max_length=250)
    changer=models.CharField(max_length=250)
    created = models.DateTimeField(default=timezone.now)
    changed = models.DateTimeField(default=timezone.now)
    def __str__(self) -> str:
        return f"{self.FullName}"
    
    class Meta:
        verbose_name = "Spravochnik"
        verbose_name_plural = "Spravochniklar"
        ordering = ["FullName"]
