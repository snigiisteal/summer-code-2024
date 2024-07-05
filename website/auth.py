from flask import Blueprint,render_template,url_for
from .models import insert_into_database

auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/auth_success')
def auth_success():
    print("Success")
    insert_into_database(id=1,email='snigdha.nallathiga@gmail.com',name='Snigdha',steps=205,move_mins=24)
    return render_template('dash.html',steps_count=10000)
