from django.db import models

class Blog(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.username
