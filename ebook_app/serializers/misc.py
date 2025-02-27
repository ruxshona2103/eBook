from rest_framework import serializers
from ebook_app.models import Category, Book, Review , BookViewHistory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    avg_rating = serializers.FloatField(read_only=True, required=False)

    class Meta:
        model = Book
        fields = ['id', 'name', 'description', 'category', 'avg_rating', 'price', 'stock']


class BookViewHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = BookViewHistory
        fields = '__all__'


