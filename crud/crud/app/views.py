from django.shortcuts import render, redirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Sum, Count, Avg, Max, Min, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from app.forms import Record
from app.models import RecordTable
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


def SignupPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            return HttpResponse("Your password and confirm Password are not same!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect("home")

    return render(request, 'signup.html')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse

def LoginPage(request):
    error_message = None

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return redirect('home')
        else:
            error_message = "Username or password incorrect!"

    return render(request, 'login.html', {'error_message': error_message})

def LogoutPage(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    if request.method == 'POST':
        form = Record(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            emaill = form.cleaned_data['email']
            phone_no = form.cleaned_data['phone']
            city = form.cleaned_data['city']
            db_table = RecordTable(
                first_name=fname, last_name=lname, email=emaill, phone=phone_no, city=city)
            db_table.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Thank You, your data has been submitted")

    else:
        form = Record()
    search_id = request.GET.get('id', None)

    if search_id:
        record = RecordTable.objects.filter(pk=search_id)
    else:
        record = RecordTable.objects.all()
    return render(request, 'index.html', context={'form': form, 'row': record})


def edit(request, id):
    record = get_object_or_404(RecordTable, pk=id)
    if request.method == 'POST':
        form = Record(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Your Data has been changed Successfully!")
            return redirect('home')
    else:
        form = Record(instance=record)
    return render(request, 'index.html', {'form': form, 'record': record})


def delete(request, id):
    try:
        record = RecordTable.objects.get(pk=id)
        record.delete()
        return redirect('home')
    except RecordTable.DoesNotExist:
        return HttpResponseNotFound("Record not found")


