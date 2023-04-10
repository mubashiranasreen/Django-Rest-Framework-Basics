from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['Get'])
def api_overview(request):
    api_urls = {
        'List': '/product-list',
        'Detail ': '/product-detail/<int:id>',
        'Create': '/product-create/<int:id>',
        'Update': '/product-update/<int:id>',
        'Delete': '/product-delete/<int:id>',

    }
    return Response(api_urls)


@api_view(['Get'])
def showall(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['Post'])
def createproduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['Get'])
def viewproduct(request, pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)


@api_view(['Post'])
def updateproduct(request, pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=products, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['Delete'])
def deleteproduct(request, pk):
    products = Product.objects.get(id=pk)
    products.delete()
    return Response("Product Deleted Successfully")





