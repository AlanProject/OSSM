from django.shortcuts import render,Http404,HttpResponse,HttpResponseRedirect
from Control import models
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from Control.models import auth_models
from Control.froms import RegisterForms, LoginForms
# Create your views here.

@login_required
def control(request):
    return render(request, 'control.html')

@login_required
def monitor(request):
    return render(request, 'monitor.html')


def acc_login(request):
    err_msg = ''
    if request.method == "POST":
        forms_data = LoginForms(request.POST)
        if forms_data.is_valid():
            request_forms = forms_data.clean()
            email = request_forms.get('email')
            passwd = request_forms.get('password')
            print email,passwd
            user = authenticate(username=email, password=passwd)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                err_msg = "Wrong username or password!"
    return render(request, 'login.html', {'err_msg': err_msg})

@login_required
def acc_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def register(request):
    forms_data = ''
    if request.method == "POST":
        forms_data = RegisterForms(request.POST)
        if forms_data.is_valid():
            request_from = forms_data.clean()
            name = request_from.get('name')
            email = request_from.get('email')
            passwd = request_from.get('passwd')
            auth_models.UserProfile.objects.create_user(email, name, passwd)
    return render(request, 'register.html', {'request_from': forms_data})


def pages(request):
    if request.method == 'GET':
        pag = request.GET.get('pag')
        type = request.GET.get('type')
        return render(request, 'AdminLTE/pages/%s/%s.html' %(type, pag))

@login_required
def host_list(request):
    return render(request, 'Control/host_list.html')