from re import L
from rest_framework import serializers
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

def getItemsList(request):
    items = Todo.objects.all()
    serializer = TodoSerializer(items,many=True)
    return Response(serializer.data)

def getItemDetail(request,pk):
    items = Todo.objects.get(id=pk)
    serializer = TodoSerializer(items,many=False)
    return Response(serializer.data)


def createItem(request):
    serializer=TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

def updateItem(request,id):
    data = request.data
    item = Todo.objects.get(id=id)
    serializer = TodoSerializer(instance=item,data=data)
    
    if serializer.is_valid():
        serializer.save()
        
    return serializer.data

def deleteItem(request,pk):
    item = Todo.objects.get(id=pk)
    item.delete()
    return Response('Item was deleted')

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
