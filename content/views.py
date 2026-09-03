from rest_framework import generics

from .models import Gallery, Testimonial
from .serializers import (
    GallerySerializer,
    TestimonialCreateSerializer,
    TestimonialSerializer,
)


class GalleryListView(generics.ListAPIView):
    """GET /gallery/ — returns all gallery images (most recent first)."""
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class TestimonialListView(generics.ListAPIView):
    """GET /testimonials/ — returns the 3 most recent approved testimonials."""
    serializer_class = TestimonialSerializer

    def get_queryset(self):
        return Testimonial.objects.filter(approved=True)[:3]


class TestimonialCreateView(generics.CreateAPIView):
    """POST /testimonials/submit/ — public submission (always unapproved)."""
    serializer_class = TestimonialCreateSerializer
