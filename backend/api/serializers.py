from django.contrib.auth.models import User
from .models import CustomerSettings, Customer, Category, Obstacle, Habbit, OvercomePlan
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class CustomerSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerSettings
        fields = ('privacy_level', )


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    settings = CustomerSettingsSerializer()

    class Meta:
        model = Customer
        fields = ('user', 'settings', )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'name', 'color', 'icon_name')


class ObstacleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obstacle
        fields = ('pk', 'name', )


class HabbitSerrializer(serializers.ModelSerializer):
    category = CategorySerializer()
    obstacles = ObstacleSerializer(many=True)

    class Meta:
        model = Habbit
        fields = ('pk', 'title', 'wish', 'outcome', 'category', 'obstacles', )
