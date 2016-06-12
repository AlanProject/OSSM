from django.shortcuts import render,Http404,HttpResponse
from Control import models
from Control.models import auth_models
from Control.froms import Register
# Create your views here.


def control(request):
    return render(request, 'control.html')


def monitor(request):
    return render(request, 'monitor.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    froms_data = ''
    if request.method == "POST":
        froms_data = Register(request.POST)
        if froms_data.is_valid():
            request_from = froms_data.clean()
            name = request_from.get('name')
            email = request_from.get('email')
            passwd = request_from.get('passwd')
            auth_models.UserProfile.objects.create_user(email, name, passwd)
    return render(request, 'register.html', {'request_from': froms_data})

def pages(request):
    if request.method == 'GET':
        pag = request.GET.get('pag')
        type = request.GET.get('type')
        return render(request, 'AdminLTE/pages/%s/%s.html' %(type, pag))
def host_list(request):
    return render(request, 'Control/host_list.html')