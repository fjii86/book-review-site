from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseForbidden
from .models import Book, Review
from .forms import BookForm
from .forms import ReviewForm
from .forms import ReviewFormWithBook 

# Create your views here.

def book_list(request):
    query = request.GET.get('q')
    books = Book.objects.all()
    if query:
        books = books.filter(title__icontains=query) | books.filter(author__icontains=query)

    paginator = Paginator(books, 9)  # 9 böcker per sida
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'books/book_list.html', {
        'page_obj': page_obj,
        'books': page_obj.object_list,
        'query': query,
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account was created. You can now log in!')
            return redirect('login')  # Send the user to login after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = Review.objects.filter(book=book).order_by('-created_at')
    user_review = None

    if request.user.is_authenticated:
        user_review = Review.objects.filter(book=book, user=request.user).first()

        if request.method == 'POST' and not user_review:
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
        'user_review': user_review
    })

@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewFormWithBook(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, 'Your review has been submitted!')
            return redirect('book_detail', pk=review.book.pk)
    else:
        form = ReviewFormWithBook()

    return render(request, 'books/add_review.html', {'form': form})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            if Book.objects.filter(title__iexact=title, author__iexact=author).exists():
                messages.error(request, 'That book already exists.')
            else:
                book = form.save()
                messages.success(request, 'Book added successfully!')
                return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})

@login_required
def edit_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if review.user != request.user:
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review was updated!')
            return redirect('book_detail', pk=review.book.pk)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'books/edit_review.html', {'form': form, 'review': review})

@login_required
def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if review.user != request.user:
        return HttpResponseForbidden()

    if request.method == 'POST':
        book_pk = review.book.pk
        review.delete()
        messages.success(request, 'Your review was deleted.')
        return redirect('book_detail', pk=book_pk)

    return render(request, 'books/delete_review.html', {'review': review})