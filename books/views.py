from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# http://127.0.0.1:8000/books
from books.models import Book


def index(request):
    print(request.user)
    return render(request, "index.html")

def books_list(request):
    context = {"books": Book.objects.all()}
    return render(request, "book_list.html", context)


# class IndexView(TemplateView):
    # template_name = "index.html"