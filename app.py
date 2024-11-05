# flask_ngrok_example.py
from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run

@app.route("/")
def index():
    return "<h1>Welcome</h1>  <p>Under construction</p>"

@app.route("/about")
def about():
    return "This is a python web application built using Flask";

@app.route("/product/<name>")
def product(name):
    return "<h3>Product</h3> <p>" + name + "</p>"

@app.route("/product/<name>/<price>")
def productPrice(name, price):
    return "<h3>Product</h3> <p>" + name + " costs: " + price + "</p>"
if __name__ == '__main__':
    app.run()  # If address is in use, may need to terminate other sessions:
               # Runtime > Manage Sessions > Terminate Other Sessions