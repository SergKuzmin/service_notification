from django.http import HttpResponse
from django.shortcuts import redirect
from .tasks import send_message_task


def index(request):
    return HttpResponse('OK')


def send_messages(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            message = request.POST.get('message_text')
            send_message_task.delay(message)
        return redirect('/')
    else:
        return redirect('/')
