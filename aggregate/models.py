from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class aggregateList(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, blank=True)
    jamb = models.PositiveIntegerField()
    post_utme = models.PositiveIntegerField()
    aggregate = models.CharField(max_length=50)
    created = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.username.username
    class Meta:
        verbose_name_plural = 'Aggregate Table'
    

