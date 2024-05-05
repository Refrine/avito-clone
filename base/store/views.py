from django.shortcuts import render, redirect
from item.models import Category, Item

from .forms import SingupForm

def index(request):
    items = Item.objects.filter(is_sold = False)[0:6]
    categories = Category.objects.all()
    return render(request, 'store/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'store/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SingupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
        else:
            form = SingupForm()
            
            
    form = SingupForm()
    
    return render(request, 'store/signup.html', {
        'form': form
    })
