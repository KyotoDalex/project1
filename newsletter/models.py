from django.db import models

class SubscribedUsers(models.Model):
    email = models.CharField(unique=True, max_length=50, null=True,blank=True)
    def __str__(self):
        return self.email
