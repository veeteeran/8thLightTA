#!/usr/bin/env python3
"""Module for reading_list.py unittests"""
from fixtures import TEST_BOOKS, TEST_PAYLOAD
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

  @patch('requests.get')
  def test_get_books(self, mock_requests_get):
    """Test get_books"""

    with patch('reading_list.ReadingList.get_books',
                new_callable=PropertyMock) as mock_get_books:

      test_object = reading_list.ReadingList()
      mock_requests_get().json.return_value = TEST_PAYLOAD
      mock_get_books.return_value = TEST_BOOKS

      self.assertEqual(test_object.get_books, TEST_BOOKS)
      mock_requests_get.assert_called_once()
      mock_get_books.assert_called_once_with()
  