from django.db import models
from authentication.models import Account

class Lead(models.Model):
    name            = models.CharField(max_length=50)
    email           = models.EmailField(max_length=100, unique=True)
    phone_number    = models.IntegerField()
    state           = models.CharField(max_length=50)
    assigned_to     = models.CharField(max_length=50)
    # user_id         = models.ForeignKey('Account', on_delete=models.CASCADE)
    add_remark      = models.CharField(max_length=50)
    
    STATUS_CHOICES  = (('newlead','New Lead'),('hotlead','Hot Lead'),('medlead','Med Lead'),('greylead','Grey Lead'),('success','Success'))
    status          = models.CharField(max_length=50, choices=STATUS_CHOICES)

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
# class Remark(models.Model):
#     created_at      = models.DateTimeField(auto_now_add=True)
#     lead_id         = models.ForeignKey('Lead', on_delete=models.CASCADE)
#     user_id         = models.ForeignKey('Lead', on_delete=models.CASCADE)