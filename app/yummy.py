from flask import *
from models.user import User


app = Flask(__name__)
app.secret_key = 'testing'
Used = {}
sign = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    '''Landing encouraging user to login'''
    if 'username' in session:
        username = session['username']
        password = session['password']
        return 'Logged in as ' + username + ' with password ' + password +'<br>' + \
         "<b><a href = '/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href = '/signup'></b>" + \
      "click here to create account in</b></a>"

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    '''page to facilitate creating of accounts'''
    if request.method == 'POST':
        session['username'] = request.form['uname']
        session['password'] = request.form['password']
        user = User(session['username'], session['password'])
        Used[session['username']] = user
        flash(session['username'])
        return redirect(url_for('signin'))
    return render_template('signup.html')

	# Used[session['username']].(class methid goes here)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    '''Route to sign in users'''
    if request.method == 'POST':
        siginname = request.form['uname']
        signinpass = request.form['psw']
        sign[siginname] = signinpass
        if Used == sign:
            return redirect(url_for('dash'))
    return render_template('signin.html')

@app.route('/home')
def home():
    '''renders the landing page for all users to see
	'''
    return render_template('home.html')

@app.route('/categoryCreation')
def catcreate():
    ''' renders the form used to create the category'''
    return render_template('catcreate.html')

@app.route('/logout')
def logout():
    '''Remove the session username and password if they are there'''
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
