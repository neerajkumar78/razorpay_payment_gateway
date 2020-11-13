from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt
import os
import json
key_id=os.environ.get('RAZORPAY_KEY_ID') #assign your id
secret_key=os.environ.get('RAZORPAY_SECRET_KEY') #assign your secret key
client = razorpay.Client(auth =(key_id , secret_key))
def home(request):
    return render(request, 'index.html')
def pay(request):
    context={}
    if request.method == "POST":
        name = request.POST.get('name')
        phone=os.environ.get('MY_PHONE')#assign your phone no
        email=os.environ.get('MY_EMAIL')#assign your email id
        amount = int(request.POST.get('amount')) * 100
        
        payment = client.order.create({'amount':amount, 'currency':'INR',
                              'payment_capture':'1' })
    
        order_id = payment['id']
        order_status = payment['status']

        if order_status=='created':

            # Server data for user convinience
            context['amount'] = amount
            context['name'] = name
            context['phone'] = phone
            context['email'] = email
            context['key']=key_id

            # data that'll be send to the razorpay for
            context['order_id'] = order_id 
            print(key_id)       
        return render(request, 'pay.html' ,{'context': context})
    return render(request, 'index.html')


@csrf_exempt
def confirm(request):
    context={}
    response = request.POST

    params_dict = {
        'razorpay_payment_id' : response['razorpay_payment_id'],
        'razorpay_order_id' : response['razorpay_order_id'],
        'razorpay_signature' : response['razorpay_signature']
    }


    # VERIFYING SIGNATURE
    try:
        status = client.utility.verify_payment_signature(params_dict)
        context['flag']=True
        context['status']="Payment Successful"
        return render(request, 'status.html', {'context':context})
    except Exception as e:
        print(e)
        context['flag']=False
        context['status']="Payment Faliure!!!"
        return render(request, 'status.html', {'context':context})