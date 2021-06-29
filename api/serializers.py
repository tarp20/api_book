from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'authors', 'published_date', 'categories',
                  'average_rating', 'ratings_count', 'thumbnail')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        try:
            ret['authors'] = ret['authors'].split(',')
        except AttributeError:
            ret['authors'] = None
        try:
            ret['categories'] = ret['categories'].split(',$')
        except AttributeError:
            ret['categories'] = None

        return ret


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title',)
