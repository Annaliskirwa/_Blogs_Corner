from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,TextAreaField, SubmitField,ValidationError
from wtforms.validators import Required,Email
from flask_login import current_user
from ..models import User

class UpdateProfile(FlaskForm):
    username = StringField('Your username here..', validators=[Required()])
    email = StringField('Your email address here..', validators=[Required(),Email()])
    bio = TextAreaField('Tell us about you here..',validators = [Required()])
    profile_picture = FileField('profile picture', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')