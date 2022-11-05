from django.shortcuts import render
from rest_framework import generics
from myapi.models import Operation
from myapi.serializers import MyApiSerializer
from rest_framework.response import  Response



class Arithmetic(generics.ListCreateAPIView):
    queryset = Operation.objects.all()
    serializer_class = MyApiSerializer

    def post(self, request, *args, **kwargs):
        header = {"Access-Control-Allow-Origin":"*"}
        serializer = MyApiSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.save()
            x = question.x
            y = question.y
            sign = question.operation_type.lower()
        
            if "add" in sign or "addition" in sign:
                result = x+y
                return Response({'slackUsername': 'Abby_fade', 'result': result, 'operation_type': "addition"}, headers=header)
            elif "subtract" in sign or "subtraction" in sign:
                result = x-y
                return Response({'slackUsername': 'Abby_fade', 'result': result, 'operation_type': "subtraction"}, headers=header)
            elif "multiply" in sign or "multiplication" in sign:
                result = x*y
                return Response({'slackUsername': 'Abby_fade', 'result': result, 'operation_type': "multiplication"}, headers=header)


            
