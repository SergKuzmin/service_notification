from celery import shared_task


@shared_task
def adding_task(x, y):
    return x + y


@shared_task
def send_message_task(message: str):
    print(message)
