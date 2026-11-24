from django.db import models


class Presentation(models.Model):
    title = models.CharField(max_length=200, default="Untitled Presentation")
    lyrics = models.TextField()

    # Generated slide content
    slides = models.JSONField(default=list)

    # Presentation appearance
    font = models.CharField(max_length=50, default="Arial")
    font_size = models.PositiveIntegerField(default=36)
    background = models.CharField(max_length=30, default="black")
    text_color = models.CharField(max_length=30, default="white")

    # Timestamps
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
