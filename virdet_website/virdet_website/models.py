from django.db import models
from django.contrib import admin

class Token(models.Model):
    code = models.CharField(max_length=20)
    used = models.BooleanField(default=False)

admin.site.register(Token)