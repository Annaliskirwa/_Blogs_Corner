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
    submit = SubmitField('Update your profile')

    def validate_email(self,email):
        if email.data != current_user.email:
            if User.query.filter_by(email = email.data).first():
                raise ValidationError("Ooops!That email has already been taken")


    def validate_username(self, username):
        if username.data != current_user.username:
            if User.query.filter_by(username = username.data).first():
                raise ValidationError("Ooops!That username has already been taken")

class CreateBlog(FlaskForm):
    title = StringField('Your blog title here..',validators=[Required()])
    content = TextAreaField('Your blog content here..',validators=[Required()])
    submit = SubmitField('Post your blog')