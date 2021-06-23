#!/usr/bin/env python3
""" This module contains utility functions for ReadingList class"""

import json
import os
from requests import get
from sys import exit

def exit_app():
  print('\nBye. Enjoy your books!\n')
  exit(0)

def get_books(search_terms):
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

  response = get_response(search_terms)

  items = response.json().get('items')
  # print(f"ITEMS: {items}")
  if not items:
    print(f'\nSorry, nothing found for {search_terms}\n')
    return

  print_volume_info(response)

  return books

def get_response(search_terms):
  url = 'https://www.googleapis.com/books/v1/volumes?q='

  max_results = '&maxResults=5'

  response = get(url + search_terms + max_results)
  # print(response.text)
  if not response:
    print('\nAn error has occurred.\n')
    return

  return response

def greet():
  print("\nHello! Enter a book or author to start")
  print("Type the word 'list' to see your reading list")
  print("Or type the word 'exit' to leave\n")

# def handle_input(user_input):
#   if user_input == 'exit':
#     exit_app()
#   else if user_input == 'list' 

def print_book_info(book, count=1):
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

def print_volume_info(response):
  books = []

  items = response.json().get('items')
  # print(f"ITEMS: {items}")
  if not items:
    print(f'\nSorry, nothing found for {search_terms}\n')
    return

  for count, item in enumerate(items, 1):
    my_dict = {}
    volume_info = item.get('volumeInfo')
    print_book_info(volume_info, count)

    my_dict = {
      'authors': volume_info.get('authors'),
      'title': volume_info.get('title'),
      'publisher': volume_info.get('publisher')
    }

    books.append(my_dict)
  
  return books

def save_leave_prompt():
    """
    Prompts user to save book or exit from book search
    
    Parameters
    ----------
    None

    Returns
    -------
    None
    """

    print('\nPress a number and enter to save a book to your reading list')
    print('Or press "q" and enter to exit\n')

def save_or_leave_list(books):
    """
    Prompts user to save book or exit from book search
    
    Parameters
    ----------
    None

    Returns
    -------
    None
    """

    save_leave_prompt()

    leave_list = ['q', 'Q']
    user_input = input()

    if user_input in leave_list:
      return False