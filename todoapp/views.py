from django.shortcuts import render
import rest_framework
from rest_framework import request
from rest_framework import authentication
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo
from rest_framework import status
from rest_framework import response,serializers
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo
from rest_framework import status
from rest_framework import response,serializers
from django.shortcuts import get_object_or_404
# from .utils import getItemList,createItem,getItemDetail,updateItem,deleteItem
from rest_framework.authentication import TokenAuthentication
# Create your views here.

from .utils import updateItem,getItemDetail,deleteItem,getItemsList,createItem

@api_view(['GET'])
def getRoutes(request):
    
    routes = [
        {
            'Endpoint': '/items',
            'method': 'GET',
            'body':None,
            'description':'Returns an array of notes'
        },
        {
            'Endpoint': '/items/id',
            'method': 'GET',
            'body':None,
            'description':'Returns a single note object'
        },
        {
            'Endpoint': '/items/create',
            'method': 'POST',
            'body':{'body':""},
            'description':'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/items/id/update',
            'method': 'PUT',
            'body':None,
            'description':'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

# @api_view(['GET'])
# def getItems(request):
#     items=Todo.objects.all()
#     serializer=TodoSerializer(items,many=True)
#     return Response(serializer.data)

# @api_view(['GET'])

# def getItem(request,id):
#     items = Todo.objects.get(id=id)
#     serializer = TodoSerializer(items,many=False)
#     return Response(serializer.data)


# @api_view(['POST'])
# # def createItem(request):
# #     data = request.data
# #     item = Todo.objects.create(
# #         body=data['body']
# #     )
# #     serializer = TodoSerializer(item, many=False)
# #     return Response(serializer.data)

# def createItem(request):
#     serializer=TodoSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# #     data=request.data
# #     item= Todo.objects.create(
# #     body=data['body']
# #     )
# #     serializer = TodoSerializer(item,many=False)
# #     return Response(serializer.data)
    
# @api_view(['PUT'])
# def updateItem(request,id):
#     data = request.data
#     item = Todo.objects.get(id=id)
#     serializer = TodoSerializer(instance=item,data=data)
    
#     if serializer.is_valid():
#         serializer.save()
        
#     return Response(serializer.data)

# @api_view(['DELETE'])
# def deleteItem(request,id):
#     item = Todo.objects.get(id=id)
#     item.delete()
#     return Response('Item was deleted')


@api_view(['GET','POST'])
def getItems(request):
    
    if request.method=='GET':
        return getItemsList(request)
    
    if request.method=='POST':
        return createItem(request)
    
@api_view(['GET','PUT','DELETE'])
def getItem(request,pk):
    
    if request.method=='GET':
        return getItemDetail(request,pk)
    
    if request.method=='PUT':
        return updateItem(request,pk)
    
    if request.method=='DELETE':
        return deleteItem(request,pk)