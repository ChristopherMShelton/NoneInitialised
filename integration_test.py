from person import Person
import uuid
import unittest
from example import app
import json

class IntegrationTest(unittest.TestCase):
   def setUp(self):
       self.client = app.test_client()
    
   def test_get_person(self):
       response = self.client.get('/person/1d8c5b28-84c8-485a-9cdb-0bd49eb1298e')
       self.assertEqual(response.status_code, 200)
       person_test = json.loads(response.get_data())
       self.assertEqual(person_test['firstname'],'fred')
       self.assertEqual(person_test['surname'],'bloggs')
    
  