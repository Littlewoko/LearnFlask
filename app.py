# flask_ngrok_example.py
from flask import Flask, render_template, jsonify
from flask_ngrok import run_with_ngrok

app = Flask(__name__) #templates is default
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

@app.route("/template")
def template():
    return render_template('template.html')

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', name=username)

Lores = [
    {'id': 1, 'title': 'van helsing', 'image': 'https://media.newyorker.com/photos/5909544b6552fa0be682ca71/master/pass/lincoln-vampire.jpg'}, 
    {'id': 2, 'title': 'vampire', 'image': 'https://th-thumbnailer.cdn-si-edu.com/XxlgYLkrQNjgEGJs3B1ecOh8cVs=/800x600/filters:focal(278x186:279x187)/https://tf-cmsv2-smithsonianmag-media.s3.amazonaws.com/filer/51/58/515809d8-1e1c-44aa-ae26-4688598f38ce/untitled-1.jpg'}, 
]

@app.route('/api/lores')
def apiCourses():
    return jsonify(Lores)


@app.route("/lore")
def courses():
    return render_template("lore.html", lores=Lores)

if __name__ == '__main__':
    app.run()  # If address is in use, may need to terminate other sessions:
               # Runtime > Manage Sessions > Terminate Other Sessions