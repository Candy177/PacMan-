import turtle

from mazes import calc_maze , maze_level_1

class Pen(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.walls, self.pellets, self.powerups= calc_maze(maze_lvl= maze_level_1)

class Wall(Pen):
    def __init__(self) ->None:
        super().__init__()
        self.shape("square")
        self.shapesize(1.2)
        self.pencolor("white")
        self.fillcolor("dodger blue")

    def draw(self) ->None:
        for x,y in self.walls:
            self.goto(x=x,y=y)
            self.stamp()

class Pellet(Pen):
    def __init__(self) ->None:
        super().__init__()
        self.shape("circle")
        self.shapesize(0.35,0.35)
        self.pencolor("white")
        self.fillcolor("gold")

    def draw(self) ->None:
        for x,y in self.pellets:
            self.goto(x=x,y=y)
            self.stamp()

class Powerup(Pen):
    def __init__(self) ->None:
        super().__init__()
        self.shape(name="circle")
        self.shapesize(0.8,0.8)
        self.pencolor("white")
        self.fillcolor("red")

    def draw(self) ->None:
        for x,y in self.powerups:
            self.goto(x=x,y=y)
            self.stamp()


