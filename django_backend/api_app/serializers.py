from .models import Vacation, Branch, Employee
from rest_framework import serializers


class VacationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Vacation
        fields = '__all__'

