from django.db import models

class Message(models.Model):
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]
