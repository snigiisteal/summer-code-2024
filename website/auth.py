from flask import Blueprint,render_template,url_for

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
    return render_template('dash.html')