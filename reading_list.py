#!/usr/bin/env python3
""" This app searches for books and constructs a reading list"""
from requests import get
from sys import exit

class ReadingList:
  '''
    Contains attributes and methods to run reading list application
  '''
  reading_list = []

  def get_input(self):
    '''Prompts user and returns user input'''

    print("Hello! Type in a book or author to start: ")
    user_input = input()
    if user_input == 'quit':
      exit(0)

    print(f'Searching for {user_input}...')
    return user_input

  def print_book_info(self, book, count):
    """Prints user search to screen"""
    if len(book.get('authors')) > 1:
      separator = ', '
      print(f"{count }. {separator.join(book.get('authors'))}", end = ', ')
    else:
      print(f"{count }. {book.get('authors')[0]}", end = ', ')
    print(book.get('title'), end = ', ')
    print(book.get('publisher'))

  def get_books(self, search_terms):
    '''
      Returns a list of five dictionary items and prints to screen
      author, title, and publisher
    '''

    books = []

    url = 'https://www.googleapis.com/books/v1/volumes?q='

    # API_key = '&key=AIzaSyCd3eVVU4zJWdn0XnNEhuUOtC7HU03CnrE'

    # response = get('https://www.googleapis.com/books/v1/volumes?q=Steig+Larsson&maxResults=5')

    max_results = '&maxResults=5'

    response = get(url + search_terms + max_results)

    if not response:
      print('An error has occurred.')

    items = response.json().get('items')
    
    if not items:
      print(f'Sorry, nothing found for {search_terms}')
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
    print('\n\nPress a number and enter to save a book to your reading list')
    print('Or press "q" and enter to exit')

  def save_to_list(self, books):
    """
      Saves books to reading_list

      Returns True is user is selecting a book, False if finished
    """
    self.save_books_prompt()

    to_quit = ['q', 'Q'] 
    user_input = input()

    if user_input in to_quit:
      return False

    valid_input = [1, 2, 3, 4, 5] # this needs to be refactored
    if int(user_input) not in valid_input:
      print(f'{user_input} is not in the list.')
      print('Please make another selection.')
    else:
      print('*********************************')
      print(f'* Item {user_input} saved to reading list! *')
      print('*********************************')
      to_add = books.pop(int(user_input) - 1)
      self.reading_list.append(to_add)
      for count, book in enumerate(books, 1):
        self.print_book_info(book, count)

    return True

  def run_app(self):
    terms = self.get_input()
    books = self.get_books(terms)
    is_selecting = self.save_to_list(books)
    while is_selecting:
      is_selecting = self.save_to_list(books)

if __name__ == "__main__":
  rl = ReadingList()
  rl.run_app()
