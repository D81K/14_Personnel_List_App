from django.shortcuts import render
from .models import Personnel, Department
from .serializers import PersonnelSerializer, DepartmentSerializer, DepartmentPersonnelSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class PersonnelListCreateView(ListCreateAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        # authentication
        self.perform_create(serializer)
        return Response(status=status.HTTP_201_CREATED)
    
    def perform_create(self, serializer):
        serializer.save()



class DepartmentListView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentPersonnelView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentPersonnelSerializer
    
    def get_queryset(self):
        name = self.kwargs["department"]
        return Department.objects.filter(name__iexact=name)


class PersonnelGetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
        queryset = Personnel.objects.all()
        serializer_class = PersonnelSerializer

        def put(self, request, *args, **kwargs):
            # authentication
            return self.update(request, *args, **kwargs)
        
        def destroy(self, request, *args, **kwargs):
             instance = self.get_object()
             self.perform_destroy(instance)
        
        def perform_destroy(self, instance):
             instance.delete()
