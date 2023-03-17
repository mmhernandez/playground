from flask_app import app  
from flask import render_template
import random
import turtle
from freegames import path


@app.route("/memory_game")
def memory_game():
    car = path('./static/images/mario_luigi.jpgs') 
    tiles = list(range(32)) * 2

    state = {'mark': None} 
    hide = [True] * 64 
    print(tiles)

    def square(x, y): 
        turtle.up()
        turtle.goto(x, y)
        turtle.down() 
        turtle.color('black', 'white')
        turtle.begin_fill() 
        for count in range(4):
            turtle.forward(50)
            turtle.left(90) 
        turtle.end_fill()

    def index(x, y):
        return int((x + 200) // 50 + ((y + 200) // 50) * 8)
    def xy(count):
        return (count % 8) * 50 - 200, (count // 8) * 50 - 200

    def tap(x, y):
        spot = index(x, y)
        mark = state['mark']
        if mark is None or mark == spot or tiles[mark] != tiles[spot]:
            state['mark'] = spot
        else:
            hide[spot] = False
            hide[mark] = False
            state['mark'] = None

    def draw():
        turtle.clear()
        turtle.goto(0, 0)
        turtle.shape(car)
        turtle.stamp()
        for count in range(64):
            if hide[count]:
                x, y = xy(count)
                square(x, y)
        mark = state['mark']

        if mark is not None and hide[mark]:
            x, y = xy(mark)
            turtle.up()
            turtle.goto(x + 2, y)
            turtle.color('black')
            turtle.write(tiles[mark], font=('Arial', 30, 'normal'))
        turtle.update()
        turtle.ontimer(draw, 100)

    turtle.shuffle(tiles)
    turtle.addshape(car)
    turtle.hideturtle()
    turtle.tracer(False)
    turtle.onscreenclick(tap)
    draw()
    turtle.done()
    
    return render_template("memory_game.html")