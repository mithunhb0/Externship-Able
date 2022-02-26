from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from authentication.forms import RegistrationForm
from authentication.models import Account
from dashboard.models import Lead, Remark
from django.contrib.auth.decorators import login_required 
from django.views.decorators.csrf import csrf_exempt

# from rest_framework.viewsets import *
# from rest_framework.authentication import JSONWebTokenAuthentication
# from rest_framework.permissions import IsAuthenticated

 
 

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            account = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password)
            account.phone_number = phone_number
            account.save()
            
            return HttpResponseRedirect("/login/")
    
        
    context = {
        'form': form,
    }
    return render(request, 'authentication/register.html', context)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            auth.login(request, user)

            if user.is_staff == True:
                return HttpResponseRedirect('/dashboard/')
            else:
                messages.info(request,'You are not varified, Please cantact Manager ')
                return HttpResponseRedirect('/login/')

        else:
            messages.info(request,'Invalid credentials')
            return HttpResponseRedirect('/login/')
        
    
    return render(request, "authentication/login.html")

@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')

@login_required(login_url = 'login')
def test(request):
    account = Account.objects.all()
    print('account',account)
    remark = Remark()
    print('remark',remark.remark_area)
    print(remark.remark_area)
    

  


    lead = Lead.objects.all()
    print(lead)
    context = {
        
        'lead':lead
        
    }
    return render(request, "authentication/test.html", context)