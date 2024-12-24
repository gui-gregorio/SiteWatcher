from django.shortcuts import render
from .serializers import UserSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import UserModel


@api_view(["POST"])
def register_user(request):
    serializer = UserSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def list_user(request):
    user = UserModel.objects.all()
    serializer = UserSerializers(user, many=True)
    return Response(serializer.data)
        
