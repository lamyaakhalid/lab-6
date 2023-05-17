from django.shortcuts import render

tax_rate= 0.15

def index(request):
    return render(request,'index.html')

def tax(request, num):
    return render(request,'tax.html', {"tnum": num + tax_rate*num})

def rate(request):
    return render(request,'rate.html', {'tax': tax_rate})
