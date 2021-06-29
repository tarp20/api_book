from django.db import models


class Book(models.Model):
    '''
    Book model
    '''

    title = models.CharField(
        max_length=249,
        null=True)
    authors = models.CharField(
        max_length=500,
        null=True)
    published_date = models.CharField(
        max_length=100,
        null=True)
    categories = models.CharField(
        max_length=500,
        null=True)
    average_rating = models.PositiveBigIntegerField(
        blank=True,
        null=True)
    ratings_count = models.PositiveBigIntegerField(
        null=True)
    thumbnail = models.CharField(
        max_length=300,
        null=True)

    def __str__(self):
        return self.title

    class Meta:
        '''
        prohibit books with same title, authors, published_date
        '''
        unique_together = ('title', 'authors', 'published_date')
