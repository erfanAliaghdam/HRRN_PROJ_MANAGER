from urllib import request
from rest_framework import serializers
from processManager.models import Process
from django.contrib.auth import get_user_model

class UserSerailizerReadOnly(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email',)
        read_only_fields = ('email',)

class ProcessSerializer(serializers.ModelSerializer):
    user = UserSerailizerReadOnly(read_only=True)
    class Meta:
        model = Process
        fields = ['user', 'process_time_sec', 'created_at', 'status', 'HRRN']
        read_only_fields = ['created_at', 'user', 'status', 'HRRN']


