from django.urls import path
from .views import PersonnelListCreateView, DepartmentListView, DepartmentPersonnelView, PersonnelGetUpdateDeleteView


urlpatterns = [
    path('personnel/', PersonnelListCreateView.as_view()),
    path('', DepartmentListView.as_view()),
    path('department/<str:department>', DepartmentPersonnelView.as_view()),
    path('personnel/<int:pk>', PersonnelGetUpdateDeleteView.as_view()),
]