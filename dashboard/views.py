from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 
from dashboard.models import Lead
from dashboard.forms import LeadForm
from authentication.models import Account
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


@login_required(login_url = 'login')
@csrf_exempt
def display(request):
    form = LeadForm()
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            status = form.cleaned_data['status']
            add_remark = form.cleaned_data['add_remark']
            
            form.save()
            messages.info(request, "Remark data saved")
            return redirect('/')
        else:
            messages.info(request, "Not saved")
            return redirect('/')
    
    
    lead = Lead.objects.all()
    account = Account.objects.all()
    new  = Lead.objects.filter(status__iexact='newlead')
    
    context = {
        'lead':lead,
        'form':form,
        'new':new,
        'account':account,
        
    }
    return render(request, 'dashboard/display.html',context)

@login_required(login_url = 'login')
def newlead(request):
    new  = Lead.objects.filter(status__iexact='newlead')

    context = {
        'new':new
    }
    return render(request, 'dashboard/newlead.html',context)

@login_required(login_url = 'login')
def hotlead(request):
    hot  = Lead.objects.filter(status__iexact='hotlead')

    context = {
        'hot':hot
    }
    return render(request, 'dashboard/hotlead.html',context)