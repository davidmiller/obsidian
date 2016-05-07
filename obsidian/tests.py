"""
Unittests for obsidian
"""
from django.test import TestCase

from obsidian import models

class WeHaveSomeModelsTestCase(TestCase):
    def test_there_is_a_model(self):
        demographics = models.Demographics(name='Larry')
        self.assertEqual('Larry', demographics.name)
