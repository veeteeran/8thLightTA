#!/usr/bin/env python3
""" This app searches for books and constructs a reading list"""

class ReadingList:
  '''
    Contains attributes and methods to run reading list application
  '''
  def get_input(self):
    print("Hello! Type in a book or author to start: ")
    x = input()
    print(f'Searching for {x}...')

if __name__ == "__main__":
  rl = ReadingList()
  rl.get_input()
