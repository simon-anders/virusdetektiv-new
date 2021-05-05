from django.db import models
from django.contrib import admin

class TokenList(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=300)

class Token(models.Model):
    code = models.CharField(max_length=20)
    used = models.BooleanField(default=False)

class Order(models.Model):
    token = models.ForeignKey(Token,on_delete=models.SET_NULL,null=True)
    nKits = models.IntegerField()
    encrypted_data = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

admin.site.register(TokenList)
admin.site.register(Token)
admin.site.register(Order)