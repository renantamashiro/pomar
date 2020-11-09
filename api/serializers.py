from rest_framework import serializers

from api.models import Specie, Tree, TreeGroup, Harvest


class SpecieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specie
        fields = ['id', 'description']


class TreeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = ['id', 'description', 'age', 'specie']


class TreeGroupModelSeralizer(serializers.ModelSerializer):
    class Meta:
        model = TreeGroup
        fields = ['id', 'name', 'description', 'trees']


class HarvestModelSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Harvest
        fields = ['id', 'info', 'harvest_date', 'gross_weight', 'tree', 'tree_group']