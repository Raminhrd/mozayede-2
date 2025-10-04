from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    is_ban = models.BooleanField(default=False)
    ban_until = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        if self.user.first_name:
            return self.user.first_name
        else:
            return self.user.username