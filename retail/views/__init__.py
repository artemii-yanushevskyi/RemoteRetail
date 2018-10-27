"""
Auth through corporate mail or co-working OAuth or co-working email
- main page - dashboard
    - purchased goods
    - offered goods
"""

from ..models import Patron, Wallet, Purchase
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def landing_page(request):
    patrons = Patron.objects.order_by('nickname')
    session = [key + ': ' + value for key, value in request.session.items()]
    from retail.forms import NicknameForm
    
    if request.method == 'POST':
            # could be done this way without validation
            # type = request.POST.get('type')
            form_response = NicknameForm(request.POST)
            if form_response.is_valid():
                nickname = form_response.cleaned_data['nickname']
                # parameters are sent to db, redirecting to this page
                # method will be POST, form will not be resubmitted on page refresh
                # e.g. an http GET after a POST
                return HttpResponseRedirect(reverse('dashboard', args=[nickname]))
                # reverse will return shop/sellername
    
    form = NicknameForm()
    
    return render(request, 'retail/index.html', {
        'patrons': patrons,
        'session': str(session),
        'form': form,
    })
    
def dashboard(request, nickname):
    request.session['nickname'] = nickname
    message = ''
    patron = Patron.objects.get(nickname=nickname)
    if Wallet.objects.filter(patron=patron).exists():
        message += 'patron {} has a wallet'.format(patron.nickname)
    else:
        message += 'patron {} doesn\'t have a wallet, create new'.format(patron.nickname)
        wallet = Wallet.objects.create(patron=patron, balance=25)
    
    purchases = Purchase.objects.order_by('-pk')
    response = render(request, 'retail/dashboard.html', {
            'patron': patron,
            'wallet': patron.wallet,
            'message': message,
            'purchases': purchases
            })
    return response

def process_qr(request):
    '''
    /retail/qr/?price=2000&name=Орео&seller=Влад
    '''
    # who buys??
    if 'nickname' in request.session:
        nickname = request.session['nickname']
        if Patron.objects.filter(nickname=nickname).exists():
            buyer = Patron.objects.get(nickname=nickname)
        else:
            return landing_page(request)
            
        purchase_qr = request.GET
        
        seller = Patron.objects.get(nickname=purchase_qr['seller'])
        
        price=purchase_qr['price']
        
        from decimal import Decimal
        seller_wallet = Wallet.objects.get(patron=seller)
        seller_wallet.balance = seller_wallet.balance + Decimal(price)
        seller_wallet.save()
        
        buyer_wallet = Wallet.objects.get(patron=buyer)
        buyer_wallet.balance = buyer_wallet.balance - Decimal(price)
        buyer_wallet.save()
        
        purchase = Purchase.objects.create(name=purchase_qr['name'], price=price, seller=seller, buyer=buyer)
        
        return render(request, 'retail/purchase.html', {
            'purchase': purchase,
        })
    else:
        # send to identify
        return landing_page(request)

    