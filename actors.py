"This actors.py file contains the player and the enemy. This includes the movements , collision and all functions for the moving game characters"

import turtle  
from cons import cel_size, scr_wid, scr_hi, player_move_speed 

class actor(turtle.Turtle):

    def __init__(self) ->None:
        super(). __init__()
        self.hideturtle()
        self.penup()
        self.speed(speed = 0)


class Player(actor):

    def __init__(self) ->None:
        super(). __init__()
        self.showturtle()
        self.shape(name = "circle")
        self.shapesize(1.4)
        self.pencolor("white")
        self.fillcolor("yellow")
        self.state = "stop"
        self.move_speed = player_move_speed
        self.lives = 3
        self.score = 0


    def move(self) ->None:
        if self.state != "stop":
            self.forward(distance = self.move_speed)

            if round(number = self.ycor()) > scr_hi / 2 - 2 * cel_size:
                self.sety(y = scr_hi / 2)
            elif round(number = self.ycor()) < -scr_hi / 2:
                self.sety(y = scr_hi / 2 - 2 * cel_size)
            elif round(number = self.xcor()) < -scr_wid / 2:
                self.setx(x = scr_wid / 2)
            elif round(number = self.xcor()) > scr_wid / 2:
                self.setx(x = -scr_wid / 2)


    def turn_right(self) ->None:
        self.setheading(to_angle= 0)
        self.state = "move"

    def turn_left(self) ->None:
        self.setheading(to_angle= 180)
        self.state = "move"

    def turn_up(self) ->None:
        self.setheading(to_angle= 90)
        self.state = "move"

    def turn_down(self) ->None:
        self.setheading(to_angle= 270)
        self.state = "move"
    