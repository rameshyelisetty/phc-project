from django.shortcuts import render

# Create your views here.

def prodhome(request):
    return render(request, 'products/home.html', {'home': 'This is test for product home.'})
