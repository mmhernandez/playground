from flask_app import app
from flask import render_template


@app.route("/")
def homepage():
    render_template("home.html")

@app.route("/memory_game")
def memory_game():
    render_template("memory_game.html")