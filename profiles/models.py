from django.db import models

class Accounts (models.Model):
    account_number = models.IntegerField()
    balance = models.IntegerField(default=100)
    user_name = models.CharField(max_length = 150, default = None)
    
    def __str__(self):
         return str(self.account_number)

class Transactions(models.Model):
    debited_account_id = models.IntegerField()
    credited_account_id = models.IntegerField()
    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
         return str(self.created_at)
    
