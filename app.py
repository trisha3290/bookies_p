#importing the required libraries
import pyrebase as pyrebase
from flask import Flask, render_template, url_for, flash, redirect, request, session, redirect,abort
import pandas as pd
from csv import DictWriter
app = Flask(__name__)
app.secret_key = '_5#y2LF4Q8z/'
df = pd.read_csv("books.csv")
#configuration
config = {
    "apiKey": "AIzaSyBKjSrlI4JKqqy6-iTM16Ss44rLwlVisJI",
      "authDomain": "bookies-8dbd8.firebaseapp.com",
      "databaseURL": "https://bookies-8dbd8-default-rtdb.firebaseio.com/",
      "projectId": "bookies-8dbd8",
      "storageBucket": "bookies-8dbd8.appspot.com",
      "messagingSenderId": "395639425142",
      "appId": "1:395639425142:web:b51400c5aae343d024b757",
      "measurementId": "G-64EGLB9JH2"
}
#firebase implementation
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

#function to get the sorted values on the basis of rating and age
def sort(age,genre,author):
    df1=df.loc[age>=df.age]
    if(genre!="none"):
        df2=df1.loc[df.genre==genre]
    else:
        df2=df1
    if(author!="none"):
        df3=df2.loc[df.author==author]
    else:
        df3=df2    
    df4=df3.sort_values('rating',ascending=False)
    res=[[]]
    for i in range(0,(df4.shape[0]),1):
        res.append(list(df4.iloc[i]))
    return res[1:]

#function to calculate rating change when someone rates
def rating_change(n,index):
    current_rating = df['rating'][index]
    current_votes = df['votes'][index]
    total_ratings = current_rating*current_votes
    n=float(n)
    total_ratings = total_ratings + n
    current_votes = current_votes + 1
    new_rating = total_ratings/current_votes
    df.loc[index,'rating'] = round(new_rating,1)
    df.loc[index,'votes']  = current_votes 
    df.to_csv("books.csv",index=False)

#function to add new record when someone suggests new book
def add_new_record(book_name,author_name,rating,link,genre):
    field_names = ['index','genre','author','book_name','rating','age','link','votes']
    index=len(df)
    dict={'index':index,'genre':genre,'author':author_name,'book_name':book_name,'rating':rating,'age':20,'link':link,'votes':1}
    with open('books.csv','a') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=field_names)
        dictwriter_object.writerow(dict)
        f_object.close()
print(len(df))

#person variable which tells whether the user is logged in or not
person = {"is_logged_in":False,"name":"","email":"","uid":""}
#welcome page
@app.route("/")
def welcome():
    return render_template('welcome.html')
#signup page
@app.route("/signup")
def signup():
    return render_template('signup.html')
@app.route("/register", methods = ["POST", "GET"])
def register():
    if request.method == "POST":        #Only listen to POST
        result = request.form           #Get the data submitted
        email = result["email"]
        password = result["pass"]
        name = result["name"]
        try:
            #Try creating the user account using the provided data
            auth.create_user_with_email_and_password(email, password)
            #Login the user
            user = auth.sign_in_with_email_and_password(email, password)
            #Add data to global person
            global person
            person["is_logged_in"] = True
            person["email"] = user["email"]
            person["uid"] = user["localId"]
            person["name"] = name
            #Append data to the firebase realtime database
            data = {"name": name, "email": email}
            db.child("users").child(person["uid"]).set(data)
            #Go to welcome page
            flash('You have successfully created your account','error')
            return redirect(url_for('home'))
            
        except:
            #If there is any error, redirect to register
            return redirect(url_for('welcome'))

    else:
        if person["is_logged_in"] == True:
            return redirect(url_for('home'))
        else:
            return redirect(url_for('welcome'))
#adding a new record
@app.route("/new")
def new():
    return render_template('new.html')
@app.route("/add", methods=['POST','GET'])
def add():
    if request.method == "POST":
        result=request.form
        book_name=result["book_name"]
        print(book_name)
        author_name=result["author_name"]
        rate=result["rate"]
        link=result["link"]
        genre=result["genre"]
        add_new_record(book_name,author_name,rate,link,genre)
        print(len(df))
        return render_template('thankyou.html')
#home page
@app.route("/home", methods=['POST','GET'])
def home():
    return render_template('home.html',user=person)
#rating change
@app.route("/rating")
def rating():
    return render_template('rating.html')
@app.route("/change", methods=['GET','POST'])
def change():
    if request.method == "POST":
        n = request.form['rate']
        index = int(request.form["book_id"])
        rating = df['rating'][index]
        rating_change(n,index)
        new_rating = df['rating'][index]
        print(rating)
        print(new_rating)
        return render_template('thankyou.html')
#login
@app.route("/login")
def login():
    return render_template('login.html')
@app.route("/result", methods=['POST','GET'])
def result():
    if request.method == "POST":        #Only if data has been posted
        result = request.form           #Get the data
        email = result["email"]
        password = result["pass"]
        try:
            #Try signing in the user with the given information
            user = auth.sign_in_with_email_and_password(email, password)
            #Insert the user data in the global person
            global person
            person["is_logged_in"] = True
            person["email"] = user["email"]
            person["uid"] = user["localId"]
            #Get the name of the user
            data = db.child("users").get()
            person["name"] = data.val()[person["uid"]]["name"]
            #Redirect to home page
            return redirect(url_for('home'))
        except:
            #If there is any error, redirect back to login
            flash('Invalid credentials','error')
            return redirect(url_for('login'))
    else:
        if person["is_logged_in"] == True:
            return redirect(url_for('home'))
        else:
            return redirect(url_for('welcome'))
#logout
@app.route("/logout")
def logout():
    person["is_logged_in"]=False
    return render_template('welcome.html')
#search
@app.route("/search", methods=['POST'])
def search():
    if request.method == 'POST':
        age = int(request.form['age'])
        genre = request.form['genre']
        author = request.form['author']
        print(author)
        res = sort( age, genre, author)
        print(res)
        return render_template('search.html', title='Search', books=res)
        #return res
    else:
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
