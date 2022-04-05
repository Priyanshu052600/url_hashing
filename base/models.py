from django.db import models
from hashlib import md5

# Create your models here.

class Url(models.Model):
    full_url= models.CharField(unique=True,max_length=10000000000000)
    short_url=models.CharField(unique=True, max_length=20)

    def __str__(self):
        return self.full_url
    
    @classmethod
    def create(self,full_url,code):
        if Url.objects.filter(short_url=code).exists():
            temp_url=md5(full_url.encode()).hexdigest()[:5]
        else:
            temp_url=code

        try:
            obj=self.objects.create(full_url=full_url, short_url=temp_url)
        except:
            obj=self.objects.get(full_url=full_url)
        return obj




