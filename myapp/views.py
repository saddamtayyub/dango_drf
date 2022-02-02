from django.shortcuts import render
from django.http import HttpResponse, request
from django.shortcuts import get_list_or_404
   #APIView
from rest_framework.views import APIView
  # mixin view
 # https://www.django-rest-framework.org/tutorial/3-class-based-views/#using-mixins
from rest_framework import mixins
from rest_framework import generics
#from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import employee
from .serializers import employeeSerializer
#from rest_framework.parsers import JSONParser
#import io

# API authentication 
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
# social login

# from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
# from dj_rest_auth.registration.views import SocialLoginView
# from allauth.socialaccount.providers.oauth2.client import OAuth2Client
# from django.conf import settings

# Create your views here.

   #apiView
class class_Base_API(APIView):
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            try:
                stu=employee.objects.get(id=id)
                serilizer=employeeSerializer(stu)
                return Response(serilizer.data)
            except:
                res={'msg':'data not found'}
                return Response(res,status.HTTP_404_NOT_FOUND)    
        emp1=employee.objects.all()
        serilizer=employeeSerializer(emp1,many=True)
        return Response(serilizer.data)  
        

        
        #add data
    def post(self,request,format=None):
        sr=employeeSerializer(data=request.data)
        if sr.is_valid():
            sr.save()
            return Response({'msg':'data created'}, status=status.HTTP_201_CREATED)
        return Response(sr.errors,status=status.HTTP_400_BAD_REQUEST)

     #updete data by put
    def put(self,request,pk=None,format=None):
        id=pk
        stu=employee.objects.get(id=id)
        sr=employeeSerializer(stu,data=request.data)
        if sr.is_valid():
            sr.save()
            return Response({'msg':'data created'}, status=status.HTTP_201_CREATED)
        return Response(sr.errors,status=status.HTTP_400_BAD_REQUEST)

     # patch update data 
    def patch(self,request,pk=None,format=None):
        id=pk
        stu=employee.objects.get(id=id)
        sr=employeeSerializer(stu,data=request.data,partial=True)
        if sr.is_valid():
            sr.save()
            return Response({'msg':'data created partial'}, status=status.HTTP_201_CREATED)
        return Response(sr.errors,status=status.HTTP_400_BAD_REQUEST)



     # delete data
    def delete(self,request,pk=None,format=None):
        #id=pk
        try:
            stu=employee.objects.get(id=id)
            stu.delete()
            return Response({'msg':'data deleted'}, status=status.HTTP_201_CREATED)
        except:
            res={'msg':'data not deleted becouse this id not in database'}
            return Response(res,status.HTTP_404_NOT_FOUND)












# function based API 
           
@api_view(['GET','POST','DELETE','PUT','PATCH'])   
def function_Base_API(request,pk=None):
    # authentication_classes=[JWTAuthentication]
    # permission_classes=[IsAuthenticated]
    id=pk
    if request.method=='GET':
        if id is not None:
            try:
                stu=employee.objects.get(id=id)
                serilizer=employeeSerializer(stu)
                                      
            except:
                res={'msg':'data not found'}
                return Response(res,status.HTTP_400_BAD_REQUEST)
            return Response(serilizer.data) 
        emp1=employee.objects.all()
         
        print("=======================================",emp1)

        serilizer=employeeSerializer(emp1,many=True)
        print("after sr",serilizer.data)
        return Response(serilizer.data)  



   # create data
    if request.method=='POST':
        data=request.data
        data['name']='bluthink'
        print(data,"===befor sr===================")
        serializer=employeeSerializer(data=data)
        print("after sr",serializer)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data created'}
            return Response(res,status=status.HTTP_201_CREATED)
        res={'msg':'data not created'}
        return Response(res,status=status.HTTP_400_BAD_REQUEST)   
        # delete data 
    if request.method=='DELETE':
        #id=pk
        try:
            stu=employee.objects.get(id=id)
            stu.delete()
            return Response({'msg':'data deleted'}, status=status.HTTP_201_CREATED)   
        except:
            res={'msg':'data not in database'}
            return Response(res,stutus=status.HTTP_400_BAD_REQUEST)   
     # data update           
    if request.method=='PUT':
        #id=pk
        stu=employee.objects.get(id=id)
        sr=employeeSerializer(stu,data=request.data)
        if sr.is_valid():
            sr.save()
            return Response({'msg':'data created'}, status=status.HTTP_201_CREATED)
        return Response(sr.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=='PATCH':
        #id=pk
        stu=employee.objects.get(id=id)
        sr=employeeSerializer(stu,data=request.data,partial=True)
        if sr.is_valid():
            sr.save()
            return Response({'msg':'data created partial'}, status=status.HTTP_201_CREATED)
        return Response(sr.errors,status=status.HTTP_400_BAD_REQUEST)



#mixin view
class ListEmployeeMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    # def post(self,request):
    #     serializer = employeeSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response({'massage':'data not valid'})
 
    


class DetailEmployeeMixins(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset=employee.objects.all()
    serializer_class=employeeSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
 
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    
    def patch(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    # def post(self,request,*args,**kwargs):
    #     return self.create(self,request,*args,**kwargs) 

    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)



# generic base

class empList(generics.ListCreateAPIView):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer


class empDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer




 # its 3 way to save data
# In [8]: emp_data = {"name": "Sid1", "lastname": "maulana", "email":"ml@gmail.com"}
# In [9]: emp = employee.objects.create(**emp_data)



# open shell command
# python manage.py shell

# leran about    aggregate(max,min,sum,avg,count),anotate()