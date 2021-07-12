from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    return HttpResponse('OK')


def send_messages(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            print(request.POST.get('message_text'))
        return HttpResponse("Send task to worker")
    else:
        return redirect('/')
