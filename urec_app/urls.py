from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accident/', views.accident, name='accident'),
    path('count/', views.count, name='count'),
    path('erp/', views.erp, name='erp'),
    path('form/', views.form, name='form'),
    path('incident/', views.incident, name='incident'),
    path('sop/', views.sop, name='sop'),
    path('survey/', views.survey, name='survey'),
    path('task/', views.task, name='task'),

]
