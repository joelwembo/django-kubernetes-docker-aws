from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    organisation = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=14)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        managed = True
        db_table = "contact"

 # context = {'amount': investamount, 'ir': ir, 'period': duration, 'totalinterest': totalinterest,
 #               'totalROIA': totalROIA, 'totalinvest': totalinvest, 'oneROIA': oneROIA, 'oneinterest': oneinterest}

class RoiInvestment(models.Model):
    amount = models.CharField(max_length=200)
    totalinterest = models.CharField(max_length=200)
    ir = models.CharField(max_length=200)
    period = models.CharField(max_length=200)
    totalROIA = models.CharField(max_length=200)
    totalinvest = models.CharField(max_length=200)
    oneROIA = models.CharField(max_length=200)
    oneinterest = models.CharField(max_length=200)
