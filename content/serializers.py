from rest_framework import serializers

from .models import Gallery, Testimonial


class GallerySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = ['id', 'image', 'caption', 'uploaded_at']

    def get_image(self, obj):
        """Return the full Cloudinary URL for the image."""
        if obj.image:
            return obj.image.url
        return None


class TestimonialSerializer(serializers.ModelSerializer):
    """Read-only serializer — does NOT expose the approved field."""

    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'text', 'submitted_at']


class TestimonialCreateSerializer(serializers.ModelSerializer):
    """Write-only serializer for public submissions.

    Only accepts name and text. The approved field is always
    forced to False regardless of what the client sends.
    """

    class Meta:
        model = Testimonial
        fields = ['name', 'text']
