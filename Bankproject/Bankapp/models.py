from django.db import models

# Create your models here.

class applogin(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=120)
    password = models.CharField(max_length=120)

class bankLoging(models.Model):
    account_no = models.BigIntegerField(null=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=120)
    mobile_no = models.BigIntegerField()
    password = models.CharField(max_length=120)
    bank_balance = models.BigIntegerField(null=True,default=0)
    
    def __str__(self):
        return str(self.account_no)

class transaction_details(models.Model):
    credited_detials = models.CharField(max_length=500,null=True)
    deposit_detials = models.CharField(max_length=500,null=True)
    account_no = models.ForeignKey(bankLoging,on_delete=models.CASCADE)

   

