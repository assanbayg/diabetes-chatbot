from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BloodLevelEntry
from .serializers import BloodLevelEntrySerializer


@api_view(["GET", "POST"])
def blood_level_list(request):
    # List all blood levels entries in db
    if request.method == "GET":
        entries = BloodLevelEntry.objects.all()
        serializer = BloodLevelEntrySerializer(entries, many=True)
        return Response(serializer.data)

    # Create a new blood level entry
    elif request.method == "POST":
        serializer = BloodLevelEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def blood_level_detail(request, pk):
    # Retrieve, update, or delete a blood level entry

    blood_level = get_object_or_404(BloodLevelEntry, pk=pk)

    if request.method == "GET":
        serializer = BloodLevelEntrySerializer(blood_level)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = BloodLevelEntrySerializer(blood_level, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    elif request.method == "DELETE":
        blood_level.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
