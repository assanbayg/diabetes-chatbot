from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import InsulinTake, InsulinType
from .serializers import InsulinTakeSerializer, InsulinTypeSerializer


@api_view(["GET"])
def insulin_type(request):
    types = InsulinType.objects.all()
    serializer = InsulinTypeSerializer(types, many=True)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def insulin_take(request):
    if request.method == "GET":
        takes = InsulinTake.objects.all()
        seializer = InsulinTakeSerializer(takes, many=True)
        return Response(seializer.data)

    elif request.method == "POST":
        serializer = InsulinTakeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def insulin_take_detail(request, pk):
    take = get_object_or_404(InsulinTake, pk=pk)

    if request.method == "GET":
        serializer = InsulinTakeSerializer(take)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = InsulinTakeSerializer(take, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        take.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
