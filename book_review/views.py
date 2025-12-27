from django.contrib import messages 
from django.shortcuts import render, redirect 
from .models import Book_Review_forms, book, Category
from .forms import user_form
from django.contrib.auth import authenticate, login, logout, get_user_model 
from django.contrib.auth.decorators import login_required 
# from rest_framework.views import APIView


User = get_user_model()


# ---------------- Register User ----------------
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

        user = User.objects.create_user(
            username=username, 
            email=email, 
            password=password1)
        user.save()
        messages.success(request, "Account created successfully. Please login.")
        return redirect('login')   

    return render(request, "register.html")


# ---------------- Login User ----------------
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session.set_expiry(900)
            return redirect('form_view') 
        else:
            messages.error(request, "Invalid credentials")
            return render(request, 'login.html')

    return render(request, 'login.html')  


# ---------------- Logout User ----------------
def logout_user(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login') 


# ---------------- Book Review Form ----------------
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


# ---------------- Home page ----------------
@login_required(login_url='login')
def home(request):
    reviews = Book_Review_forms.objects.all().order_by('-id')
    return render(request, 'home.html', {'reviews': reviews})   


# --------------------Book Info------------------------
@login_required(login_url='login')
def book_info(request):
    categories = Category.objects.all()
    if request.method == "POST":
        title = request.POST['title']
        category_id  = request.POST['category']
        author = request.POST['author']
        rating = request.POST['rating']
        comment = request.POST['comment']
        description = request.POST['description']

        category = Category.objects.get(id=category_id)

        book.objects.create(
            title=title,
            category=category,
            author=author,
            rating=rating,
            comment=comment,
            description=description
        )
        messages.success(request, "Book added successfully")
        return redirect('form_view')
    
    
    return render(request, 'book.html', {'categories': categories})