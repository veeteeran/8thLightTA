#!/usr/bin/env python3
""" This class searches fpr books using Google Books API"""

# import json
import os
from requests import get

class Books:
  """
    Contains attributes and methods for BooksAPI class
  """
  def get_books(self, search_terms):
    """
    Gets a list of five books based on user search

    Parameters
    ----------
    search_terms : str
        search string from user

    Returns
    -------
      List of five dictionary items and prints to screen
      author, title, and publisher
    """

    books = []

    response = self.call_api(search_terms)

    books = self.show_search_results(response)
  
    return books

  def call_api(self, search_terms):
    url = 'https://www.googleapis.com/books/v1/volumes?q='

    max_results = '&maxResults=5'

    response = get(url + search_terms + max_results)
    if not response:
      print('\nAn error has occurred.\n')

    return response

  def print_book_info(self, book, count=1):
    """
    Prints user search to screen

    Parameters
    ----------
    book : dictionary
        volumeInfo passed in from the response object

    count : int
        number to print in front of book

    Returns
    -------
    None
    """
    print(f"{count}. ", end='')

    if not book.get('authors'):
      print('None', end = ', ')
    elif len(book.get('authors')) > 1:
      separator = ', '
      print(f"{separator.join(book.get('authors'))}", end=', ')
    else:
      print(f"{book.get('authors')[0]}", end=', ')

    print(book.get('title'), end=', ')
    print(book.get('publisher'))

  def show_search_results(self, response):
    books = []

    items = response.json().get('items')
    if not items:
      print(f'\nSorry, nothing found for {search_terms}\n')
      return

    for count, item in enumerate(items, 1):
      my_dict = {}
      volume_info = item.get('volumeInfo')
      self.print_book_info(volume_info, count)

      my_dict = {
        'authors': volume_info.get('authors'),
        'title': volume_info.get('title'),
        'publisher': volume_info.get('publisher')
      }

      books.append(my_dict)
    
    return books