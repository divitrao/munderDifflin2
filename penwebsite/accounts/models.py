from django.db import models

# Create your models here.
class error_msg(models.Model):
    def __init__(self,username,emailid):
        self.username  = username
        self.email = emailid