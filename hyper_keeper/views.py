from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .serializer import HomeAppliancesSerializer, HomeAppliancesDetailSerializer, HomeAppliancesPostSerializer,\
    EdiblesSerializer, EdiblesDetailSerializer, EdiblesPostSerializer,\
    ClothesSerializer, ClothesDetailSerializer, ClotheDetailSerializerForPost
from .models import HomeAppliances, HomeAppliancesModel, Edibles, EdiblesModel, Clothes, ClothesModel

class HomeAppliancesList(APIView):

    def get(self, request):
        categories = HomeAppliances.objects.all()
        serializer = HomeAppliancesSerializer(categories, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = HomeAppliancesPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HomeAppliancesDetail(APIView):

    def get(self, request, pk):
        try:
            category = HomeAppliancesModel.objects.get(pk=pk)
        except HomeAppliancesModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = HomeAppliancesDetailSerializer(category, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class EdiblesList(APIView):

   def get(self, request):
        categories = Edibles.objects.all()
        serializer = EdiblesSerializer(categories, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

   def post(self, request):
        serializer = EdiblesPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EdiblesDetail(APIView):

    def get(self, request, pk):
        try:
            category = EdiblesModel.objects.get(pk=pk)
        except EdiblesModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EdiblesDetailSerializer(category, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class ClothesList(APIView):

    def get(self, request):
        categories = Clothes.objects.all()
        serializer = ClothesSerializer(categories, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

# class ClothesDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Clothes
#     serializer_class = ClotheDetailSerializerForPost

class ClothesDetail(APIView):

    def get(self, request, pk):
        try:
            category = ClothesModel.objects.get(pk=pk)
        except ClothesModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ClothesDetailSerializer(category, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            category = ClothesModel.objects.get(pk=pk)
        except ClothesModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ClotheDetailSerializerForPost(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            category = ClothesModel.objects.get(pk=pk)
        except ClothesModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response({'detail':'category has deleted seccessfully.'}, status=status.HTTP_204_NO_CONTENT)
