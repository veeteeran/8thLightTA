#!/usr/bin/env python3
""" This app searches for books and constructs a reading list"""

import json
import os
from requests import get
from sys import exit

class ReadingList:
  """
    Contains attributes and methods to run reading list application
    
    ...

    Class Variables
    ----------
    reading_list : list
        holds deserialized reading list
    file_path : str
        path to reading_list.json

    Methods
    -------
    get_input():
      Prompts user and returns user input

    print_book_info(book, count = 1):
      Prints user search to screen

    get_books(search_terms):
      Returns a list of five dictionary items and prints to screen
      author, title, and publisher

    save_books_prompt():
      Prompts user to save book or exit from book search

    save_to_list(books):
      Saves books to reading_list

    show_list():
      Prints reading_list

    run_app():
      Runs ReadingList app
  """

  reading_list = []
  __file_path = 'reading_list.json'

  def get_input(self):
    """Prompts user and returns user input"""

    print("\nHello! Enter a book or author to start")
    print("Type the word 'list' to see your reading list")
    print("Or type the word 'exit' to leave\n")

    user_input = input()
    if user_input == 'exit':
      print('\nBye. Enjoy your books!\n')
      exit(0)
    if user_input == 'list':
      self.show_list()
      return user_input

    print(f'\nSearching for {user_input}...\n')
    return user_input

  def print_book_info(self, book, count = 1):
    """Prints user search to screen"""

    if len(book.get('authors')) > 1:
      separator = ', '
      print(f"{count }. {separator.join(book.get('authors'))}", end = ', ')
    else:
      print(f"{count }. {book.get('authors')[0]}", end = ', ')
    print(book.get('title'), end = ', ')
    print(book.get('publisher'))

  def get_books(self, search_terms):
    """
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

    url = 'https://www.googleapis.com/books/v1/volumes?q='

    max_results = '&maxResults=5'

    response = get(url + search_terms + max_results)

    if not response:
      print('\nAn error has occurred.\n')

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

  def save_books_prompt(self):
    """Prompts user to save book or exit from book search"""

    print('\nPress a number and enter to save a book to your reading list')
    print('Or press "q" and enter to exit\n')

  def save_to_list(self, books):
    """
    Saves books to reading_list

    Parameters
    ----------
    books : list
        List of dictionaries containing book info

    Returns
    -------
    True is user is selecting a book, False when finished
    """

    self.save_books_prompt()

    to_quit = ['q', 'Q'] 
    user_input = input()

    if user_input in to_quit:
      return False

    valid_input = [count for count, book in enumerate(books, 1)]
    if int(user_input) not in valid_input:
      print(f'\n{user_input} is not in the list.')
      print('Please make another selection.\n')
    else:
      print('\n*********************************')
      print(f'* Item {user_input} saved to reading list! *')
      print('*********************************\n')
      to_add = books.pop(int(user_input) - 1)
      for count, book in enumerate(books, 1):
        self.print_book_info(book, count)

      if os.stat(self.__file_path).st_size != 0:
        with open(self.__file_path, 'r') as read_file:
            self.reading_list = json.load(read_file)

      with open(self.__file_path, 'w') as write_file:
        self.reading_list.append(to_add)
        json.dump(self.reading_list, write_file)

    return True

  def show_list(self):
    """Prints reading_list"""

    with open(self.__file_path, 'r') as read_file:
      try:
        books = json.load(read_file)
        print("\nHere's your list!\n")
        for count, book in enumerate(books, 1):
          self.print_book_info(book, count)
      except json.decoder.JSONDecodeError as e:
        print('\nYour list is empty\n')

  def run_app(self):
    """Runs ReadingList app"""
    
    app_running = True
    while app_running:
      user_input = self.get_input()
      if user_input != 'list':
        books = self.get_books(user_input)
        is_selecting = self.save_to_list(books)
        while is_selecting:
          is_selecting = self.save_to_list(books)

      app_running = True

if __name__ == "__main__":
  rl = ReadingList()
  rl.run_app()
