# Books Recommendation System  


This repository contains code for Recommendation of differents books. Developed using Flask and python. 






### 📂 Structure

The directory contains web sub directories and a sub directory for hosting model and other scripts:

1. [app.py](https://github.com/shsarv/Restaurant-Recommendation-System/blob/main/app.py) The file which contains all the main backend operations of the website and used to run the flask server locally.
   
2. [requirement.txt](https://github.com/shsarv/Restaurant-Recommendation-System/blob/main/requirements.txt) contains all the dependencies.

3. [templates](https://github.com/shsarv/Restaurant-Recommendation-System/blob/main/templates) contains the html file.

      |- - - [home.html](https://github.com/shsarv/Restaurant-Recommendation-System/blob/main/templates/home.html) contains home page.
      
      |- - - [login.html](https://github.com/shsarv/Restaurant-Recommendation-System/blob/main/templates/search.html) contains login page.

      |- - - [new.html](https://github.com/shsarv/Restaurant-Recommendation-System/blob/main/templates/search.html) contains page which adds new book from the user.

      |- - - [rating.html](https://github.com/shsarv/Restaurant-Recommendation-System/blob/main/templates/search.html) contains rating page.

      |- - - [search.html](https://github.com/shsarv/Restaurant-Recommendation-System/blob/main/templates/search.html) contains search page.

      |- - - [signup.html](https://github.com/shsarv/Restaurant-Recommendation-System/blob/main/templates/search.html) contains signup page.

      |- - - [thankyou.html](https://github.com/shsarv/Restaurant-Recommendation-System/blob/main/templates/search.html) contains thankyou page.

      |- - - [welcome.html](https://github.com/shsarv/Restaurant-Recommendation-System/blob/main/templates/search.html) contains welcome page.

5. [static](https://github.com/shsarv/Restaurant-Recommendation-System/blob/main/static) contains the css file and images.

      |- - - [home.css](https://github.com/shsarv/Restaurant-Recommendation-System/blob/main/static/home.css) contains Styling of home page.
      
      |- - - [search.css](https://github.com/shsarv/Restaurant-Recommendation-System/blob/main/static/search.css) contains Styling of Search page.
      
      |- - - [main.css](https://github.com/shsarv/Restaurant-Recommendation-System/blob/main/static/background1.jpg) contains Styling of login and signup page.

      |- - - [rating.css](https://github.com/shsarv/Restaurant-Recommendation-System/blob/main/static/home.css) contains Styling of rating page.

      |- - - [thankyou.css](https://github.com/shsarv/Restaurant-Recommendation-System/blob/main/static/home.css) contains Styling of thankyou page.

      |- - - [welcome.css](https://github.com/shsarv/Restaurant-Recommendation-System/blob/main/static/home.css) contains Styling of welcome page.

6. [books.csv](https://github.com/shsarv/Restaurant-Recommendation-System/blob/main/main_rest.csv) contains the  data of the books.

### Codebase <img src="https://www.flaticon.com/svg/static/icons/svg/3565/3565585.svg" width="24px">

The entire code has been developed using Python programming language. The recommendation has used ratings for sorting by taking the age, genre and author(where genre and author are optional) as input from the user. The website is developed using Flask. The website asks the user to rate the book recommended which causes change in the rating of the book and is refelected for other users as well. Users can also add books of their choice which also can be read by other users. The feature of recommendation is disabled if user is not logged in to ensure authentication.

### How to run the project 🚀:

  1. Open the `Terminal`.
  2. Clone the repository by entering `$ git clone https://github.com/shsarv/Restaurant-Recommendation-System.git`.
  3. Ensure that `Python3` and `pip` are installed on the system.
  4. change the diectory to repository name using  `$ cd [Repository name]`.
  5. Enter the cloned repository directory and execute `pip install -r requirements.txt`.
  6. Now, execute the following command: `flask run` and it will point to the `localhost` server with the port `5000`.
  7. Enter the `IP Address: http://localhost:5000` on a web browser and use the application.
  
### Dependencies <img src="https://www.flaticon.com/svg/static/icons/svg/2621/2621122.svg" width="24px">

The following dependencies can be found in [requirements.txt](https://github.com/shsarv/Restaurant-Recommendation-System/blob/main/requirements.txt):

  1. [Flask](https://palletsprojects.com/p/flask/)
  2. [pandas](https://pandas.pydata.org/)
  3. [numpy](http://www.numpy.org/)
  4. [gunicorn](https://gunicorn.org/)
  
