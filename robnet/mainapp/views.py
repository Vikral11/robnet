from django.shortcuts import render
from . import serializers
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


@api_view(["POST"])
def form1(request, *args, **kwargs):
    data = request.data
    if not (data.get("name") and data.get("phone") and data.get("message")):
        return Response({"error" : "name or phone or message or some of them not provides."}, status=status.HTTP_400_BAD_REQUEST)
    serial = serializers.FormOneSerializer(data=data)
    if serial.is_valid():
        serial.save()
        return Response({"response":"Data saved Sussfully"}, status=status.HTTP_200_OK)
    return Response({"error": serial.errors}, status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST"])
def form_two(request, *args, **kwargs):
    data = request.data
    serial = serializers.FormTwoSerializer(data=data)
    if serial.is_valid():
        serial.save()
        return Response({"response":"Data saved Sussfully"}, status=status.HTTP_200_OK)
    print(serial.errors)
    return Response({"error": serial.errors}, status=status.HTTP_400_BAD_REQUEST)

