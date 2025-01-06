from django.urls import path
from . import views

urlpatterns = [
    path('',views.sib_login, name ='sib_login'),
    path('sib-register/',views.sib_register, name ='sib_register'),
    path('sib-create-new-account/',views.sib_createAcc, name ='sib_creatAcc'),
    path('sib-accunt-verification/',views.sib_accVerifiy, name ='sib_accVerifiy'),
    path('bank-home/',views.index, name ='index'),
    path('bank-home/deposit/',views.sib_deposit, name ='index-deposit'),
    path('bank-home/withdraw/',views.sib_withdraw, name ='index-withdraw'),
    path('bank-home/bankbalance/',views.sib_bankbalance, name ='index-bankbalance'),
    path('bank-home/transactionhistory/',views.sib_Transaction_History, name ='index-Transaction_History'),
]