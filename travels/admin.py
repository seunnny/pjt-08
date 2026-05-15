from django.contrib import admin

from .models import Place, Review


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "address", "created_at")
    search_fields = ("name", "address", "accessibility_info")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "place", "title", "rating", "created_at")
    list_filter = ("rating", "created_at")
    search_fields = ("title", "content", "accessibility_keywords", "place__name")
