from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200, unique=True)
    # last_name = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True, max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Full name: {self.first_name} {self.last_name}'

