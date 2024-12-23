from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class Website(models.Model):
    name = models.CharField(max_length=100)
    data_added = models.DateTimeField(auto_now=True)
    owners = models.ManyToManyField('users.UserModel')
    url = models.URLField()
    status = models.BooleanField(default=True)
    needs_password = models.BooleanField(default=False)
    username = models.CharField(max_length=300, blank=True, null=True)
    hashed_password = models.CharField(blank=True, null=True, max_length=500)

    def set_password(self, password):
        self.hashed_password = make_password(password)
    
    def check_password(self, password):
        return check_password(password, self.hashed_password)
    

class Rotas(models.Model):
    site = models.ForeignKey('website', on_delete=models.CASCADE)
    rota = models.CharField(max_length=100)
    is_login = models.BooleanField(default=False)
