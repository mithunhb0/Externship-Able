from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from authentication.forms import RegistrationForm
from authentication.models import Account
from dashboard.models import Lead
from django.contrib.auth.decorators import login_required 

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

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            auth.login(request, user)
            # is_staff = False
            # account = Account.objects.all()
            # print('account',account)
            # print('type of account',type(account))
            # print('email',account.email)
            
            # account = Account.objects.filter(is_staff=request.POST['is_staff'])
            # print('account',account)
            
            # print('account is staff',account.is_staff)
            # if account.is_staff == True:
            #     return HttpResponseRedirect('/dashboard/')
            # else:
            #     messages.info(request,'You are not varified, Please cantact Manager ')
            #     return HttpResponseRedirect('/login/')
            return HttpResponseRedirect('/dashboard/')  
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
    # is_staff = None
    # account = Account.objects.filter(is_staff=is_staff)
    # # data = request.GET.get()
    # print(account)
    
    # if request.user.is_authenticated():
    #     email = request.user.email
    #     id_user = request.user.id
    #     fav = Account.objects.filter(user_id=id_user, email=email)
    #     print(fav)
        
    account = Account.objects.all()
    print('account',account)
    # email = None
    # staff = None
    # a = Account.objects.get(is_staff=staff)
    # print(a.is_staff)
    lead = Lead.objects.all()
    print(lead)
    context = {
        
        'lead':lead
        
    }
    return render(request, "authentication/test.html", context)