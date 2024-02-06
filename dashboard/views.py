from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dashboard(request):
    students = [
        {"name": "John", "age": 24, "address": "Bhopal"},
        {"name": "Alice", "age": 18, "address": "New York"},
        {"name": "Bob", "age": 25, "address": "London"},
        {"name": "Charlie", "age": 23, "address": "Paris"},
        {"name": "Eve", "age": 17, "address": "Tokyo"},
    ]
    return render(request, 'dashboard/index.html', context={'students': students})

def success_page(request):
    print("*" * 10)
    return HttpResponse('This is success page')

def navbar(request):
    return render(request , 'component/navbar.html')

def sidebar(request):
    return render(request, 'component/sidebar.html')