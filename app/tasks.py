# This is the file where the task functions are stored

from celery import shared_task # This imports the task decorator

from time import sleep


@shared_task
def sleepy(duration): # Background Function 
    sleep(duration)
    return None