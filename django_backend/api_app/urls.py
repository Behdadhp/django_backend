from django.urls import path
from api_app import views
from .views import VacationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('vacation', VacationViewSet,basename='vacation')

app_name = 'vacation'

urlpatterns=[
    path('',views.VacationCreate.as_view(), name='create'),
    path('vacation_list',views.VacationList.as_view(),name='list'),
    path('viewset/',include(router.urls)),
]