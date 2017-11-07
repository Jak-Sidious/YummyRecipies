from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template("signin.html")

@app.route('/signup')
def user():
    return render_template("signup.html")

@app.route('/dash')
def dash():
    return render_template("dashboard.html")



if __name__ == "__main__":
	app.run(debug=True)