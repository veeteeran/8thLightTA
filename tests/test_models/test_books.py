#!/usr/bin/env python3
"""Module for reading_list.py unittests"""
from fixtures import TEST_BOOKS, TEST_PAYLOAD
from parameterized import parameterized
import books
from unittest import TestCase
from unittest.mock import patch, PropertyMock

class TestBooks(TestCase):
  """Books unittests"""
  @patch('requests.get')
  def test_get_books(self, mock_requests_get):
    """Test get_books"""

    with patch('books.Books.get_books',
                new_callable=PropertyMock) as mock_get_books:

      test_object = books.Books()
      mock_requests_get().json.return_value = TEST_PAYLOAD
      mock_get_books.return_value = TEST_BOOKS

      self.assertEqual(test_object.get_books, TEST_BOOKS)
      mock_requests_get.assert_called_once()
      mock_get_books.assert_called_once_with()
  