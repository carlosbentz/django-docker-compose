from django.test import TestCase
from rest_framework.test import APIClient


class TestSongView(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.song_data_1 = {
            "title": "Fortunate son",
            "artist": {
                "name": "Creedence Clearwater Revival"
            }
        }

        self.song_data_2 = {
            "title": "Green river",
            "artist": {
                "name": "Creedence Clearwater Revival"
            }
        }

        self.song_data_3 = {
            "title": "My way",
            "artist": {
                "name": "Frank Sinatra"
            }
        }

        self.song_data_4 = {
            "title": "General Lee",
            "artist": {
                "name": "Johnny Cash"
            }
        }
    
    def test_create_song(self):
        
        response = self.client.post(
            "/api/songs/", self.song_data_1, format="json"
        )
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.json(), 
            {
                "id": 1,
                "title": "Fortunate son",
                "artist": {
                    "id": 1,
                    "name": "Creedence Clearwater Revival"
                },
                "votes": 1
            }
        )

    def test_create_song_with_same_artist(self):
        
        response_1 = self.client.post(
            "/api/songs/", self.song_data_1, format="json"
        )

        response_2 = self.client.post(
            "/api/songs/", self.song_data_2, format="json"
        )
        

        self.assertEqual(
            response_1.json()["artist"]["id"], response_2.json()["artist"]["id"]
        )
        self.assertEqual(response_1.status_code and response_2.status_code, 201)


    def test_cannot_create_song(self):
        
        response = self.client.post(
            "/api/songs/", {"song": "mrs crowley"}, format="json"
        )

        self.assertEqual(response.status_code, 400)


    def test_list_songs(self):
        self.client.post(
            "/api/songs/", self.song_data_1, format="json"
        )
        self.client.post(
            "/api/songs/", self.song_data_2, format="json"
        )
        self.client.post(
            "/api/songs/", self.song_data_3, format="json"
        )
        self.client.post(
            "/api/songs/", self.song_data_4, format="json"
        )


        response = self.client.get("/api/songs/", format="json")


        self.assertEqual(
            response.json()[0]["id"], 1
        )
        self.assertEqual(
            response.json()[1]["id"], 2
        )
        self.assertEqual(
            response.json()[2]["id"], 3
        )
        self.assertEqual(
            response.json()[3]["id"], 4
        )


        self.assertEqual(response.status_code, 200)


    def test_retrieve_songs(self):
        self.client.post(
            "/api/songs/", self.song_data_1, format="json"
        )
        self.client.post(
            "/api/songs/", self.song_data_2, format="json"
        )
        self.client.post(
            "/api/songs/", self.song_data_3, format="json"
        )


        response = self.client.get("/api/songs/2/", format="json")

        self.assertEqual(
            response.json()["id"], 2
        )

        self.assertEqual(response.status_code, 200)


    def test_cannot_retrieve_songs(self):
        response = self.client.get("/api/songs/2/", format="json")

        self.assertEqual(response.status_code, 404)


    def test_delete_songs(self):
        self.client.post(
            "/api/songs/", self.song_data_1, format="json"
        )
        
        response = self.client.delete("/api/songs/1/", format="json")
        
        self.assertEqual(response.status_code, 204)
        

    def test_cannot_delete_songs(self):
        response = self.client.delete("/api/songs/1/", format="json")
        
        self.assertEqual(response.status_code, 404)


    def test_patch_songs(self):
        self.client.post(
            "/api/songs/", self.song_data_1, format="json"
        )

        response = self.client.patch("/api/songs/1/", format="json")
        response = self.client.patch("/api/songs/1/", format="json")


        self.assertEqual(response.json()["votes"], 3)
        self.assertEqual(response.status_code, 200)


    def test_cannot_patch_songs(self):
        response = self.client.patch("/api/songs/1/", format="json")

        self.assertEqual(response.status_code, 404)

    def test_put_songs(self):
        self.client.post(
            "/api/songs/", self.song_data_1, format="json"
        )

        response = self.client.put("/api/songs/1/", self.song_data_4, format="json")


        self.assertEqual(response.json(), {"id": 1, "title": "General Lee", "artist": {"id": 2, "name": "Johnny Cash"}, "votes": 1})
        self.assertEqual(response.status_code, 200)


    def test_cannot_put_songs(self):
        self.client.post(
            "/api/songs/", self.song_data_1, format="json"
        )

        response = self.client.put("/api/songs/1/", {"title": "ace of spades"}, format="json")

        self.assertEqual(response.status_code, 400)

        response = self.client.put("/api/songs/4/", self.song_data_4, format="json")

        self.assertEqual(response.status_code, 404)
