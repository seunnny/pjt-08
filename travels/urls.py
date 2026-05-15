from django.urls import path

from . import views


urlpatterns = [
    path("places/", views.place_list, name="place_list"),
    path("places/search/", views.place_search, name="place_search"),
    path("places/<int:place_pk>/", views.place_detail, name="place_detail"),
    path("places/<int:place_pk>/reviews/", views.create_review, name="create_review"),
    path("reviews/", views.review_list, name="review_list"),
    path("reviews/<int:review_pk>/", views.review_detail, name="review_detail"),
]
