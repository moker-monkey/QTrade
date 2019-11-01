from rest_framework import serializers
from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('url', 'id', 'name', 'username', 'email', 'is_staff','birthday', 'mobile', 'gender', 'email', 'cash', 'stock')
