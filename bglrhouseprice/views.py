from django.shortcuts import render

def Home(request):
    return render(request,'index.html')

def Estimate(request):
    return render(request,'estimate.html')