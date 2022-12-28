from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from book.forms import BookCreate
from book.models import Book


def index(request):
    shelf = Book.objects.all()
    return render(request, 'book/library.html', {'shelf': shelf})


def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'book/upload_form.html', {'upload_form': upload})


def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_form = BookCreate(request.POST or None, instance=book_sel)
    if book_form.is_valid():
        book_form.save()
        return redirect('index')
    return render(request, 'book/upload_form.html', {'upload_form': book_form})


def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_sel.delete()
    return redirect('index')
