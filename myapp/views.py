from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.

def homepage(request):
    if request.method == 'POST':
        product_form = dataForm(request.POST)
        if product_form.is_valid():
            product_form.save()
        return redirect(homepage)
    
    product_form = dataForm()
    product = data.objects.all()

    context = ({'product_form':product_form , 'product': product })
    return render(request,'homepage.html',context)