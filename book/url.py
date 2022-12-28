from . import views
from django.urls import path


urlpatterns = [
      path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-books'),
    path('update/<int:book_id>', views.update_book),
    path('delete/<int:book_id>', views.delete_book)
]