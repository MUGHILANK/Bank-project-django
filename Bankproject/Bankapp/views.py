from django.shortcuts import render,redirect,HttpResponse
from .models import applogin,bankLoging,transaction_details
from django.contrib.auth import authenticate,login,logout
import random
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime

# Create your views here.

def random_number():
    random_number = random.randint(10**11, 10**12 - 1)
    return random_number

def current_datetime():
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%A, %d %B %Y %I:%M %p")
    return formatted_datetime

def sib_register(request):
    if request.method == "POST":
        name = request.POST['fname']
        email = request.POST['email']
        password = request.POST['password']

        try:
            obj = applogin(name = name,email=email,password=password)
            obj.save()
            return redirect('sib_login')
        except Exception:
            message = "Error: Entered email or password is already exiting. Please try different mail ID or passwaord...!"
            return render(request,'SIB_register.html',{'message':message})
    else:              
        return render(request,'SIB_register.html')

def sib_createAcc(request):
    if request.method == "POST":
        name = request.POST['fname']
        email = request.POST['email']
        mobile = request.POST['mobile_no']
        password = request.POST['password']
        account_no = random_number()

        try:
            obj = bankLoging(account_no=account_no,name=name,email=email,mobile_no=mobile,password=password)
            obj.save()

            # Compose the email
            subject = "welcome to SIB"
            message = f"Hello,\n\nYour Account Number is: {account_no}\n\nThank you!"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]

            # Send the email
            try:
                send_mail(subject, message, from_email, recipient_list)
                return redirect('sib_accVerifiy')
            except Exception as e:
                return HttpResponse(e)
               
        except Exception:
            message = "Error: Entered email or password is already exiting. Please try different mail ID or passwaord...!"
            return render(request,'create_new_acc.html',{'message':message})
           
    else:
        return render(request,'create_new_acc.html')

def sib_login(request):
    if request.method =='POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            login_values = applogin.objects.all()
            for i in login_values:
                if email == i.email and password == i.password:
                    return redirect('sib_accVerifiy')
                    
        except Exception:
            message = "Error: Please Check your Email or password...!"
            return render(request,'SIB_login.html',{'message':message})

    else:
        return render(request,'SIB_login.html')

def sib_accVerifiy(request):
    if request.method == "POST":
        acc_no = int(request.POST['acc_no'])
        mobile = int(request.POST['mobile_no'])
        password = request.POST['password']

        try: 
            datas = bankLoging.objects.values('mobile_no','password','account_no','name')
            for i in datas:
                if mobile==i['mobile_no'] and password==i['password'] and acc_no == i['account_no']:
                    request.session['username'] = i['name']
                    request.session['mobile_no'] = mobile
                    request.session['account'] = acc_no

                    return redirect('index')
       
        except Exception:
                   message ="Please check your details..?"
                   return render(request,'account_verification.html',{'message':message})

    return render(request,'account_verification.html')

# @login_required
def index(request):
    use_data ={
        'name':request.session.get('username'),
        'account_no':request.session.get('account'),
        'mobile_no':request.session.get('mobile_no'),
    }
    return render(request,'home.html',{'datas':use_data})

def sib_deposit(request):
    if request.method =="POST":
        get_deposit = int(request.POST['deposit'])  
        session_num = request.session.get('account')  

        if session_num: 
            try:
                user_account = bankLoging.objects.get(account_no=session_num)
                user_account.bank_balance += get_deposit
                user_account.save()

            except Exception as message:
                return render(request,'deposit.html',{'message':message})
                
        time_value = current_datetime()
        message = f"{time_value} Deposit Amount: {get_deposit} Current balance: {user_account.bank_balance}"

        transactions = transaction_details.objects.create(deposit_detials=message, account_no=user_account)
        transactions.save()
        return render(request,'deposit.html',{"message":message})
        
    return render(request,'deposit.html')

def sib_withdraw(request):
    if request.method =="POST":
        get_withdraw = int(request.POST['withdraw'])  
        session_num = request.session.get('account')  

        if session_num: 
            try:
                user_account = bankLoging.objects.get(account_no=session_num)
                user_account.bank_balance -= get_withdraw
                user_account.save()

            except Exception as message:
                return render(request,'withdraw.html',{'message':message})
            
        time_value = current_datetime()
        message = f"{time_value} Withdraw Amount: {get_withdraw} Current balance: {user_account.bank_balance}"

        transactions = transaction_details.objects.create(credited_detials=message,account_no = user_account)
        transactions.save()
        return render(request,'withdraw.html',{"message":message})
                
            
    return render(request,'withdraw.html')

def sib_bankbalance(request):
    session_number = request.session.get('account')
    bank_balance = bankLoging.objects.get(account_no=session_number)
    value = bank_balance.bank_balance
    
    return render(request,'bank_balance.html',{'account':session_number,'balance':value})

def sib_Transaction_History(request):
    session_number = request.session.get('account')
     
    try:
        obj = transaction_details.objects.filter(account_no__account_no=session_number)
        
        return render(request,"Transaction_History.html",{"values":obj})

    except Exception as message:
        return render(request,"Transaction_History.html",{"message":message})
    
    # return render(request,"Transaction_History.html")

def logout(request):
    request.session.flush()
    return redirect('sib_login')