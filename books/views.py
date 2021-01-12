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

def book_details(request, book_id):
    context = {
        "book": Book.objects.get(id=book_id),
    }
    return render(request, "book_details.html", context)

# class IndexView(TemplateView):
    # template_name = "index.html"

from django.contrib.auth.forms import UserCreationForm

def user_signup(request):
    form = None
    if request.method == "POST":
        # stwórz użytkownika
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # formularz poprawny, można zapisać użytkownika
            form.save()
            # przekierowanie na stronę z podziękowaniem
            return render(request, "registration/signup_complete.html")
    else:
        # pokaż pusty formularze rejestracji
        form = UserCreationForm()

    context = {"form": form}
    return render(request, "registration/signup_form.html", context)