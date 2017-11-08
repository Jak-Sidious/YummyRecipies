from flask import *
from models.user import User


app = Flask(__name__)
app.secret_key = 'caman'
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
        if Used[session['username']].username == siginname and Used[session['username']].password == signinpass:
            return redirect(url_for('home'))
    return render_template('signin.html')

@app.route('/home')
def home():
    '''renders the landing page for all users to see
	'''
    return render_template('home.html')

@app.route('/categoryCreation', methods=['GET', 'POST'])
def catcreate():
    ''' renders the form used to create the category'''
    if request.method == 'POST':
        catname = request.form['name']
        catdesc = request.form['description']
        Used[session['username']].categorycreate(catname, catdesc)
        listing = Used[session['username']].categorycreate(catname, catdesc)
        all_listings = list(listing.values())
        return render_template('categories.html', all_listings=all_listings)
    return render_template('catcreate.html')

@app.route('/categories', methods=['GET', 'POST'])
def catlisting():
	'''List all the categories within the app'''
	return render_template('categories.html')

@app.route('/view_category/<category_name>', methods=['GET', 'POST'])
def view_category(category_name):
    '''View recipies attached to a particular category'''
    cat = Used[session['username']].view_recipies(category_name)
    if cat is not None:
        return render_template('catrecipiecreate.html', category_name=category_name)
	# this is where you call the create recipie function

@app.route('/<category_name>/create_recipie', methods=['GET', 'POST'])
def create_category_recipie(category_name):
	if request.method == 'POST':
		cat_name = category_name
		recipie_name = request.form['recipiename']
		ingridients = request.form['ingird']
		Used[session['username']].create_recipe(cat_name, recipie_name, ingridients)
		return render_template('catrecipiecreate.html')


@app.route('/logout')
def logout():
    '''Remove the session username and password if they are there'''
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
