from rest_framework import serializers
from .models import Personnel, Department
from django.utils.timezone import now


class PersonnelSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()
    
    class Meta:
        model = Personnel
        fields = "__all__"
    
    def get_days_since_joined(self, obj):
        return (now() - obj.start_date).days
    
    # def get_fields() -> look at project 11_Django_Car_App and ask Gerard about serializers and views


class DepartmentSerializer(serializers.ModelSerializer):
    personnel_count = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = "__all__"
    
    def get_personnel_count(self, obj):
        return Personnel.objects.filter(department = obj.id).count()


class DepartmentPersonnelSerializer(serializers.ModelSerializer):
    personnel_count = serializers.SerializerMethodField()
    departments = PersonnelSerializer(read_only=True, many=True)

    class Meta:
        model = Department
        fields = ('id', 'name', 'personnel_count', 'departments')
    
    def get_personnel_count(self, obj):
        return Personnel.objects.filter(department = obj.id).count()