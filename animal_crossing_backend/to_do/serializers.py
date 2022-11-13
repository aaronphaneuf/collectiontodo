from rest_framework import serializers
from .models import User, Collection

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection 
        fields = '__all__'

class UserCollectionSerializer(serializers.ModelSerializer):
    collections = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User 
        fields = ['collections']

    def get_collections(self, obj):
        x = obj.collections
        return CollectionSerializer(x, many=True).data
