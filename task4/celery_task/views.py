from django.shortcuts import render
from django.http import HttpResponse
from . import tasks


def celery(request):
    task = tasks.test.delay()
    return HttpResponse('task id: {0}'.format(task.task_id))