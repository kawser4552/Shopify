

from django.urls import path,include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

router = routers.DefaultRouter()
router.register(r'',views.UserViewSet)



urlpatterns = [
     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('login/', views.signin, name='signin'),
     path('logout/<int:id>/', views.signout, name='signout'),
     path('', include(router.urls))
  
]

