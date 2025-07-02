from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Book, Review
from .forms import ReviewForm

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    for book in books:
        book.average_rating = 4.3
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


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = Review.objects.filter(book=book).order_by('-created_at')

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.book = book
                review.user = request.user
                review.save()
                messages.success(request, 'Thank you for your review!')
                return redirect('book_detail', pk=book.pk)
        else:
            form = ReviewForm()
    else:
        form = None

    return render(request, 'books/book_detail.html', {
        'book': book,
        'reviews': reviews,
        'form': form,
    })

@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, 'Your review has been submitted!')
            return redirect('book_detail', pk=review.book.pk)
    else:
        form = ReviewForm()

    return render(request, 'books/add_review.html', {'form': form})