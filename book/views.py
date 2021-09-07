from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import Http404
from django.db.models import Avg

# Create your views here.
def index(request):
    books = Book.objects.all().order_by("rating") # ajratish= order_by masalan -title ketmaketligi
    num_books =  books.count()
    avg = books.aggregate(Avg("rating")) # ratingni aniqlash: rating__avg, rating__min
    return render(request,"index.html",{
        "books":books,
        "total_number_of_books":num_books,
        "average_rating":avg
    })


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except :
    #     raise Http404
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_detail.html",{
        "title": book.title ,
        "author" : book.author,
        "rating": book.rating ,
        "is_bestseller": book.is_bestselling,
    })