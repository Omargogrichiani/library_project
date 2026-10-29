from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def books(request):
    book_list = [
        {'title': 'Harry Potter', 'pages': 350},
        {'title': 'The Hobbit', 'pages': 280},
        {'title': 'Atomic Habits', 'pages': 320},
        {'title': '1984', 'pages': 250},
    ]

    return render(request, 'books.html', {'books': book_list})