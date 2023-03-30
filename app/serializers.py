from rest_framework import serializers
from app.models import ToDo

class ToDoSerializer (serializers.ModelSerializer):
    class Model:
        model = ToDo
        fields = ['id', 'actividade', 'status']