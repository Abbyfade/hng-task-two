from rest_framework import serializers
from myapi.models import Operation

class MyApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = "__all__"
