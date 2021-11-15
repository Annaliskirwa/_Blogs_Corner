from flask import render_template,redirect,url_for,abort,request,flash
from app.main import main
from app.models import User,Blog,Comment,Subscriber
from .forms import UpdateProfile,CreateBlog
from .. import db
from app.requests import get_quotes
from flask_login import login_required,current_user
from ..email import mail_message
import secrets
import os
from PIL import Image
import markdown2  