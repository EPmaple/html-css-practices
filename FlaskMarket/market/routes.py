from market import app
from flask import render_template
from market.models import Item

#app.route, what url in my website I'm going to navigate to and display me some
#html code; "/" root url of my website --- routing to root url of my website
@app.route("/") #decorator, one step before a function that is going to be executed
@app.route('/home')
def home_page():
  return render_template("home.html")

@app.route('/market')
def market_page():
  #3 dictionaries that happened to have the same keys
  items = Item.query.all()
  return render_template('market.html', items=items)

 
#dynamic routes
#allow this route after about/ to take in <variable>
@app.route('/about/<username>')
def about_page(username):
  return f'<h1>This is the about page of {username}</h1>'