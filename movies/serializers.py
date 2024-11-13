from rest_framework import serializers

from movies.models import Category, Movie


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    categoria = serializers.SerializerMethodField()

    def get_categoria(self, obj):
        serializer = CategorySerializer(obj.category)
        return serializer.data

    class Meta:
        model = Movie
        fields = '__all__'
