from django.contrib import messages
from django.shortcuts import render, redirect
from book_review.models import Book_Review_forms
from .forms import user_form

def form_view(request):
    if request.method == 'POST':
        form = user_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            request.session['form_submitted'] = True
            request.session.set_expiry(300)
            messages.success(request, 'Saved successfully')
            return redirect('home') 
    else:
        form = user_form()
    return render(request, 'index.html', {'form': form})

def home(request):
    if not request.session.get('form_submitted', False):
        messages.warning(request, 'Please fill the form first!')
        return redirect('form_view')
    
    reviews= Book_Review_forms.objects.all()
    request.session.set_expiry(200)  # Set session expiry to 5 minutes
    return render(request, 'home.html', {'reviews': reviews})
