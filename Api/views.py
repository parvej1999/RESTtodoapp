from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import taskSerializer
from rest_framework import status
from .models import task

# Create your views here.


@api_view(['GET', 'POST'])
def taskCreate(request):
    if request.method == "GET":
        tasks = task.objects.all().order_by('-scheduled_date').order_by('-scheduled_time')[:1]
        serialize = taskSerializer(tasks, many = True)
        return Response(serialize.data)
    elif request.method == "POST":
        serialize = taskSerializer(data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status = status.HTTP_201_CREATED)
    return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def taskIndex(request):
    tasks = task.objects.all().order_by('-scheduled_date').order_by('-scheduled_time')
    serialize = taskSerializer(tasks, many = True)
    return Response(serialize.data)

@api_view(['GET'])
def taskDetail(request,pk):
    Task = get_object_or_404(task, id = pk)
    serialize = taskSerializer(Task, many = False)
    return Response(serialize.data)


@api_view(['GET', 'PUT'])
def taskUpdate(request, pk):
    if request.method == "GET":
        Task = get_object_or_404(task, id = pk)
        serialize = taskSerializer(Task, many = False)
        return Response(serialize.data)
    elif request.method == "PUT":
        Task = get_object_or_404(task, id = pk)
        serialize = taskSerializer(Task, data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
    return Response(status = status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'DELETE'])
def taskDelete(request, pk):
    if request.method == "GET":
        Task = get_object_or_404(task, id = pk)
        serialize = taskSerializer(Task, many = False)
        return Response(serialize.data)
    elif request.method == "DELETE":
        Task = get_object_or_404(task, id = pk)
        Task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)