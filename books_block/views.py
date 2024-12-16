from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models

def book_detail_view(request, id):
    if request.method == 'GET':
        book = get_object_or_404(models.BookModels, id=id)  # исправлено на 'book', так как мы работаем с книгами
        context = {
            'book_id': book,  # передаем книгу в шаблон
        }
        return render(request, 'show_detail.html', context)

def book_list_view(request):
    if request.method == "GET":

        book_list = models.BookModels.objects.all().order_by('-id')
        context = {
            'book_list': book_list,
        }
        return render(request, template_name='show.html', context=context)

def about(request):
    if request.method == 'GET':
        return HttpResponse('привет это мой первый проект на джанго')
def about_me(request):
    if request.method == 'GET':
        return HttpResponse("Тут я должен был написать что-то о себе. я Алихан и мне 17 полных лет")
def about_pets(request):
    if request.method == 'GET':
        return HttpResponse("у меня есть две собачки)))")
def system_time(request):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse(f"Текущее системное время: {current_time}")