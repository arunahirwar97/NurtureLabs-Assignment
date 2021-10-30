from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('advisor/', views.AdvisorViewSet.as_view()),

]