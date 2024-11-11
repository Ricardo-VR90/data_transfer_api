from rest_framework import serializers
from .models import Employee, Department, Job

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class DepartmenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'