from flask import url_for, redirect
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

class TestIndex(TestBase):

    def test_index_page(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

class TestIndexContentTitle(TestBase):
    
    def test_index_has_h1_title(self):
        response = self.client.get(url_for('index'))
        html = response.data.decode()

        assert "<h3>Simple number Add</h3>" in html

class TestIndexContentInput(TestBase):
    def test_index_has_input_field(self):
        response = self.client.get(url_for('index'))
        html = response.data.decode()

        assert '<input type="number" name="num1" placeholder="Enter num1" id="">' in html
