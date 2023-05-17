from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def tax(request, num):
    return render(request,'tax.html', {"tnum": num + 0.15*num})

def rate(request, trate):
    return render(request,'rate.html', {'trate': trate})
