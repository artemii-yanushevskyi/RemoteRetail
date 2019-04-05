from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

from django.conf import settings
from django.shortcuts import redirect

from .forms import LoginForm

def index(request):
    if not request.user.is_authenticated:
        # return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        return HttpResponse("You have to log in.")
    else:
        return render(request, 'purchasetap/index.html')

def login_seller(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/tap/')
            else:
                return HttpResponse("Can not log in.")
    else:
        form = LoginForm()

    return render(request, 'purchasetap/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponse("Logged out.")
