
from django.shortcuts import render
from rest_framework import generics
from .models import Data
from .serializers import DataSerializer
from django.views.generic import ListView

# Create your views here.

class ListView(generics.ListAPIView):
   queryset = Data.objects.all()
   serializer_class = DataSerializer
class CreateView(generics.CreateAPIView):
   queryset = Data.objects.all()
   serializer_class = DataSerializer

def index(request):
   data = Data.objects.all()
   new = Data.objects.latest('information')
   newData = {'newData',new}
   context = {'data':data}
   return render(request, 'mainapp/index.html',context,newData)
