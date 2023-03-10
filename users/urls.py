from django.urls import include, path
from .views import RegisterView


urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/register/', RegisterView.as_view(), name='register'),
]