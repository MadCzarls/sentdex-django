from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return HttpResponse('Wow this is and <strong>awesome</strong> tutorial')
