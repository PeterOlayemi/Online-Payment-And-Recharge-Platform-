from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import DataForm, AirtimeForm, BankForm, WithForm, ElectForm, EducationForm, CableForm
from account.models import Myuser

# Create your views here.

@login_required
def dashboard(request):
    data = Myuser.objects.filter(owner=request.user).all()
    return render(request, 'user/dashboard.html', {'data':data})

@login_required
def querybill(request):
    data = Myuser.objects.filter(owner=request.user)
    air=Cable.objects.filter(owner=request.user).order_by('-date')
    date=Elect.objects.filter(owner=request.user).order_by('-date')
    bill=Education.objects.filter(owner=request.user).order_by('-date')

    context = {
            'air':air,
            'data':data,
            'date':date,
            'bill':bill
        }
    return render(request,'user/querybill.html', context)

@login_required
def querybill1(request, _id):
    air =Cable.objects.filter(owner=request.user).get(id=_id)
    air.queried=True
    air.save()
    return redirect(f'/user/query_bill/')

@login_required
def querybill2(request, _id):
    date =Elect.objects.filter(owner=request.user).get(id=_id)
    date.queried=True
    date.save()
    return redirect(f'/user/query_bill/')

@login_required
def querybill4(request, _id):
    date =Education.objects.filter(owner=request.user).get(id=_id)
    date.queried=True
    date.save()
    return redirect(f'/user/query_bill/')

@login_required
def cable(request):
    msg = None
    data = Myuser.objects.filter(owner=request.user)
    air = Cable.objects.filter(owner=request.user).order_by('-date')
    if request.method == 'POST':
        form = CableForm(request.POST)
        if form.is_valid():
            date=form.save(commit=False)
            for obj in data:
                if obj.balance > date.plan.amount or obj.balance == date.plan.amount:
                    date.owner=request.user
                    date.save()
                    obj.balance -= date.plan.amount
                    obj.save()
                    return redirect(f'/user/cable_success/')
                else:
                    msg = 'Insufficient Balance'
    else:
        form = CableForm()
 
    context = {
            'air':air,
            'msg':msg,
            'form':form,
            'data':data,
        }
    return render(request,'user/cable.html', context)

def load_cable_plans(request):
    service_id = request.GET.get('service')
    plans = CablePlan.objects.filter(service_id=service_id)
    return render(request, 'user/plan_dropdown.html', {'plans': plans})

@login_required
def cab(request):
    return render(request, 'user/cab.html')

@login_required
def elect(request):
    msg=None
    data = Myuser.objects.filter(owner=request.user)
    air =Elect.objects.filter(owner=request.user).order_by('-date')
    if request.method == 'POST':
        form = ElectForm(request.POST)
        if form.is_valid():
            date=form.save(commit=False)
            for obj in data:
                if obj.balance > date.amount or obj.balance == date.amount:
                    date.owner=request.user
                    date.save()
                    obj.balance -= date.amount
                    obj.save()
                    return redirect(f'/user/purchase/')
                else:
                    msg = 'Insufficient Balance'
    else:
        form = ElectForm()
 
    context = {
            'air':air,
            'msg':msg,
            'form':form,
            'data':data,
        }
    return render(request,'user/elect.html', context)

@login_required
def purchase(request):
    return render(request, 'user/purchase.html')

@login_required
def edu(request):
    msg = None
    data = Myuser.objects.filter(owner=request.user)
    air =Education.objects.filter(owner=request.user).order_by('-date')
    form = EducationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            date=form.save(commit=False)
            for obj in data:
                if obj.balance > date.quantity.amount or obj.balance == date.quantity.amount:
                    date.owner=request.user
                    date.save()
                    obj.balance -= date.quantity.amount
                    obj.save()
                    return redirect(f'/user/education_success/')
                else:
                    msg = 'Insufficient Balance'
 
    context = {
            'air':air,
            'msg':msg,
            'form':form,
            'data':data,
        }
    return render(request,'user/edu.html', context)

def load_edu_quantity(request):
    service_id = request.GET.get('service')
    quantity = Checker.objects.filter(service_id=service_id)
    return render(request, 'user/plan_dropdown.html', {'plans': quantity})

@login_required
def sock(request):
    return render(request, 'user/sock.html')

@login_required
def fund(request):
    data = Myuser.objects.filter(owner=request.user)
    return render(request, 'user/fund.html', {'data':data})

@login_required
def center(request):
    data = Myuser.objects.filter(owner=request.user)
    return render(request, 'user/center.html', {'data':data})

@login_required
def buydata(request):
    msg = None
    data = Myuser.objects.filter(owner=request.user)
    ava = Availability.objects.all()
    air =Data.objects.filter(owner=request.user).order_by('-date_updated')
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            date=form.save(commit=False)
            for obj in data:
                if obj.balance == date.plan.amount or obj.balance > date.plan.amount:
                    date.owner=request.user
                    date.save()
                    obj.balance -= date.plan.amount
                    obj.save()
                    return redirect(f'/user/buy_success/')
                else:
                    msg = 'Insufficient Balance'
    else:
        form = DataForm()
 
    context = {
            'air':air,
            'msg':msg,
            'ava':ava,
            'form':form,
            'data':data,
        }
    return render(request,'user/data.html', context)

