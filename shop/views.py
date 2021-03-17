from django.db.models import query
from django.shortcuts import render
from django.http import HttpResponse
from .models import Order, OrderUpdate, Product, Contact
from math import ceil
import json
from django.contrib import messages

# Create your views here.


def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4+ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {"allProds": allProds}
    return render(request, 'shop/index.html', params)



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        phone = request.POST.get('phone', 123456789)
        message = request.POST.get('message', "")
        msg = Contact(Name=name, Email=email, Phone=phone, Message=message)
        messages.success(request,'Thanks for getting in touch! We appreciate you contacting us. One of our colleagues will get back in touch with you soon! Have a great day!')
        # msg.save()
    return render(request, 'shop/contact.html')


def tracker(request):
    if request.method == 'POST':
        orderId = request.POST.get('orderId', 0)
        email = request.POST.get('email', '')
        try:
            update = OrderUpdate.objects.filter(Order_id=orderId, Email=email)
            if len(update) > 0:
                details = []
                for item in update:
                    details.append(
                        {'text': item.Order_update, 'time': item.timestamp,'cartItem':item.Cart_item})
                    response = json.dumps(details, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')

def searchMatch(query:str,item:list):
    if query in item.product_name.lower() or query in item.desc.lower():
        return True
    return False

def search(request):
    found:bool=True
    if request.method=='GET':
        query=request.GET.get('search')
        allProds=[]
        catprods = Product.objects.values('category', 'id')
        cats = {item['category'] for item in catprods}
        for cat in cats:
            prodtemp = Product.objects.filter(category=cat)
            prod=[item for item in prodtemp if searchMatch(query,item)]          
            n = len(prod)
            nSlides = n//4+ceil((n/4)-(n//4))
            if n>0:
                found=False
                allProds.append([prod, range(1, nSlides), nSlides])
    params = {"allProds": allProds,'found':found}
    return render(request, 'shop/index.html', params)



def productView(request, myid):
    prod = Product.objects.filter(id=myid)
    params = {'product': prod[0]}
    return render(request, 'shop/prodView.html', params)


def checkout(request):
    if request.method == "POST":
        name = f"{request.POST.get('firstname','')} {request.POST.get('lastname','')}"
        email = request.POST.get('email', '')
        phone = f"{request.POST.get('phone1',0)} {request.POST.get('phone2',1)}"
        address = request.POST.get('address', '')
        state = request.POST.get('state', '')
        city = request.POST.get('city', '')
        pincode = request.POST.get('pincode', 0000)
        items = request.POST.get('jsonCart', '')
        order = Order(Name=name, Email=email, Phone=phone,
                      Address=address, State=state, City=city, Pincode=pincode)
        order.save()
        id = order.id
        details = OrderUpdate(Order_id=id, Email=email, Cart_item=items,
                              Order_update="Your order has been placed it will be deliverd shortly")
        details.save()
        return render(request, 'shop/checkout.html', {'ordered': True, 'id': id})
    return render(request, 'shop/checkout.html')
