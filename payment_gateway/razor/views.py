from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt

import json
def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = int(request.POST.get('amount')) * 100
        client = razorpay.Client(auth =("rzp_test_JlPjzUIwgg90G9" , "uMTMq23rLB6of2AnH4S04u5s"))
        payment = client.order.create({'amount':amount, 'currency':'INR',
                              'payment_capture':'1' })
        
        #coffee = Coffee(name = name , amount =amount , order_id = payment['id'])
        #coffee.save()
        
        return render(request, 'index.html' ,{'payment':payment})
    return render(request, 'index.html')


@csrf_exempt
def confirm(request):
    return render(request, "confirm.html")