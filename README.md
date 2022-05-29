# bookies_p


This repository contains code for Recommendation of differents books. Developed using Flask and python for backend and HTML/CSS/Bootstrap for the frontend. 


### 📂 Structure

The directory contains web sub directories and a sub directory for hosting model and other scripts:

1. [app.py](https://github.com/trisha3290/bookies_p/blob/main/app.py) The file which contains all the main backend operations of the website and used to run the flask server locally.
   
2. [requirement.txt](https://github.com/trisha3290/bookies_p/blob/main/requirements.txt) contains all the dependencies.

3. [templates](https://github.com/trisha3290/bookies_p/blob/main/templates) contains the html file.

      |- - - [home.html](https://github.com/trisha3290/bookies_p/blob/main/templates/home.html) contains home page.
      
      |- - - [login.html](https://github.com/trisha3290/bookies_p/blob/main/templates/login.html) contains login page.

      |- - - [new.html](https://github.com/trisha3290/bookies_p/blob/main/templates/new.html) contains page which adds new book from the user.

      |- - - [rating.html](https://github.com/trisha3290/bookies_p/blob/main/templates/rating.html) contains rating page.

      |- - - [search.html](https://github.com/trisha3290/bookies_p/blob/main/templates/search.html) contains search page.

      |- - - [signup.html](https://github.com/trisha3290/bookies_p/blob/main/templates/signup.html) contains signup page.

      |- - - [thankyou.html](https://github.com/trisha3290/bookies_p/blob/main/templates/thankyou.html) contains thankyou page.

      |- - - [welcome.html](https://github.com/trisha3290/bookies_p/blob/main/templates/welcome.html) contains welcome page.

5. [static](https://github.com/trisha3290/bookies_p/blob/main/static) contains the css file and images.

      |- - - [home.css](https://github.com/trisha3290/bookies_p/blob/main/static/home.css) contains Styling of home page.
      
      |- - - [search.css](https://github.com/trisha3290/bookies_p/blob/main/static/search.css) contains Styling of Search page.
      
      |- - - [main.css](https://github.com/trisha3290/bookies_p/blob/main/static/main.css) contains Styling of login and signup page.

      |- - - [rating.css](https://github.com/trisha3290/bookies_p/blob/main/static/rating.css) contains Styling of rating page.

      |- - - [thankyou.css](https://github.com/trisha3290/bookies_p/blob/main/static/thankyou.css) contains Styling of thankyou page.

      |- - - [welcome.css](https://github.com/trisha3290/bookies_p/blob/main/static/welcome.css) contains Styling of welcome page.

6. [books.csv](https://github.com/trisha3290/bookies_p/blob/main/books.csv) contains the  data of the books.

### Codebase 

The entire code has been developed using Python programming language. The recommendation has used ratings for sorting by taking the age, genre and author(where genre and author are optional) as input from the user. The python's sort function uses TIM sort algorithm which is a combination of insertion sort and merge sort making it highly powerful. It's average time complexity is O(n) and worst time complexity is O(nlogn). The space complexity is O(n). The website is developed using Flask. The website asks the user to rate the book recommended which causes change in the rating of the book and is refelected for other users as well as rating is the primary factor for sorting. Users can also add books of their choice which also can be recommended to other users. The feature of rating and adding new is disabled if user is not logged in to ensure authentication.

### How to run the project 🚀:

  1. Open the `Terminal`.
  2. Clone the repository by entering `$ git clone https://github.com/trisha3290/bookies_p.git`.
  3. Ensure that `Python3` and `pip` are installed on the system.
  4. change the diectory to repository name using  `$ cd [Repository name]`.
  5. Enter the cloned repository directory and execute `pip install -r requirements.txt`.
  6. Now, execute the following command: `flask run` and it will point to the `localhost` server with the port `5000`.
  7. Enter the `IP Address: http://localhost:5000` on a web browser and use the application.
  8. No virtual environment is required after installing the required dependencies. Deactivate it in case of    activation.
  
### Dependencies 

The following dependencies can be found in [requirements.txt](https://github.com/trisha3290/bookies_p/blob/main/requirements.txt):

  1. [Flask](https://palletsprojects.com/p/flask/)
  2. [pandas](https://pandas.pydata.org/)
  3. [numpy](http://www.numpy.org/)
  
  
