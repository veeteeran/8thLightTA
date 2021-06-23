#!/usr/bin/env python3
"""Module for reading_list.py unittests"""
from parameterized import parameterized
import reading_list
from unittest import TestCase
from unittest.mock import patch, PropertyMock

class TestReadingList(TestCase):
  """ReadingList unittests"""
  @parameterized.expand([
        ("Hello", "Hello"),
        ("dune", "dune"),
        ("Neil Gaiman", "Neil Gaiman"),
        ("", ""),
    ])
  def test_get_input(self, input, expected):
    """Test get_input"""
    with patch('builtins.input', lambda *args: input) as mock_input:
      assert mock_input() == expected

    with patch('reading_list.ReadingList.get_input', new_callable=PropertyMock) as mock_get_input:
      mock_get_input.return_value = expected
      test_obj = reading_list.ReadingList()
      self.assertEqual(test_obj.get_input, expected)