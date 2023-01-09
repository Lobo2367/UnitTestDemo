import unittest
from main import *
# Add imports here

def test_id_is_4_len(self):
  self.assertTrue(len(insertID()) == 5)

def test_id_is_string(self):
  self.assertTrue(isinstance(insertID(), str))