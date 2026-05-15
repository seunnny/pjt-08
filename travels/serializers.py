from rest_framework import serializers

from .models import Place, Review


class ReviewSerializer(serializers.ModelSerializer):
    place = serializers.PrimaryKeyRelatedField(read_only=True)
    place_name = serializers.CharField(source="place.name", read_only=True)

    class Meta:
        model = Review
        fields = (
            "id",
            "place",
            "place_name",
            "title",
            "content",
            "accessibility_keywords",
            "rating",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "place", "place_name", "created_at", "updated_at")


class PlaceSerializer(serializers.ModelSerializer):
    reviews_count = serializers.IntegerField(source="reviews.count", read_only=True)

    class Meta:
        model = Place
        fields = (
            "id",
            "name",
            "address",
            "description",
            "accessibility_info",
            "latitude",
            "longitude",
            "reviews_count",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "reviews_count", "created_at", "updated_at")
