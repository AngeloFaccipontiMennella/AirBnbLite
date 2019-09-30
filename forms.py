from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DecimalField, IntegerField, FileField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange

class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=1, max=25)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=40)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=8, max=40), EqualTo("password")])
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=40)])
    #remember field uses a secure cookie to stay logged in
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")

class RentPropertyForm(FlaskForm):
    submit = SubmitField("Rent House")

class AddPropertyForm(FlaskForm):
    name = StringField("Property Name", validators=[DataRequired(), Length(min=1, max=60)])
    location = StringField("Location", validators=[DataRequired(), Length(min=1, max=30)])
    bedrooms = IntegerField("Number of Bedrooms", validators=[DataRequired(), NumberRange(min=1, max=20)])
    price = DecimalField("Price per Night", validators=[DataRequired(), NumberRange(min=1.00)])
    image_url =  StringField("Image", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired(), Length(max=800)])
    submit = SubmitField("Post")

class GetPropertyForm(FlaskForm):
    property_id = HiddenField("property_id")
