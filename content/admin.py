from django.contrib import admin
from django.utils.html import format_html

from .models import Gallery, Testimonial


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('thumbnail_preview', 'caption', 'uploaded_at')
    list_display_links = ('caption',)
    readonly_fields = ('image_preview',)

    @admin.display(description='Preview')
    def thumbnail_preview(self, obj):
        if obj.image:
            url = obj.image.url
            return format_html(
                '<img src="{}" style="height:50px; border-radius:4px;" />',
                url,
            )
        return '-'

    @admin.display(description='Image')
    def image_preview(self, obj):
        if obj.image:
            url = obj.image.url
            return format_html(
                '<img src="{}" style="max-height:300px; border-radius:6px;" />',
                url,
            )
        return '-'


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'text_preview', 'approved', 'submitted_at')
    list_editable = ('approved',)
    list_filter = ('approved',)
    search_fields = ('name', 'text')
    actions = ('approve_selected',)

    @admin.display(description='Text preview')
    def text_preview(self, obj):
        if len(obj.text) > 80:
            return obj.text[:80] + '…'
        return obj.text

    @admin.action(description='Approve selected testimonials')
    def approve_selected(self, request, queryset):
        updated = queryset.update(approved=True)
        self.message_user(request, f'{updated} testimonial(s) approved.')
