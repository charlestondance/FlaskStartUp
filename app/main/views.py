from flask import render_template,redirect, request, url_for, flash
from . import main
from ..models import ConsumableDB, User, Role, Permission
from .. import db
from flask.ext.login import login_required, current_user
from ..decorators import admin_required, permission_required
from werkzeug import secure_filename

@main.route('/')
def index():
    return render_template('index.html', Permission=Permission)



