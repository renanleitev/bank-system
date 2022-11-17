from django.urls import re_path, path
from . import views
from profiles.views import TransactionsListView

app_name = "profiles"

urlpatterns = [
    re_path("account_status/", views.index, name = "account_status"),
    re_path("money_transfer/", views.money_transfer, name = "money_transfer"),
    re_path("view_transactions/", TransactionsListView.as_view(), name = "view_transactions"),
]
