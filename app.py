from flask import Flask,request

app = Flask(__name__)


# Binding def index function with the url '/'.
# @ signifies a decorator - a way to wrap a function and modifying it's behaviour
@app.route('/')
def index():
    return 'This is Homepage'


@app.route('/about')
def about():
    return '<h1>About Me<h1>'


# Variables String Types
@app.route('/about/<username>')
def profile(username):
    return "<h2>Hey There. My name is  %s<h2>" % username


# Variables Integer Types
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "<h2>Post ID is %s<h2>" % post_id


# Get method and Post Method
# requires request library
@app.route('/default_request')
def default_request():
    return "Method used: %s" % request.method

# POST Method Check
# TO check the post method use POSTMAN app https://www.getpostman.com/downloads/
@app.route('/post_request', methods=['GET', 'POST'])
def post_request():
    if request.method == 'POST':
        return "Your are using post method"
    else:
        return "Your are using get method"


if __name__ == '__main__':
    app.run()
