from flask_app import app
from flask import render_template


@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/memory_game")
def memory_game():
    return render_template("memory_game.html")