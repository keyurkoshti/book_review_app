from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from django.shortcuts import render, redirect


# --------------------Register API------------------------
class RegisterApiview(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'user created successfully'},
                status = status.HTTP_201_CREATED 
            )
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

def register_page(request):
    return render(request, "register.html")