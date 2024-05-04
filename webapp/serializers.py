from rest_framework import serializers
from .models import employees

# creating the serializer for the model "employees"
class employeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = employees
        fields = '__all__'