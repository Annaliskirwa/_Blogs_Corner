from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo, Length
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
    username = StringField('Enter here your username..',validators=[Required()])
    password = PasswordField('Enter here your password..',validators=[Required()])
    remember = BooleanField('Remember Me!')
    submit = SubmitField('Login')