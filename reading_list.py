#!/usr/bin/env python3
""" This app searches for books and constructs a reading list"""
from requests import get
from sys import exit

class ReadingList:
  '''
    Contains attributes and methods to run reading list application
  '''
  def get_input(self):
    print("Hello! Type in a book or author to start: ")
    user_input = input()
    if user_input == 'quit':
      exit(0)

    print(f'Searching for {user_input}...')
    return user_input

  def get_books(self, search_terms):
    url = 'https://www.googleapis.com/books/v1/volumes?q='

    # API_key = '&key=AIzaSyCd3eVVU4zJWdn0XnNEhuUOtC7HU03CnrE'

    # response = get('https://www.googleapis.com/books/v1/volumes?q=Steig+Larsson&maxResults=5')

    max_results = '&maxResults=5'

    response = get(url + search_terms + max_results)

    if not response:
      print('An error has occurred.')

    items = response.json().get('items')
    for count, item in enumerate(items, 1):
      volume_info = item.get('volumeInfo')
      if len(volume_info.get('authors')) > 1:
        separator = ', '
        print(f"{count }. {separator.join(volume_info.get('authors'))}", end = ', ')
      else:
        print(f"{count }. {volume_info.get('authors')[0]}", end = ', ')
      print(volume_info.get('title'), end = ', ')
      print(volume_info.get('publisher'))

  def run_app(self):
    terms = self.get_input()
    self.get_books(terms)


if __name__ == "__main__":
  rl = ReadingList()
  rl.run_app()
