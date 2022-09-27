import unittest
from django.test import TestCase
from . import utils
# Create your tests here.

class FetchDataTesrCase(TestCase):
    def test_fetch_problems_count(self):
        out = utils.fetch_problems_count()
  
    @unittest.skip('Time expenisve test so skipped.')
    def test_fetch_all_questions(self):
        utils.fetch_all_problems()
