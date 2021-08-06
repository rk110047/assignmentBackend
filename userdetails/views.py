from django.shortcuts import render
from .models import UserDetails
from .serializers import UserDetailSerializer
from rest_framework import generics
from rest_framework.response import Response


# Create your views here.



class UserDetailsListAPIView(generics.ListAPIView):
    queryset                =       UserDetails.objects.all()
    serializer_class        =       UserDetailSerializer



class UserDetailsCreateAPIView(generics.CreateAPIView):
    serializer_class        =       UserDetailSerializer
    queryset                =       UserDetails.objects.all()


    def post(self,request,*args,**kwargs):
        phone_number  = self.request.POST["phone_number"]
        if len(phone_number)<10 or phone_number.isnumeric()==False:
            return Response({"message":"invalid phone number"},status=400)
        self.create(request,*args,**kwargs)
        return Response({"message":"created","status":201},status=201)