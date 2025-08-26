from django.contrib import messages # type: ignore
from django.shortcuts import render, redirect # type: ignore
from book_review.models import Book_Review_forms
from .forms import user_form
from django.contrib.auth import authenticate, login, logout, get_user_model # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore

User = get_user_model()

# ---------------- REGISTER ----------------
def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST.get('email')
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return render(request, 'register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, "register.html")

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, "Account created successfully. Please login.")
        return redirect('login')   

    return render(request, "register.html")  


# ---------------- LOGIN ----------------
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('form_view') 
        else:
            messages.error(request, "Invalid credentials")
            return render(request, 'login.html')

    return render(request, 'login.html')  


# ---------------- LOGOUT ----------------
def logout_user(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login') 


# ---------------- ADD REVIEW FORM (index.html) ----------------
@login_required(login_url='login')
def form_view(request):
    if request.method == 'POST':
        form = user_form(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  
            review.save()
            messages.success(request, 'Review saved successfully')
            return redirect('home') 
    else:
        form = user_form()
    return render(request, 'index.html', {'form': form})


# ---------------- LIST ALL REVIEWS (home.html) ----------------
@login_required(login_url='login')
def home(request):
    reviews = Book_Review_forms.objects.all().order_by('-id')
    return render(request, 'home.html', {'reviews': reviews})   
