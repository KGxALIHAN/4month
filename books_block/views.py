from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

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