def load_plans(request):
    service_id = request.GET.get('service')
    plans = Plan.objects.filter(service_id=service_id).order_by('plan')
    return render(request, 'user/plan_dropdown.html', {'plans': plans})

@login_required
def data(request):
    data = Myuser.objects.filter(owner=request.user)
    air =Data.objects.filter(owner=request.user).order_by('-date_updated')
    return render(request,'user/querydata.html', {'air':air, 'data':data})

@login_required
def querydata(request, _id):
    air =Data.objects.filter(owner=request.user).get(id=_id)
    air.queried=True
    air.save()
    return redirect(f'/user/query_data/')

@login_required
def bank(request):
    data = Myuser.objects.filter(owner=request.user)
    air =Bank.objects.filter(owner=request.user).order_by('-date_added')
    if request.method == 'POST':
        form = BankForm(request.POST)
        if form.is_valid():
            date=form.save(commit=False)
            date.owner=request.user
            date.save()
            return redirect(f'/user/add_success/')
    else:
        form = BankForm()
 
    context = {
            'air':air,
            'form':form,
            'data':data
        }
    return render(request,'user/bank.html', context)

@login_required
def banker(request):
    return render(request, 'user/banker.html')

@login_required
def delete(request, _id):
    delete=Bank.objects.get(id=_id)
    delete.delete()
    return HttpResponseRedirect(reverse('user:bank'))

@login_required
def default(request, _id):
    air =Bank.objects.filter(owner=request.user).get(id=_id)
    air.default=True
    air.save()
    return redirect(f'/user/bank_details/')

@login_required
def buyairtime(request):
    msg=None
    data = Myuser.objects.filter(owner=request.user)
    air =Airtime.objects.filter(owner=request.user).order_by('-date_updated')
    if request.method == 'POST':
        form = AirtimeForm(request.POST)
        if form.is_valid():
            date=form.save(commit=False)
            for obj in data:
                if obj.balance == date.amount or obj.balance > date.amount:
                    date.owner=request.user
                    pack = (5/100)*date.amount
                    obj.balance -= date.amount
                    obj.balance += pack
                    date.amount -= pack
                    date.save()
                    obj.save()
                    return redirect(f'/user/get_success/')
                else:
                    msg = 'Insufficient Balance'
    else:
        form = AirtimeForm()
 
    context = {
            'air':air,
            'msg':msg,
            'form':form,
            'data':data
        }
    return render(request,'user/airtime.html', context)

@login_required
def airtime(request):
    data = Myuser.objects.filter(owner=request.user)
    air =Airtime.objects.filter(owner=request.user).order_by('-date_updated')
    return render(request,'user/queryairtime.html', {'air':air, 'data':data})

@login_required
def queryairtime(request, _id):
    air =Airtime.objects.filter(owner=request.user).get(id=_id)
    air.queried=True
    air.save()
    return redirect(f'/user/query_airtime/')

@login_required
def success(request):
    return render(request, 'user/response.html')

@login_required
def response(request):
    return render(request, 'user/success.html')

@login_required
def bill(request):
    data = Myuser.objects.filter(owner=request.user)
    return render(request, 'user/bill.html', {'data':data})

@login_required
def faq(request):
    data = Myuser.objects.filter(owner=request.user)
    return render(request, 'user/faq.html', {'data':data})

@login_required
def withdraw(request):
    msg=None
    data = Myuser.objects.filter(owner=request.user)
    air =With.objects.filter(owner=request.user).order_by('-date')
    if request.method == 'POST':
        form = WithForm(request.POST)
        if form.is_valid():
            date=form.save(commit=False)
            if date.amount > 99:
                if date.amount > 999:
                    date.charge = 100
                else:
                    date.charge = 50
                date.owner=request.user
                for obj in data:
                    if obj.balance == date.amount or obj.balance > date.amount:
                        obj.balance -= date.amount
                        if obj.balance == date.charge or obj.balance > date.charge:
                            obj.balance -= date.charge
                            obj.save()
                            date.save()
                            return redirect(f'/user/withdraw_update/')
                        else:
                            msg = 'Insufficient balance cos of charges'
                    else:
                        msg = 'Insufficient Balance'
            else:
                msg='minimum withdrawal is #100'
    else:
        form = WithForm()
 
    context = {
            'air':air,
            'msg':msg,
            'form':form,
            'data':data
        }
    return render(request,'user/with.html', context)

@login_required
def withdrawer(request):
    return render(request, 'user/withdraw.html')

@login_required
def withe(request):
    data = Myuser.objects.filter(owner=request.user)
    air =With.objects.filter(owner=request.user).order_by('-date')
    return render(request,'user/querywith.html', {'air':air, 'data':data})

@login_required
def querywithe(request, _id):
    air =With.objects.filter(owner=request.user).get(id=_id)
    air.queried=True
    air.save()
    return redirect(f'/user/query_withdrawal/')
