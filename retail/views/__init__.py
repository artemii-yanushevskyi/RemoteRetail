"""
Auth through corporate mail or co-working OAuth or co-working email
- main page - dashboard
    - purchased goods
    - offered goods



"""
from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()

def landing_page(request):
    users = User.objects.order_by('username')
    return render(request, 'retail/index.html', {
        'users': users,
    })