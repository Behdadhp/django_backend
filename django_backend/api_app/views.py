from django.shortcuts import render
from .models import Vacation
from django.views import generic

# Create your views here.

class VacationCreate(generic.CreateView):
    model = Vacation
    form_class = CreateVacation

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)   
