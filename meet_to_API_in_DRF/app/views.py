from django.http import HttpResponse, JsonResponse
from .models import Car
import json
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from .serializers import CarModelSerializer  #  , CarSerializer


# DRF дает возможность получить из коробки полноценный CRUD сразу
# при этом будет использоваться роутинг (urls.py)
class CarApiViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarModelSerializer


# # еще больше упростим создание методов GET и POST, используя ListCreateAPIView
# class CarApiView(ListCreateAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarModelSerializer
#
# # также есть возможность из коробки получить еще 4 метода
# # (детализированный GET, PUT, PATCH, DELETE)
# # и тем самым получить CRUD
# class CarRApiView(RetrieveUpdateDestroyAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarModelSerializer

# # используем встроенные возможности DRF для создания API
# class CarApiView(APIView):
#     def get(self, request, *args, **kwargs):
#         cars = Car.objects.all()
#         serializer = CarSerializer(cars, many=True)
#
#         return JsonResponse(serializer.data, safe=False, status=HTTP_200_OK)
#
#     def post(self, request, *args, **kwargs):
#         serializer = CarSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         car = Car.objects.create(**serializer.validated_data)
#         context = CarSerializer(car)
#         return Response(context.data, status=HTTP_201_CREATED)


# # пишем API сами
# # применяем декоратор и передаем в него разрешенные нами для использования методы
# @api_view(http_method_names=['GET', 'POST'])
# def car_view(request):
#
#     # после применения декоратора @api_view , наша проверка уже не нужна
#     # if request.method not in ['GET', 'POST']:
#     #     return HttpResponse(status=405)
#
#     if request.method == 'GET':
#         cars = Car.objects.all()
#
#         # преобразуем QuerySet в понятный для json'а список словарей
#         # data = [{'id': car.id, 'name': car.name} for car in cars]
#
#         # будем использовать сериалайзер
#         serializer = CarSerializer(cars, many=True)
#
#         # return JsonResponse(data, safe=False, status=200)
#
#         # будем использовать сериалайзер
#         return JsonResponse(serializer.data, safe=False, status=HTTP_200_OK)
#
#     if request.method == 'POST':
#
#         # без сериализатора
#         data = json.loads(request.body)
#
#         # так мы получаем объект из json и загружаем его в БД
#         # car = Car.objects.create(name=data.get('name'))
#
#         # используем сериализатор
#         serializer = CarSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         # более краткий и простой способ написания
#         # car = Car.objects.create(**data)
#
#         # используем сериализатор
#         car = Car.objects.create(**serializer.validated_data)
#
#         # передаем информацию на frontend
#         # context = {'id': car.id, 'name': car.name}
#
#         # используем сериализатор, передаем информацию на frontend
#         context = CarSerializer(car)
#
#         # return JsonResponse(context.data, status=HTTP_201_CREATED)
#
#         # используем сериализатор
#         return JsonResponse(context.data, status=HTTP_201_CREATED)
