from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 
from dashboard.models import Lead, Remark
from dashboard.forms import LeadForm, RemarkForm
from authentication.models import Account
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


@login_required(login_url = 'login')
@csrf_exempt
def display(request):
    lead = Lead.objects.all()
    account = Account.objects.all()
    new  = Lead.objects.filter(status__iexact='newlead')
    
    context = {
        'lead':lead,
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


def addremark(request):
    remark_form = RemarkForm()
    if request.method == 'POST':
        remark_form = RemarkForm(request.POST)
        if remark_form.is_valid():            
            remark_form.save()
            messages.info(request, "status data saved")
            return redirect('/')
        else:
            messages.info(request, "Not saved")
            return redirect('/')
    else:
            messages.info(request, "Not saved")
            return redirect('/')