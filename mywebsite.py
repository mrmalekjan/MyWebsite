from flask import Flask, request, render_template, session, redirect, url_for, send_from_directory, jsonify
#from markupsafe import escape
import os

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = os.urandom(12)
password='1'

@app.route("/")
@app.route("/home")
def home(sub_page="home_subform.html"):

    button_id = request.args.get('button_id')
    if 'username' in session:
        user_authorized = True
        if button_id == '2':
            sub_page = 'resume_form.html'
    else:
        user_authorized = False

    if button_id == '1':
        sub_page = 'contact.html'
    

    return render_template('home.html', user_authorized=user_authorized, sub_page=sub_page)

@app.route("/login", methods=['GET','POST'])
def login(wrong_log=""):
    if 'username' in request.form:
        if request.method == 'POST' and request.form['password']==password:
            session['username'] = request.form['username']
            return redirect('/home')
        else:
            wrong_log="Wrong username or password! Try again!"
    return render_template('login_form.html', wrong_log=wrong_log)

@app.route("/resume", methods=['GET', 'POST'])
def resume():
    return render_template("resume_form.html")

@app.route("/home_subform")
def homesubform():
    return render_template("home_subform.html")

@app.route("/test", methods=['GET','POST'])
def test():
    test_name='ali'
    if 'your_name' in request.form:
        test_name=request.form['your_name']

    if 'filename' in request.files:
        f = request.files['filename']
        f.save(os.path.join(os.path.dirname(__file__),'uploads',f.filename))

    return  render_template('test.html', test_name=test_name)

@app.errorhandler(404)
def error_404(error):
    return render_template('error_404.html')

@app.route('/uploads/<path:name>')
def download_file(name):
    return send_from_directory(app.static_folder, os.path.join('uploads',"testtext.txt"))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/home')

@app.route('/contact')
def contact():
    return render_template('contact.html')

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

app.run(host='0.0.0.0', port=35000)