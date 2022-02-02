from rest_framework import serializers

#from rest_framework import employee
from .models import employee  #,User

# Serializers define the API representation.

       
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
#         # fields = ("first_name", "last_name", "email", "phone_number","dob","gender","password")




class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        #fields = ['name', 'lastname', 'email','emid']

        fields= '__all__'