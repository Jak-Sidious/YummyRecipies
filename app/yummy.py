from flask import *
from models.user import User


app = Flask(__name__)
Use = {}
sign = {}

@app.route('/', methods=['GET', 'POST'])
def user():
    '''Route to signup page'''
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        if username and password:
            a = User(username, password)
            Use[username] = password
            return redirect(url_for('signin'))
    return render_template("signup.html")

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    '''Route to sign in users'''
    if request.method == 'POST':
        siginname = request.form['uname']
        signinpass = request.form['psw']
        sign[siginname] = signinpass
        if Use == sign:
            return redirect(url_for('dash'))
    return render_template('signin.html')

@app.route('/home')
def home():
    '''renders the landing page for all users to see
	'''
    return render_template('home.html')

@app.route('/add')
def add():
    '''renders the add recipie page for a user
    '''
    return render_template('add.html')

@app.route('/view')
def view():
    '''renders the view recipies page
    '''
    return render_template('view.html')

@app.route('/update')
def update():
    '''renders the update recipies page
    '''
    return render_template('update.html')

@app.route('/delete')
def delete():
	'''renders the delete recipies page
	'''
	return render_template('delete.html')


if __name__ == "__main__":
	app.run(debug=True)
