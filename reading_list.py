#!/usr/bin/env python3
""" This class constructs a reading list using the Books class"""

from models.books import Books 
import json
import os
  
class ReadingList:
  """
    Contains attributes and methods for ReadList class
    
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
    """
    Prompts user and returns user input
    
    Parameters
    ----------
    None

    Returns
    -------
    user_input : str - search string entered from command line
    """

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

  def save_books_prompt(self):
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

  def save_to_list(self, books):
    """
    Saves books to reading_list

    Parameters
    ----------
    books : list
        List of dictionaries containing book info

    Returns
    -------
    True if user is selecting a book, False when finished
    """

    self.save_books_prompt()

    to_quit = ['q', 'Q'] 
    user_input = input()

    if user_input in to_quit:
      return False

    valid_input = [count for count, book in enumerate(books, 1)]
    b = Books()
    try:
      if int(user_input) not in valid_input:
        print(f'\n{user_input} is not in the list.')
        print('Please make another selection.\n')
        for count, book in enumerate(books, 1):
          b.print_book_info(book, count)
      else:
        print('\n*********************************')
        print(f'* Item {user_input} saved to reading list! *')
        print('*********************************\n')
        to_add = books.pop(int(user_input) - 1)
        for count, book in enumerate(books, 1):
          b.print_book_info(book, count)

        if os.stat(self.__file_path).st_size != 0:
          with open(self.__file_path, 'r') as read_file:
              self.reading_list = json.load(read_file)

        with open(self.__file_path, 'w') as write_file:
          self.reading_list.append(to_add)
          json.dump(self.reading_list, write_file)
    except ValueError:
      print(f'\n{user_input} is not a number\n')
      for count, book in enumerate(books, 1):
        b.print_book_info(book, count)

    return True

  def show_list(self):
    """
    Prints reading_list
    
    Parameters
    ----------
    None

    Returns
    -------
    None
    """

    with open(self.__file_path, 'r') as read_file:
      b = Books()
      try:
        books = json.load(read_file)
        print("\nHere's your list!\n")
        for count, book in enumerate(books, 1):
          b.print_book_info(book, count)
      except json.decoder.JSONDecodeError as e:
        print('\nYour list is empty\n')

  def run_app(self):
    """
    Runs ReadingList app
    
    Parameters
    ----------
    None

    Returns
    -------
    None
    """

    while True:
      user_input = self.get_input()
      if user_input != 'list':
        b = Books()
        books = b.get_books(user_input)
        if books != []:
          is_selecting = self.save_to_list(books)
          while is_selecting:
            is_selecting = self.save_to_list(books)

if __name__ == "__main__":
  rl = ReadingList()
  rl.run_app()
