from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list_view, name='books'),
    path('book_ditail/<int:id>', views.book_detail_view, name='book_ditail'),
    path('about/', views.about, name='about'),
    path('about_me/', views.about_me, name='about_me'),
    path('about_pets', views.about_pets, name='about_pets'),
    path('system_time', views.system_time, name='system_time'),
]


