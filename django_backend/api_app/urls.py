from django.urls import path, include
from api_app import views
from .views import VacationViewSet, BranchViewSet, EmployeeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('vacation', VacationViewSet,basename='vacation')
router.register('branch',BranchViewSet,basename='branch')
router.register('employee',EmployeeViewSet,basename='employee')

app_name = 'vacation'

urlpatterns=[
    path('',views.VacationCreate.as_view(), name='create'),
    path('vacation_list',views.VacationList.as_view(),name='list'),
    path('viewset/',include(router.urls)),
]