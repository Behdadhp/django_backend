from django.shortcuts import render
from .models import Vacation, Branch, Employee
from django.views import generic
from .forms import VacationForm
from django.urls import reverse_lazy

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .serializers import VacationSerializer, BranchSerializer, EmployeeSerializer

class VacationCreate(generic.CreateView):
    context_object_name = 'django_backend\api_app\templates\vacation\Vacation_form.html'
    model = Vacation
    form_class = VacationForm
    success_url = reverse_lazy("vacation:list")

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)   


class VacationList(generic.ListView):

    context_object_name = 'vacation_lists'
    queryset = Vacation.objects.all().order_by('-start_date')


class BaseAuthViewSet(viewsets.ModelViewSet):

    authentication_class = [TokenAuthentication ]
    permission_classes = [IsAuthenticated]


class VacationViewSet(BaseAuthViewSet):

    serializer_class = VacationSerializer
    queryset = Vacation.objects.all()

class BranchViewSet(BaseAuthViewSet):

    serializer_class = BranchSerializer
    queryset = Branch.objects.all()


class EmployeeViewSet(BaseAuthViewSet):

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()