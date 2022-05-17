from django.shortcuts import render
from .models import Vacation
from django.views import generic
from .forms import VacationForm

# Create your views here.

class VacationCreate(generic.CreateView):
    context_object_name = 'django_backend\api_app\templates\vacation\Vacation_form.html'
    model = Vacation
    form_class = VacationForm

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)   


class VacationList(generic.ListView):

    context_object_name = 'vacation_lists'
    queryset = Vacation.objects.all().order_by('-start_date')