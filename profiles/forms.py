from django import forms
from . import models

class TransactionsForm (forms.ModelForm):
    class Meta:
        model = models.Transactions
        fields = [
            "debited_account_id",
            "credited_account_id", 
            "value",
        ]
