"""
Auth through corporate mail or co-working OAuth or co-working email
- main page - dashboard
    - purchased goods
    - offered goods



"""

from ..models import Patron, Wallet
from django.shortcuts import render
from django.http import HttpResponse



def landing_page(request):
    patrons = Patron.objects.order_by('nickname')
    session = [key + ': ' + value for key, value in request.session.items()]
    return render(request, 'retail/index.html', {
        'patrons': patrons,
        'session': str(session),
    })
    
def dashboard(request, nickname):
    patron = Patron.objects.get(nickname=nickname)
    wallet = Wallet(patron=patron, balance=5)
    request.session['nickname'] = nickname
    response = render(request, 'retail/dashboard.html', {
            'patron': patron,
            'wallet': wallet,
            })
    return response

def process_qr(request):
    
    # who buys??
    if 'nickname' in request.session:
        nickname = request.session['nickname']
        if Patron.objects.filter(nickname=nickname).exists():
            buyer = Patron.objects.get(nickname=nickname)
        else:
            return landing_page(request)
        purchase_qr = request.GET
        
        seller = Patron.objects.get(nickname=purchase_qr['seller'])
        # if seller doesn't exist, create patron
        purchase = Purchase.objects.create(good=purchase_qr['name'], price=purchase_qr['price'], seller=seller, buyer=buyer)
    
        return render(request, 'retail/purchase.html', {
            'purchase': purchase,
        })
    else:
        # send to identify
        return landing_page(request)

    