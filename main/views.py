from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306275102',
        'name': 'Abraham Jordy Ollen',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
# Create your views here.
