from django.shortcuts import render, redirect
from . import forms
from . import models
from profiles.models import Accounts 
from django.db.models import Q
from django_tables2 import SingleTableView
from .tables import TransactionsTable
import random

def randomGen():
    return int(random.uniform(100000, 999999))

def index(request):
    try:
        curr_user = Accounts.objects.get(user_name=request.user)
    except:
        curr_user = Accounts()
        curr_user.account_number = randomGen() 
        curr_user.balance = 100
        curr_user.user_name = request.user
        curr_user.save()
    return render(request, "profiles/profile.html", {"curr_user": curr_user})

def money_transfer(request):
    if request.method == "POST":
        form = forms.TransactionsForm(request.POST)
        if form.is_valid():
            curr_user = models.Accounts.objects.get(account_number=form['debited_account_id'].value())
            dest_user = models.Accounts.objects.get(account_number=form['credited_account_id'].value())
            transfer_amount = int(form['value'].value()) 
            if (curr_user.balance >= transfer_amount) and (curr_user != dest_user): 
                form.save()
                curr_user.balance = curr_user.balance - transfer_amount
                dest_user.balance = dest_user.balance + transfer_amount
                curr_user.save()
                dest_user.save()
        return redirect("profiles/profile.html")
    else:
        form = forms.TransactionsForm()
    return render(request, "profiles/money_transfer.html", {"form": form})

class TransactionsListView(SingleTableView):
    model = models.Transactions
    table_class = TransactionsTable
    template_name = 'profiles/view_transactions.html'
    
    def get_queryset(self):
            curr_user = Accounts.objects.get(user_name=self.request.user)
            conta = curr_user.account_number        
            return super().get_queryset().filter(Q(debited_account_id=conta) | Q(credited_account_id=conta))
    
