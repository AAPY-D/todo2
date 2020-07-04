from django.shortcuts import render
from .models import Todo
from django.utils import timezone
# Create your views here.

t = Todo(data='Django on the way', timeStamp=timezone.now(), author = 'admin1')
t.save()


def todo(request):
    data_for_frontend = {
    }
    return render(request, 'todo/todo.html', data_for_frontend)