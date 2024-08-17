from flask import Flask, request, render_template, session, redirect, url_for, send_from_directory
#from markupsafe import escape
import os

#os.system('flask run --host=0.0.0.0')

app = Flask(__name__, static_folder='static')
app.secret_key = os.urandom(12)
password='1'

@app.route("/")
@app.route("/home")
def home():
    if 'username' in session:
        return redirect('/resume')
    return redirect('/login')

@app.route("/login", methods=['GET','POST'])
def login(wrong_log=""):
    if 'username' in request.form:
        if request.method == 'POST' and request.form['password']==password:
            session['username'] = request.form['username']
            return redirect('/resume')
        else:
            wrong_log="Wrong username or password! Try again!"
    return render_template('login_form.html', wrong_log=wrong_log)

@app.route("/resume")
def resume():
    return render_template('resume_form.html')

@app.route("/test", methods=['GET','post'])
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

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.run()