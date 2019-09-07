from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # odnośnik do innego modelu
    title = models.CharField(max_length=200) # tak definiujemy tekst z ograniczoną liczbą znaków
    text = models.TextField() # do dłuższych tekstów bez ograniczeń w ilości znaków
    created_date = models.DateTimeField( # data i godzina
            default=timezone.now)
    published_date = models.DateTimeField( # data i godzina
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
