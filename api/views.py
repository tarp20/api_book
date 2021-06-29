from django.shortcuts import redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, filters, generics
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from .serializers import BookSerializer, BookCreateSerializer
from books.models import Book
from .utils import save_data


class BookView(mixins.ListModelMixin,
               mixins.RetrieveModelMixin,
               viewsets.GenericViewSet,
               ):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter]
    filter_fields = ['published_date']
    search_fields = ['authors']
    ordering_fields = ['published_date']


class BookCreate(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer

    def create(self, request, *args, **kwargs):
        title = request.data['title']
        save_data(title)
        return Response(status=HTTP_201_CREATED)
