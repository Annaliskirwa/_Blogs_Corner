from flask import render_template,flash, request, redirect, url_for
from flask_login import login_user, logout_user,login_required
from app.auth import auth
from app.models import User
from .forms import RegForm,LoginForm
from ..email import mail_message