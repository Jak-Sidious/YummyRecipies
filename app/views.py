from flask import *
from app import app
from app.models.user import User


userdata = {}
all_listings = []
category_store = {}
@app.route('/', methods=('GET', 'POST'))
def signup():
    if request.method == 'POST':
        name = request.form['uname']
        password = request.form['password']
        used = User(name, password)
        userdata[name] = used
        #user_data.append(used)
        return redirect(url_for('signin', name=name, ))
    return render_template('signup.html')

@app.route('/home')
@app.route('/<name>/home')
def home(name):
    '''renders the landing page for all users to see
	'''
    if name in userdata.keys():
        print(userdata[name].username)
    return render_template('home.html', name=name)

# @app.route('/signin')
@app.route('/<name>/signin', methods=('GET', 'POST'))
def signin(name=None):
    if name in userdata.keys():
        # print(userdata)
        # print(userdata[name].username, "...........")
        # print(userdata[name].password, "............")
        print (userdata[name])
        if request.method == 'POST':
            name = request.form['uname']
            pssword = request.form['password']
            # Test print to ensure user_data is accesible
            # print (userdata)
            # print(userdata[name].username, "...........")
            # print(userdata[name].password, "............")
            if name == userdata[name].username and pssword == userdata[name].password:
                return redirect(url_for('home', name=name))
    return render_template('signin.html')
        
# @app.route('/categories')
@app.route('/<name>/categories')
def ccatlisting(name):
    '''List all the categories within the app'''
    return render_template('categories.html', name=name)

# @app.route('/categoryCreation', methods=['GET', 'POST'])
# @app.route('/<name>/categoryCreation', methods=['GET', 'POST'])
# def catcreate(name):
#     ''' renders the form used to create the category'''
#     # catuse = User(userdata[name].username, userdata[name].password)
#     if name in userdata.keys():
#         if request.method == 'POST':
#             catname = request.form['name']
#             catdesc = request.form['description']
#             # 
#             # print (catuse)
#             # catuse.categorycreate(catname, catdesc)
#             # all_listings[catuse.categories[]]
#             # return redirect(url_for('categories', all_listings=all_listings))
#             if catname
#     return render_template('catcreate.html', name=name)

# @app.route('/edit_category')
# @app.route('/<name>/edit_category', methods=['GET', 'POST'])
# def edit_category(name):
#     '''edit any recipies existingg in the applications'''
#     if name in userdata.keys():
#         catuse = User(userdata[name].username, userdata[name].password)
#         present_items = catuse.categories
        
#         if request.method == 'POST':
#             catdesc = request.form['catname']
#             editdesc = request.form['description']
#             if catdesc not in present_items:
#                 # current_categories = catuse.categories
#                 # del current_categories[userdata[name].username]
#                 # present_items[userdata[name].username]
#                 # catuse.categorycreate(catdesc, editdesc)
#                 # all_listings.append(catuse.categorycreate(catdesc, editdesc))
#                 # return redirect(url_for('categories.html', all_lisings=all_listings))
#             else:
#                 catuse.edit_category(catdesc, editdesc)
#                 return redirect(url_for('categories.html', all_lisings=all_listings))
#     return render_template('edit_category.html', name=name)
# @app.route('/<name>/edit_category', methods=['GET', 'POST'])
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
