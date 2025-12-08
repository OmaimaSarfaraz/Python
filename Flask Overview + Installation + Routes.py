from flask import Flask

app = Flask(__name__)

# Root route
@app.route('/')
def home():
    return "Hello, Flask!"

# About route
@app.route('/about')
def about():
    return "This is the About Page"

# Users route with parameter
@app.route('/user/<username>')
def user(username):
    return f"Hello, {username}!"

if __name__ == "__main__":
    app.run(debug=True)