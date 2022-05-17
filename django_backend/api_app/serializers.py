from .models import Vacation, Branch, Employee
from rest_framework import serializers


class VacationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Vacation
        fields = '__all__'

class BranchSerializer(serializers.ModelSerializer):

    class Meta:

        model = Branch
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Branch
        fields = '__all__'

