from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Place, Review
from .serializers import PlaceSerializer, ReviewSerializer


@api_view(["GET"])
def place_list(request):
    places = Place.objects.all()
    serializer = PlaceSerializer(places, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def place_detail(request, place_pk):
    place = get_object_or_404(Place, pk=place_pk)
    serializer = PlaceSerializer(place)
    return Response(serializer.data)


@api_view(["GET"])
def review_list(request):
    reviews = Review.objects.select_related("place").all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
def review_detail(request, review_pk):
    review = get_object_or_404(Review.objects.select_related("place"), pk=review_pk)

    if request.method == "GET":
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    review.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def create_review(request, place_pk):
    place = get_object_or_404(Place, pk=place_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(place=place)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def place_search(request):
    query = request.query_params.get("q", "").strip()
    keyword = request.query_params.get("keyword", "").strip()

    places = Place.objects.all()

    if query:
        places = places.filter(
            Q(name__icontains=query)
            | Q(address__icontains=query)
            | Q(description__icontains=query)
        )

    if keyword:
        places = places.filter(
            Q(accessibility_info__icontains=keyword)
            | Q(reviews__accessibility_keywords__icontains=keyword)
            | Q(reviews__content__icontains=keyword)
        )

    serializer = PlaceSerializer(places.distinct(), many=True)
    return Response(serializer.data)
