from django.contrib import admin
from django.urls import path, include
from app import views
# from app.converter import DateConverter
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('car', views.CarApiViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/car/', csrf_exempt(views.car_view), name='car'),
    # path('api/v1/car/', views.CarApiView.as_view(), name='car'),
    path('api/v1/', include(router.urls)),
]
