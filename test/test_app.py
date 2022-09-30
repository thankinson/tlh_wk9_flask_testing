from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestNum(TestBase):
    def addition(self, num1, num2):
        return num1 + num2
        
    def test_two_numbers_equel_five(self):
        num1 = 2
        num2 = 3
        isTrue = self.addition(num1, num2) == 5
       
        assert isTrue

class TestPage(TestBase):
    def is_index(self):
        response = TestBase.client.get(url_for('index'))
        # self.assertEqual(response.status_code, 200)
        # isTrue = self.assertIn()
        assert b'Simple number Add' in response.data