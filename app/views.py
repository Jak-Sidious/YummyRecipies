from flask import *
from flask_wtf import FlaskForm
from app import app
from app.models.user import User



@app.route('/', methods=('GET', 'POST'))
def signup():
    if request.method == 'POST':
        name = request.form['uname']
        password = request.form['password']
        used = User(name, password)
        return render_template('signin.html', used=used)
    return render_template('signup.html')


@app.route('/index')
def index():
    return "Hello, World!"

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     '''Landing encouraging user to login'''
#     if 'username' in session:
#         username = session['username']
#         password = session['password']
#         return 'Logged in as ' + username + ' with password ' + password +'<br>' + \
#          "<b><a href = '/logout'>click here to log out</a></b>"
#     return "You are not logged in <br><a href = '/app/templates/signup'></b>" + \
#       "click here to create account in</b></a>"

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     '''page to facilitate creating of accounts'''
#     if request.method == 'POST':
#         session['username'] = request.form['uname']
#         session['password'] = request.form['password']
#         user = User(session['username'], session['password'])
#         Used[session['username']] = user
#         return redirect(url_for('signin'))
#     return render_template('signup.html')

# 	# Used[session['username']].(class methid goes here)

# @app.route('/signin', methods=['GET', 'POST'])
# def signin():
#     '''Route to sign in users'''
#     if request.method == 'POST':
#         siginname = request.form['uname']
#         signinpass = request.form['psw']
#         sign[siginname] = signinpass
#         if Used[session['username']].username == siginname and Used[session['username']].password == signinpass:
#             return redirect(url_for('home'))
#     return render_template('signin.html')

# @app.route('/home')
# def home():
#     '''renders the landing page for all users to see
# 	'''
#     return render_template('home.html')

# @app.route('/categoryCreation', methods=['GET', 'POST'])
# def catcreate():
#     ''' renders the form used to create the category'''
#     if request.method == 'POST':
#         catname = request.form['name']
#         catdesc = request.form['description']
#         categoryname[session['username']] = catname
#         categorydesc[session['username']] = catdesc
#         Used[session['username']].categorycreate(categoryname[session['username']],
# 		                                               categorydesc[session['username']])
#         listing = Used[session['username']].categorycreate(categoryname[session['username']],
#                                                            categorydesc[session['username']])
#         all_listings = list(listing.values())
#         return render_template('categories.html', all_listings=all_listings)
#     return render_template('catcreate.html')

# @app.route('/categories')
# def ccatlisting():
#     '''List all the categories within the app'''
#     return render_template('categories.html')

# @app.route('/view_category', methods=['GET', 'POST'])
# def view_category():
#     '''View recipies attached to a particular category'''
#     Used[session['username']].view_categories(categoryname[session['username']])
#     cat = Used[session['username']].view_categories(categoryname[session['username']])
#     # all_listings = list(cat.values())
#     if cat is None:
#         return render_template('catrecipiecreate.html')
#     return render_template('categories.html')
# 	# this is where you call the create recipie function
# 	# return

# @app.route('/edit_category', methods=['GET', 'POST'])
# def edit_category():
#     '''  edit any recipies attached to a particular category'''
#     all_categories = Used[session['username']].categories

#     if request.method == "POST":
#         catdesc = request.form['catname']
#         editdesc = request.form['description']
#         if catdesc not in all_categories:
#             current_categories = Used[session['username']].categories
#             del current_categories[categoryname[session['username']]]
#             all_categories = Used[session['username']].categorycreate(catdesc, editdesc)
#             all_listings = list(all_categories.values())
#             return render_template('categories.html', all_listings=all_listings)
#         else:
#             Used[session['username']].edit_category(catdesc, editdesc)
#             return render_template('categories.html', all_listings=all_listings)  
#     return render_template('editcategory.html')

# @app.route('/delete_category', methods=['GET', 'POST'])
# def delete_category():
#     ''' delete any categories with or without recipes'''
#     if request.method == "POST":
#         # Used[session['username']].delete_category(categoryname[session['username']])
#         deletor = Used[session['username']].delete_category(categoryname[session['username']])
#         all_listings = list(deletor.values())
#         return render_template('categories.html', all_listings=all_listings)
#     return render_template('deletecategory.html')

# #add functionality for recipies



# @app.route('/create_recipie', methods=['GET', 'POST'])
# def create_category_recipie():
#     if request.method == 'POST':
#         cat_name = categoryname[session['username']]
#         recipie_name = request.form['recipiename']
#         ingridients = request.form['ingird']
#         Used[session['username']].create_recipe(cat_name, recipie_name, ingridients)
#         recs = Used[session['username']].create_recipe(cat_name, recipie_name, ingridients)
#         all_recs = list(recs.values())
#         return render_template('showrecipie.html', all_recs=all_recs)
#     return render_template('recipies.html')

# # @app.route('/<category_name>/edit_recipie', methods=['GET', 'POST'])
# # def edit_category_recipie(category_nam)




# @app.route('/logout')
# def logout():
#     '''Remove the session username and password if they are there'''
#     session.pop('username', None)
#     session.pop('password', None)
#     return redirect(url_for('index'))