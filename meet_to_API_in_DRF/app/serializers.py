from rest_framework import serializers
from .models import Car

# # ручной сериализатор
# class CarSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()


# сериализатор
class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car

        # выведем сразу все имеющиеся поля
        fields = "__all__"
