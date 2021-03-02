from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse

from .forms import BookForm

# Create your views here.
from app3.models import Book
from app3.forms import BookForm


def home(request):
    return render(request, 'index.html')


def upload(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return home(request)
    return render(request, 'upload.html', {'form': form})


def book(request):
    k = Book.objects.all()
    return render(request, 'book.html', {'b': k})


def delete_book(request, pk):
    b = Book.objects.get(pk=pk)
    b.delete()
    return book(request)


def view_book(request, pk):
    b = Book.objects.get(pk=pk)
    return render(request, 'booklist.html', {'instance': b})


def edit_book(request, pk):
    b = Book.objects.get(pk=pk)
    form = BookForm(instance=b)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=b)
        if form.is_valid():
            form.save(commit=True)
            return book(request)
        else:
            print('ERROR FORM VALID')
    return render(request, 'upload_book.html', {'form': form})


def search(request):
    if request.method == "POST":
        srch = request.POST['search']
        if srch:
            match = Book.objects.filter(Q(author__icontains=srch) | Q(title__icontains=srch))
            if match:
                return render(request, 'search.html', {'sr': match})
            else:
                return search(request)
        else:
            return HttpResponse('no result')
    return render(request, 'search.html')


# def setsession(request):
#     request.session['name'] = 'Appu'
#     return HttpResponse('session')
#
#
# def getsession(request):
#     name = request.session['name']
#     return HttpResponse(name)
