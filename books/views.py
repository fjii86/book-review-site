from django.shortcuts import render
from .models import Book, Review

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

    return render(request, 'books/book_detail.html', {
        'book': book,
        'reviews': reviews,
    })