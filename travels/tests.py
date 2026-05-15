from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import Place, Review


class TravelsAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.place = Place.objects.create(
            name="Seoul Forest",
            address="Seoul Seongdong-gu",
            description="Accessible public park",
            accessibility_info="wheelchair access, ramp",
            latitude="37.544388",
            longitude="127.037442",
        )
        self.review = Review.objects.create(
            place=self.place,
            title="Easy to move around",
            content="The entrance had a ramp and the paths were wide.",
            accessibility_keywords="wheelchair, ramp",
            rating=5,
        )

    def test_place_list(self):
        response = self.client.get("/api/places/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["name"], "Seoul Forest")
        self.assertEqual(response.data[0]["reviews_count"], 1)

    def test_place_detail(self):
        response = self.client.get(f"/api/places/{self.place.pk}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["address"], "Seoul Seongdong-gu")

    def test_place_endpoints_allow_get_only(self):
        response = self.client.post("/api/places/", {"name": "Busan"})

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_review_list(self):
        response = self.client.get("/api/reviews/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["place"], self.place.pk)
        self.assertEqual(response.data[0]["place_name"], "Seoul Forest")

    def test_create_review(self):
        payload = {
            "title": "Elevator available",
            "content": "It was easy to move from the station.",
            "accessibility_keywords": "elevator",
            "rating": 4,
        }

        response = self.client.post(
            f"/api/places/{self.place.pk}/reviews/",
            payload,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["place"], self.place.pk)
        self.assertEqual(Review.objects.count(), 2)

    def test_update_review(self):
        response = self.client.put(
            f"/api/reviews/{self.review.pk}/",
            {
                "title": "Updated review",
                "content": "Adding more accessibility details.",
                "accessibility_keywords": "wheelchair, elevator",
                "rating": 4,
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated review")
        self.assertEqual(response.data["rating"], 4)

    def test_delete_review(self):
        response = self.client.delete(f"/api/reviews/{self.review.pk}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Review.objects.filter(pk=self.review.pk).exists())

    def test_search_places_by_query_and_keyword(self):
        response = self.client.get("/api/places/search/?q=Seoul&keyword=ramp")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Seoul Forest")
