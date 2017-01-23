from odoo.tests.common import HttpCase
from odoo import http


class AuxiliarClass:
    def __init__(self, is_done, name):
        self.is_done = is_done
        self.name = name
    is_done = False;
    name = '';


class TestViewsGet(HttpCase):

    def test_view_hello(self):
        response = self.url_open('/hello/').read()
        self.assertIn('Hello', response)

    def test_view_hellocms(self):
        response = self.url_open('/hellocms/hello').read()
        self.assertIn('Hello', response)
