from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'urec_app/home.html')


def accident(request):
    return render(request, 'urec_app/accident.html')


def count(request):
    return render(request, 'urec_app/count.html')


def erp(request):
    return render(request, 'urec_app/erp.html')


def form(request):
    return render(request, 'urec_app/form.html')


def incident(request):
    return render(request, 'urec_app/incident.html')


def sop(request):
    return render(request, 'urec_app/sop.html')


def task(request):
    return render(request, 'urec_app/task.html')


def survey(request):
    return render(request, 'urec_app/survey.html')
