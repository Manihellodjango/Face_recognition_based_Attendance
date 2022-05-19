from django.db import models
types = [('Faculty','Faculty'),('Student','Student')]
class Profile(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    date = models.DateField()
    phone = models.BigIntegerField()
    email = models.EmailField()
    Year = models.IntegerField()
    Roll_Number = models.IntegerField(null=True)
    Branch = models.CharField(max_length=200)
    Section = models.CharField(max_length=200,null=True)
    status = models.CharField(choices=types,max_length=20,null=True,blank=False,default='Faculty')
    present = models.BooleanField(default=False)
    image = models.ImageField()
    updated = models.DateTimeField(auto_now=True)
    shift = models.TimeField()
    def __str__(self):
        return self.first_name +' '+self.last_name


class LastFace(models.Model):
    last_face = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.last_face

