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

class RegForm(FlaskForm):
    username = StringField('Enter here your username..', validators=[Required(), Length(min=4, max=20)])
    email = StringField('Enter here your email address..', validators=[Required(),Email()])
    password = PasswordField('Enter here your email password..',validators = [Required(), EqualTo('password_confirm',message = 'Your passwords should match')])
    password_confirm = PasswordField('Confirm your password above..',validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError(message="Ooops!That email has already been taken..")
    
