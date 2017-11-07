from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/base')
def user():
    return render_template("base.html")


if __name__ == "__main__":
	app.run(debug=True)