from django.urls import path
from api_app import views


app_name = 'vacation'

urlpatterns=[
    path('',views.VacationCreate.as_view(), name='create')
]