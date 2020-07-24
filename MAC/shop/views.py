from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Orders
from math import ceil
def index(request):
    products = Product.objects.all()

    # params = {'no_of_slides':nslides,'range':range(1,nslides),'product':products}
    # allprods = [[products,range(1,nslides),nslides],
    #             [products,range(1,nslides),nslides]]
    allprods = []
    catprods = Product.objects.values('categary','id')
    cats = {item['categary'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(categary=cat)
        n = len(products)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod,range(1,nslides),nslides])

    params = {'allprods':allprods}

    return render(request,"shop/index.html", params)



def about(request):
    return render(request,"shop/about.html")


def contact(request):
    if request.method == "POST":

        name = request.POST.get('name','')
        email =request.POST.get('email','')
        phone =request.POST.get('phone','')
        desc =request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()

    return render(request,"shop/contact.html")



def tracker(request):
    return render(request,"shop/tracker.html")


def search(request):
    return render(request,"shop/search.html")


def productview(request,myid):
    product = Product.objects.filter(id=myid)

    return render(request,"shop/productview.html",{'product':product[0]})


def checkout(request):
    if request.method == "POST":

        items_json = request.POST.get('itemsjson','')
        name = request.POST.get('name','')
        amount = request.POST.get('amount','')
        email =request.POST.get('email','')
        address =request.POST.get('address1','') + " " + request.POST.get('address2','')
        city =request.POST.get('city','')
        state =request.POST.get('state','')
        zip_code =request.POST.get('zip_code','')
        phone = request.POST.get('phone', '')
        Order=Orders(items_JSON=items_json,name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone,amount=amount)
        Order.save()
        thank = True
        return render(request,"shop/checkout.html",{'thank': thank})
    return render(request,"shop/checkout.html")


