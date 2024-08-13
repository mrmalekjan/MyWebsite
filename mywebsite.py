from flask import Flask, request, render_template, session, redirect
import os

#os.system('flask run --host=0.0.0.0')

app = Flask(__name__)
app.secret_key = os.urandom(12)

@app.route("/")
@app.route("/home")
def home():
    if 'username' in session:
        return redirect('/resume')
    return redirect('/login')

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['username']==request.form['password']:
            session['username'] = request.form['username']
            return redirect('/resume')
        else:
            return render_template('login_form.html')
    return render_template('login_form.html')

@app.route("/resume")
def resume():
    return render_template('resume_form.html')

app.run()