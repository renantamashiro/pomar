from rest_framework import serializers

from api.models import Specie, Tree, TreeGroup, Harvest


class SpecieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specie
        fields = ['id', 'description']


class TreeModelSerializer(serializers.ModelSerializer):
    specie = SpecieModelSerializer(read_only=True)
    
    class Meta:
        model = Tree
        fields = ['id', 'description', 'age', 'specie']


class TreeGroupModelSerializer(serializers.ModelSerializer):
    trees = TreeModelSerializer(read_only=True, many=True)

    class Meta:
        model = TreeGroup
        fields = ['id', 'name', 'description', 'trees']


class HarvestModelSeralizer(serializers.ModelSerializer):
    tree = TreeModelSerializer(read_only=True)
    tree_group = TreeGroupModelSerializer(read_only=True)

    class Meta:
        model = Harvest
        fields = ['id', 'info', 'harvest_date', 'gross_weight', 'tree', 'tree_group']