# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    return render_template("result.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)



# index.html
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Flask Form</title>
# </head>
# <body>
#     <h1>Enter your name</h1>
#     <form action="/result" method="POST">
#         <input type="text" name="name" placeholder="Your Name" required>
#         <button type="submit">Submit</button>
#     </form>
# </body>
# </html>



# result.html
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Result</title>
# </head>
# <body>
#     <h1>Hello, {{ name }}!</h1>
# </body>
# </html>