"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.auth.models import User
from pengpengtao.api.operations import get_deal_by_id, get_user_by_id, get_deal_list_of_user, get_deal_list_by_state

class TestDeal(TestCase):
    def SetUp(self):
        self.assertTrue(True)


    def test_get_deal_by_id(self):
       self.assertTrue(False) 

    def test_get_user_by_id(self):
       self.assertTrue(False) 

    def test_get_deal_list(self):
       self.assertTrue(False) 
    
    def test_get_deal_list_by_state(self):
       self.assertTrue(False) 




