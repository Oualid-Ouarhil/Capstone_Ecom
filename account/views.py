from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from .serializers import SignUpSerializer
from rest_framework.permissions import IsAuthenticated
import logging

# Create your views here.

@api_view(['POST'])
def register(request):
    data = request.data
    user = SignUpSerializer(data = data)

    if user.is_valid():
        if not User.objects.filter(username=data['email']).exists():
            user = User.objects.create(
                username = data['username'],
                email = data['email'],
                password = make_password(data['password']),
            )
            return Response(
                {'details':'Your account registration is a success!'},
                    status=status.HTTP_201_CREATED
                    )
        else:
            return Response(
                {'error':'This email already exists, try changing it!'},
                status=status.HTTP_400_BAD_REQUEST
            )
    else:
        return Response(user.errors)
    

logger = logging.getLogger(__name__)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def online_user(request):
    logger.info("Recieved request from user: %s", request.user)
    user = SignUpSerializer(request.user)
    return Response(user.data)