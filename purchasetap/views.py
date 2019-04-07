from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils import timezone

from django.conf import settings
from django.shortcuts import redirect

from .forms import LoginForm
from .models import Product, Purchase

def index(request):
    if not request.user.is_authenticated:
        # return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        return HttpResponseRedirect('login')
    else:
        username = str(request.user.username)
        products = Product.objects.all()
        purchases = Purchase.objects.all().order_by('-created')
        return render(request, 'purchasetap/index.html', {
            'products': products,
            'username': username,
            'time': timezone.now(),
            'purchases': purchases,
        })

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

def count(request):
    username = request.user.username
    u = User.objects.get(username=username)
    p = Product.objects.get(name=request.POST['product'])
    Purchase.objects.create(seller=u, product=p)
    data = {
        'email': User.objects.get(username='oleh').email,
        'request': str(vars(request))
    }
    return JsonResponse(data)

def logout_view(request):
    logout(request)
    return HttpResponse("<h1>Logged out</h1>")
