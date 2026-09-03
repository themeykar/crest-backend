from django.urls import path

from . import views

urlpatterns = [
    path('gallery/', views.GalleryListView.as_view(), name='gallery-list'),
    path('testimonials/', views.TestimonialListView.as_view(), name='testimonial-list'),
    path('testimonials/submit/', views.TestimonialCreateView.as_view(), name='testimonial-submit'),
]
