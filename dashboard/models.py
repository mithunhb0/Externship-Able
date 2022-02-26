from django.db import models
from authentication.models import Account

class Lead(models.Model):
    name            = models.CharField(max_length=50)
    email           = models.EmailField(max_length=100, unique=True)
    phone_number    = models.IntegerField(max_length=10,null=True)
    state           = models.CharField(max_length=50)
    assigned_to     = models.CharField(max_length=50)
    
    STATUS_CHOICES  = (('newlead','New Lead'),('hotlead','Hot Lead'),('medlead','Med Lead'),('greylead','Grey Lead'),('success','Success'))
    status          = models.CharField(max_length=50)

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    user_id         = models.ForeignKey(Account,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Remark(models.Model):
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    lead_id         = models.ForeignKey(Lead,null=True, on_delete=models.CASCADE)
    user_id         = models.ForeignKey(Account,null=True, on_delete=models.CASCADE)
    remark_area     = models.CharField(max_length=100)