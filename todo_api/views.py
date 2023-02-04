from webbrowser import get
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import generics, views
from rest_framework.decorators import api_view

from todo.utils import get_object_or_none

from .models import ToDoList
from .serializers import ToDoListSerializer

# Create your views here.
@api_view(['GET','POST'])
def index(request,**kwargs):
    return Response([])

@api_view(['GET'])
def get_todo_list(request,**kwargs):
    todo_list = ToDoList.objects.all().order_by('-id')
    if request.GET.get('category') == 'all':
        todo_list = todo_list
    if request.GET.get('category') == 'active':
        todo_list = todo_list.filter(is_completed = False)
    if request.GET.get('category') == 'completed':
        todo_list = todo_list.filter(is_completed = True)
        
    response = ToDoListSerializer(todo_list,many=True)
    return Response(response.data)

@api_view(['POST'])
def manage_todo_list(request,**kwargs):
    todo = get_object_or_none(ToDoList,id=kwargs.get('pk'))
    print(request.POST,'POST')
    serializer = ToDoListSerializer(data=request.POST,instance=todo)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['POST'])
def change_status(request,**kwargs):
    todo = get_object_or_404(ToDoList,id=kwargs.get('pk'))
    todo.is_completed = request.POST.get('is_completed')
    todo.save()
    return Response(ToDoListSerializer(todo,many=False).data,status=200)

class CreateToDoList(generics.CreateAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer
    
class StatusChangeView(views.APIView):
    
    def post(self,request,*args,**kwargs):
        todo = get_object_or_404(ToDoList,id=kwargs.get('pk'))
        todo.is_completed = request.data.get('is_completed')
        todo.save()
        return Response(ToDoListSerializer(todo,many=False).data,status=200)