super user login are:
username : admin@1120
password : 1120

mughilan@1120
1120

from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Dummy authentication
        if username == 'admin' and password == 'admin123':
            request.session['username'] = username
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'login.html')

def dashboard(request):
    if 'username' in request.session:
        return render(request, 'dashboard.html', {'username': request.session['username']})
    return redirect('login')

def logout(request):
    request.session.flush()
    return redirect('login')


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
import random

def sib_createAcc(request):
    if request.method == "POST":
        name = request.POST['fname']
        email = request.POST['email']
        mobile = request.POST['mobile_no']
        password = request.POST['password']
        account_no = random.randint(10**11, 10**12 - 1)

        # Generate a random 6-digit OTP
        otp = random.randint(100000, 999999)

        try:
            # Save the new account to the database
            obj = bankLoging(account_no=account_no, name=name, email=email, mobile_no=mobile, password=password)
            obj.save()

            # Compose the email
            subject = "Your OTP Code"
            message = f"Hello {name},\n\nYour OTP code is: {otp}\n\nThank you for creating an account with us!"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]

            try:
                # Send the email
                send_mail(subject, message, from_email, recipient_list)

                # Save OTP and user details in the session for verification
                request.session['otp'] = otp
                request.session['email'] = email

                return render(request, 'verify_otp.html', {'email': email})
            except Exception as e:
                # Handle email sending failure
                error_message = f"Failed to send OTP email: {e}"
                return render(request, 'create_new_acc.html', {'message': error_message})

        except Exception as e:
            # Handle database saving errors
            message = "Error: Entered email or password is already existing. Please try a different email or password."
            return render(request, 'create_new_acc.html', {'message': message})

    else:
        # Render the account creation form for GET requests
        return render(request, 'create_new_acc.html')
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
import random

def sib_createAcc(request):
    if request.method == "POST":
        name = request.POST['fname']
        email = request.POST['email']
        mobile = request.POST['mobile_no']
        password = request.POST['password']
        account_no = random.randint(10**11, 10**12 - 1)

        # Generate a random 6-digit OTP
        otp = random.randint(100000, 999999)

        try:
            # Save the new account to the database
            obj = bankLoging(account_no=account_no, name=name, email=email, mobile_no=mobile, password=password)
            obj.save()

            # Compose the email
            subject = "Your OTP Code"
            message = f"Hello {name},\n\nYour OTP code is: {otp}\n\nThank you for creating an account with us!"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]

            try:
                # Send the email
                send_mail(subject, message, from_email, recipient_list)

                # Save OTP and user details in the session for verification
                request.session['otp'] = otp
                request.session['email'] = email

                return render(request, 'verify_otp.html', {'email': email})
            except Exception as e:
                # Handle email sending failure
                error_message = f"Failed to send OTP email: {e}"
                return render(request, 'create_new_acc.html', {'message': error_message})

        except Exception as e:
            # Handle database saving errors
            message = "Error: Entered email or password is already existing. Please try a different email or password."
            return render(request, 'create_new_acc.html', {'message': message})

    else:
        # Render the account creation form for GET requests
        return render(request, 'create_new_acc.html')
