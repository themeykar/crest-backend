from django.db import models
from cloudinary.models import CloudinaryField


class Gallery(models.Model):
    """A photo in the boat gallery."""
    image = CloudinaryField('image')
    caption = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name_plural = 'galleries'

    def __str__(self):
        label = self.caption or 'Untitled'
        date = self.uploaded_at.strftime('%Y-%m-%d') if self.uploaded_at else 'unsaved'
        return f'{label} ({date})'


class Testimonial(models.Model):
    """A customer testimonial / review."""
    name = models.CharField(max_length=100)
    text = models.TextField()
    approved = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        date = self.submitted_at.strftime('%Y-%m-%d') if self.submitted_at else 'unsaved'
        return f'{self.name} ({date})'
