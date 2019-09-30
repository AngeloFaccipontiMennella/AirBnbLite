from flask import Flask, Response, request, jsonify, render_template, make_response, flash, url_for, redirect
from flask_pymongo import pymongo
from database import DatabaseConnection
#from Services.UserService import UserService
from forms import SignUpForm, LoginForm, AddPropertyForm, RentPropertyForm, GetPropertyForm

import datetime
import uuid


app = Flask(__name__)
app.secret_key = "angeloproject"  # can also be set via app.config['SECRET_KEY'] = your string 
db = DatabaseConnection()
#userService = UserService()

@app.route("/")
def hello():
    return "<h1>Welcome to the main page, the defualt page should be /login</h1>"

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    users = db.findAll("users")
    if False:   # REPLACE WITH: if email and password in database
        flash('Login Successful!', 'success')
        return redirect(url_for('properties'))
    elif "submit" in form:
        flash('Login Unsuccessful', 'danger')
    return render_template("login.html", form=form)

@app.route("/signUp", methods=['GET', 'POST'])  # alllows the page to accept get and post requests
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        document = {
            "username": request.form["username"],
            "email": request.form["email"],
            "password": request.form["username"]
        }
        db.insert("users", document)
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for('properties'))
    return render_template("signUp.html", form=form)

@app.route("/properties")
def getproperties():
    form = GetPropertyForm()
    properties = db.findMany("properties", {"rented": False})
    return render_template("properties.html", properties=properties)

@app.route("/propertyPage")
def propertypage():
    property = db.findOne("properties", {})
    return render_template("propertyPage.html", property=property)

@app.route("/rentProperty")
def rentproperty():
    form = RentPropertyForm()
    if form.validate_on_submit():
        query = {
            "rented": True
        }
        #"_id": request.form["property_id"]
        db.update("properties", {}, query)
        flash("Property Rented!", 'success')
        return redirect(url_for('properties'))
    return render_template("rentProperty.html", form=form)

@app.route("/vendorMode")
def vendormode():
    form = GetPropertyForm()
    properties = db.findMany("properties", {"rented": False})
    return render_template("vendorMode.html", properties=properties)

@app.route("/addProperty", methods=['GET', 'POST'])
def addproperty():
    form = AddPropertyForm()
    if form.validate_on_submit():
        document = {
            "name": request.form["name"],
            "location": request.form["location"],
            "bedrooms": request.form["bedrooms"],
            "price": request.form["price"],
            "image_url": request.form["image_url"],
            "description": request.form["description"],
            "rented": False,
        }
        db.insert("properties", document)
        #flash(f"{form.name.data} is now available for rent!")
        #return redirect(url_for('vendorMode'))
    return render_template("addProperty.html", form=form)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
    
