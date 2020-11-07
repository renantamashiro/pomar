from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import mixins
from rest_framework import generics

from api.models import (
    Specie,
    TreeGroup,
    Tree,
    Harvest
)

from api.serializers import (
    SpecieModelSerializer,
    TreeModelSerializer,
    TreeGroupModelSeralizer,
    HarvestModelSeralizer
)


class SpecieList(generics.ListCreateAPIView):
    queryset = Specie.objects.all()
    serializer_class = SpecieModelSerializer


class SpecieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Specie.objects.all()
    serializer_class = SpecieModelSerializer


class TreeList(generics.ListCreateAPIView):
    queryset = Tree.objects.all()
    serializer_class = TreeModelSerializer


class TreeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tree.objects.all()
    serializer_class = TreeModelSerializer


class TreeGroupList(generics.ListCreateAPIView):
    queryset = TreeGroup.objects.all()
    serializer_class = TreeGroupModelSeralizer


class TreeGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TreeGroup.objects.all()
    serializer_class = TreeGroupModelSeralizer


class HarvestList(generics.ListCreateAPIView):
    queryset = Harvest.objects.all()
    serializer_class = HarvestModelSeralizer


class HarvestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Harvest.objects.all()
    serializer_class = HarvestModelSeralizer

