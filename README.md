# Reading List

## What is this project?
This a command line application that allows you to search for books and construct a reading list. The application must be run on Python version 3.6 or newer.

## Dependencies
* Install the `requests` module with the following command `python3 -m pip install requests`

* More information on installation and documentation of the `requests` module can be found [here](https://pypi.org/project/requests/)

## How does it work?
* From GitHub click the green code button
<img width="366" alt="Screen Shot 2021-06-16 at 11 16 24 AM" src="https://user-images.githubusercontent.com/14856004/122251359-0c2fbe00-ce90-11eb-9180-3b7e60388a88.png">


* Click the copy button to copy the url
<img width="448" alt="Screen Shot 2021-06-16 at 11 16 35 AM" src="https://user-images.githubusercontent.com/14856004/122251590-413c1080-ce90-11eb-91d6-a44be4d8ce62.png">

* Open a terminal window and clone the repository by tying `git clone` and paste in the url
<img width="641" alt="Screen Shot 2021-06-16 at 11 21 31 AM" src="https://user-images.githubusercontent.com/14856004/122251750-69c40a80-ce90-11eb-8256-40c08905b081.png">

* `cd` into the directory
<img width="252" alt="Screen Shot 2021-06-16 at 11 49 20 AM" src="https://user-images.githubusercontent.com/14856004/122251923-90824100-ce90-11eb-9dff-be05a6cb1777.png">

* Run the application by typing `./reading_list.py`
<img width="362" alt="Screen Shot 2021-06-16 at 11 50 13 AM" src="https://user-images.githubusercontent.com/14856004/122252129-bc052b80-ce90-11eb-8903-244818148c79.png">

* You should see a welcome prompt with instructions
<img width="474" alt="Screen Shot 2021-06-16 at 11 20 37 AM" src="https://user-images.githubusercontent.com/14856004/122252186-c7585700-ce90-11eb-9604-9976b5d95347.png">

Hooray! 🎉🎉🎉

Your list will be saved locally to a file called `reading_list.json`.
Even if you exit the application your reading list will be available to you when you come back.

🐞 Feel free to report any bugs you find.

📖 Enjoy your books! 📖

## Running Tests

* Install the `parameterized` module using `pip3 install parameterized`

* More information and documentation on `paramterized` can be found [here](https://pypi.org/project/parameterized/)

* Run tests with the following command `python3 -m unittest discover tests`

* Run tests file by file using `python3 -m unittest tests/test_models/test_books.py` and `python3 -m unittest tests/test_models/test_reading_list.py`

## Author ✏️
* **Viet Tran** - [veeteeran](https://github.com/veeteeran)


