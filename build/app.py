from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/pricing")
def pricing():
    return render_template('pricing.html')

@app.route("/booking")
def booking():
    return render_template('booking.html')

@app.route("/shop")
def shop():
    return render_template('shop.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')