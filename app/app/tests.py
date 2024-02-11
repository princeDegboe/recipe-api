"""
Sample test
"""
from django.test import SimpleTestCase

from app import calc 

class  CalcTests(SimpleTestCase):
    """Test calc module"""
    def test_add_numbers(self):
        """Test adding number together"""
        res  = calc.add(3,4)
        self.assertEqual(res ,7)