from .views import BookView, BookCreate
from django.urls import path, include

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', BookView, basename='books')

urlpatterns = [
    path('db', BookCreate.as_view())
]

urlpatterns += router.urls
