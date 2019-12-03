"""Database model for rental_app"""

from django.db import models


class Friend(models.Model):
    """A friend who borrows something"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.name)


class Belonging(models.Model):
    """Thing that is being borrowed"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.name)


class Borrowed(models.Model):
    """What is being borrowed, to who, when and when returned"""
    what = models.ForeignKey(Belonging, on_delete=models.CASCADE)
    to_who = models.ForeignKey(Friend, on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now=True)
    returned = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{} to {}, {}".format(self.what, self.to_who, self.when.strftime("%d.%m.%Y %H:%M:%S"))
