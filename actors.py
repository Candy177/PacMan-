"This actors.py file contains the player and the enemy. This includes the movements , collision and all functions for the moving game characters"

import turtle  
from cons import cel_size, scr_wid, scr_hi, player_move_speed 

class actor(turtle.Turtle):

    def __init__(self) -> None:
        super(). __init__()
        self.hideturtle()
        self.penup()
        self.speed(speed = 0)
    
    
    def get_heading(self) -> int:
        return round(self.heading())


class Player(actor):

    def __init__(self, walls) ->None:
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
        self.walls = walls


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

    
    def check_wall_collision(self):
        round_x = round(self.xcor())
        round_y = round(self.ycor())
        heading = self.get_heading()
        half_cell = round(cel_size / 2)

        for x, y in self.walls:
            dx = round_x - x  #How far is pacman from wall x
            dy = round_y - y  #How far is pacman from wall y

            if heading == 0:  # Moving right
                if -half_cell < dx + half_cell < half_cell and -half_cell <= dy <= half_cell:
                    self.setx(x - cel_size)
                    self.state = "stop"
                elif -half_cell < dx + half_cell < half_cell and dy > half_cell and abs(dy) < cel_size:
                    self.sety(y + cel_size)
                elif -half_cell < dx + half_cell < half_cell and dy < -half_cell and abs(dy) < cel_size:
                    self.sety(y - cel_size)

            elif heading == 180:  # Moving left
                if -half_cell < dx - half_cell < half_cell and -half_cell <= dy <= half_cell:
                    self.setx(x + cel_size)
                    self.state = "stop"
                elif -half_cell < dx - half_cell < half_cell and dy > half_cell and abs(dy) < cel_size:
                    self.sety(y + cel_size)
                elif -half_cell < dx - half_cell < half_cell and dy < -half_cell and abs(dy) < cel_size:
                    self.sety(y - cel_size)

            elif heading == 90:  # Moving up
                if -half_cell <= dx <= half_cell and -half_cell < dy + half_cell < half_cell:
                    self.sety(y - cel_size)
                    self.state = "stop"
                elif dx > half_cell and abs(dx) < cel_size and -half_cell < dy + half_cell < half_cell:
                    self.setx(x + cel_size)
                elif dx < -half_cell and abs(dx) < cel_size and -half_cell < dy + half_cell < half_cell:
                    self.setx(x - cel_size)

            elif heading == 270:  # Moving down
                if -half_cell <= dx <= half_cell and -half_cell < dy - half_cell < half_cell:
                    self.sety(y + cel_size)
                    self.state = "stop"
                elif dx > half_cell and abs(dx) < cel_size and -half_cell < dy - half_cell < half_cell:
                    self.setx(x + cel_size)
                elif dx < -half_cell and abs(dx) < cel_size and -half_cell < dy - half_cell < half_cell:
                    self.setx(x - cel_size)


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
    