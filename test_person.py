import unittest
import uuid
from person import Person

class TestPerson(unittest.TestCase):
  
       def test_one(self):
              new_person = Person(firstname='Geoff',surname='Rodgers',birthday='23rd December',id=uuid.uuid4())
              person_dict = new_person.to_dict()
              self.assertTrue(isinstance(person_dict, dict))
            
#if __name__ == '__main__':
#        unittest.main()