from django.shortcuts import render
from .models import Message


def home(request):
    messages = Message.objects.all().order_by('-date_posted')
    return render(request, 'home.html', {'messages': messages})
