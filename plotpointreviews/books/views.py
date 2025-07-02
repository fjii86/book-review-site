from django.shortcuts import render
from .models import Book

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Send the user to login after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})