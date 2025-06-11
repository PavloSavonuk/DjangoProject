from django.shortcuts import render

def home_view(request):
    return render(request, 'pages/home.html')

def view1(request):
    return render(request, 'pages/view1.html')

def view2(request):
    return render(request, 'pages/view2.html')

def view3(request):
    return render(request, 'pages/view3.html')

def view4(request):
    return render(request, 'pages/view4.html')
