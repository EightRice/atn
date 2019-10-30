from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=200)
    content=models.TextField()
    email=models.EmailField(null=True,blank=True)
    phone=models.CharField(blank=True,null=True,max_length=120)
    class Meta:
        verbose_name='Contact Message'
        verbose_name_plural='Contact Messages'
