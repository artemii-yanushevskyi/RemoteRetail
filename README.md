## index.html:

purchasesTable - out: item, seller, price, amount (you bought) + generate summaries (like total price); IN: item (dropping down list?);

~~salesTable - out: item, price, amount (you saled); IN: item, price, seller (void adding);~~

nickname - User model's Name (Nickname) property;

saleForm - Form for new sale input;

balance - total amount of "coins" for user, maybe included in purchasesTable;

## purchase.html

nickname (username)

name (name ot item that you bought)

seller (whose item you bought)

price (how much you paid for this item)

balance (your current balance after this purchase)

**Additional**: 

daytime

## For JS:

WritePurchasesTable - js method which outputs purchasesTable;

WriteSalesTable - js method which outputs salesTable;