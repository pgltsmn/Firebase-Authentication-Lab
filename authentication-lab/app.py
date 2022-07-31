from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {
  "apiKey": "AIzaSyDCcDiFKzdCL7HPKJdpGzckTWHxDhZhcUo",
  "authDomain": "omgsmthcool.firebaseapp.com",
  "projectId": "omgsmthcool",
  "storageBucket": "omgsmthcool.appspot.com",
  "messagingSenderId": "983001006387",
  "appId": "1:983001006387:web:34a15c3ce78c79543ebe46",
  "measurementId": "G-947TPG9FTR",
  "databaseURL": ""
};

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/')
def gotosmth():
    return render_template('home.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
        except:
            error = "smth went wrong"
    return render_template('signin.html')



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect (url_for('add_tweet'))
        except:
            error = "smth went wrong"

    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    # if method = "POST":
    #     ogin_session['user'] = None
    #     auth.current_user = None
    #     return redirect(url_for('home.html'))
    return render_template("add_tweet.html")

# @app.route('/signout')
# def signout():
#     login_session['user'] = None
#     auth.current_user = None
#     return redirect(url_for('home.html'))
# return render_template('add_tweet.html')




if __name__ == '__main__':
    app.run(debug=True)