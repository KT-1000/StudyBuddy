from django.db import models


class Card(models.Model):
    """ User-created flashcards. """
    name = models.CharField(max_length=100, primary_key=True)
    question = models.CharField(max_length=2000)
    answer = models.CharField(max_length=2000)
    creation_date = models.DateTimeField(null=True, blank=True)
    topic_id = models.ForeignKey()

    def __str__(self):
        return self.name


class Deck(models.Model):
    """ A deck is a collection """
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    """ Allows user to change status of a card or deck to 'Starred' or 'Reviewed' from the default state 'Created'. """
    NAMES = (
        ('Created', 'Created'),
        ('Reviewed', 'Reviewed'),
        ('Starred', 'Starred'),
    )
    name = models.CharField(choices=NAMES)
    card_name = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
