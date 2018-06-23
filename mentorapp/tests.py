from django.test import TestCase
from mentorapp.serialisers import *
import requests
import json


URL = "http://127.0.0.1:8000/api/colleges/"
# Create your tests here.
class CollegeTestCase(TestCase):
    def setUp(self):
        self.college = College.objects.create(name="vce", location='mp', acronym='vce', contact='vce@gmail.com')
        self.serializer = CollegeSerialiser(self.college)

    def test_college_valid_serialise(self):
        self.assertEqual(self.serializer.data,
                         {'name': 'vce', 'location': 'mp', 'acronym': 'vce', 'contact': 'vce@gmail.com'})

    def test_college_invalid_serialise(self):
        self.assertNotEqual(self.serializer.data,
                            {'name': 'vce1', 'location': 'mp', 'acronym': 'vcne', 'contact': 'vce@gmail.com'})
    def testing_get_college(self):
        jason_response = requests.get(URL+"1").json()
        expected_response = '{"id": 1, "name": "CVR College of Engineering", "location": "Hyderabad", "acronym": "cvr", "contact": "contact@cvr.edu"}'
        self.assertEqual(jason_response,expected_response)

    def testing_put_college(self):
        data = {"name": "IIIT Hyderabad", "location": "Hyderabad", "acronym": "IIIT", "contact": "iiit@arpit.com"}
        post_response = requests.post(URL,data= json.dumps(data))
        response_data = post_response.json()
        new_id = response_data['id']
        get_response = requests.get(URL+str(new_id))
        self.assertEqual(post_response.text,get_response.text)
