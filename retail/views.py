from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
# from .models import ModelName

# Create your views here.

def landing_page(request):
    patrons = Patron.objects.order_by('nickname')
    return render(request, 'retail/index.html', {
        'patrons': patrons,
    })