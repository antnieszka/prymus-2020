"""libraryproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from books.views import books_list, book_details, index, user_signup
from django.urls import include

urlpatterns = [
    # http://127.0.0.1:8000/
    path('', index, name="index"),
    path('uzytkownicy/', include("django.contrib.auth.urls")),
    path('uzytkownicy/rejestracja/', user_signup),
    path('admin/', admin.site.urls),
    # path('hello-world/', ...),
    # http://127.0.0.1:8000/books
    path('ksiazki/', books_list, name="book_list"),
    # path('authors/', ...),
    path('ksiazki/<int:book_id>', book_details, name="book_details"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
