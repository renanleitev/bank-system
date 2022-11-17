import django_tables2 as tables
from .models import Transactions

class TransactionsTable(tables.Table):
    class Meta:
        model = Transactions
        template_name = "django_tables2/bootstrap.html"
        fields = ("debited_account_id", "credited_account_id", "value", "created_at")
