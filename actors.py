"""This actors.py file contains the player and the enemy (ghosts).
Includes movement, collision, and optimized AI (BFS & A*)."""

import turtle
import math
from collections import deque
import heapq

from cons import cel_size, scr_wid, scr_hi, player_move_speed


# =========================
# Base Actor Class
# =========================
class actor(turtle.Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)

    def get_heading(self) -> int:
        return round(self.heading())


# =========================
# Player (Pacman)
# =========================
class Player(actor):

    def __init__(self, walls) -> None:
        super().__init__()
        self.showturtle()
        self.shape("circle")
        self.shapesize(1.4)
        self.pencolor("white")
        self.fillcolor("yellow")

        self.state = "stop"
        self.move_speed = player_move_speed
        self.lives = 3
        self.score = 0
        self.walls = walls

    def move(self) -> None:
        if self.state != "stop":
            self.forward(self.move_speed)

            # screen wrapping
            if round(self.ycor()) > scr_hi / 2 - 2 * cel_size:
                self.sety(scr_hi / 2)
            elif round(self.ycor()) < -scr_hi / 2:
                self.sety(scr_hi / 2 - 2 * cel_size)
            elif round(self.xcor()) < -scr_wid / 2:
                self.setx(scr_wid / 2)
            elif round(self.xcor()) > scr_wid / 2:
                self.setx(-scr_wid / 2)

    def check_wall_collision(self):
        round_x = round(self.xcor())
        round_y = round(self.ycor())
        heading = self.get_heading()
        half_cell = round(cel_size / 2)

        for x, y in self.walls:
            dx = round_x - x
            dy = round_y - y

            if heading == 0:
                if -half_cell < dx + half_cell < half_cell and -half_cell <= dy <= half_cell:
                    self.setx(x - cel_size)
                    self.state = "stop"

            elif heading == 180:
                if -half_cell < dx - half_cell < half_cell and -half_cell <= dy <= half_cell:
                    self.setx(x + cel_size)
                    self.state = "stop"

            elif heading == 90:
                if -half_cell <= dx <= half_cell and -half_cell < dy + half_cell < half_cell:
                    self.sety(y - cel_size)
                    self.state = "stop"

            elif heading == 270:
                if -half_cell <= dx <= half_cell and -half_cell < dy - half_cell < half_cell:
                    self.sety(y + cel_size)
                    self.state = "stop"

    def turn_right(self):
        self.setheading(0)
        self.state = "move"

    def turn_left(self):
        self.setheading(180)
        self.state = "move"

    def turn_up(self):
        self.setheading(90)
        self.state = "move"

    def turn_down(self):
        self.setheading(270)
        self.state = "move"


# =========================
# Ghosts (Optimized AI)
# =========================
class Ghost(actor):

    def __init__(self, walls, algorithm="bfs"):
        super().__init__()
        self.showturtle()
        self.move_speed = 8
        self.shape("circle")
        self.shapesize(1.2)
        self.color("red")

        self.walls = set(walls)
        self.algorithm = algorithm

        self.counter = 0
        self.path = []  # store computed path

    def check_wall_collision(self):
        round_x = round(self.xcor())
        round_y = round(self.ycor())
        heading = self.get_heading()
        half_cell = round(cel_size / 2)

        for x, y in self.walls:
            dx = round_x - x
            dy = round_y - y

            if heading == 0:
                if -half_cell < dx + half_cell < half_cell and -half_cell <= dy <= half_cell:
                    self.setx(x - cel_size)

            elif heading == 180:
                if -half_cell < dx - half_cell < half_cell and -half_cell <= dy <= half_cell:
                    self.setx(x + cel_size)

            elif heading == 90:
                if -half_cell <= dx <= half_cell and -half_cell < dy + half_cell < half_cell:
                    self.sety(y - cel_size)

            elif heading == 270:
                if -half_cell <= dx <= half_cell and -half_cell < dy - half_cell < half_cell:
                    self.sety(y + cel_size)
    def to_grid(self, x, y):
        return (
        round(x / cel_size) * cel_size,
        round(y / cel_size) * cel_size
        )

    def get_neighbors(self, pos):
        x, y = pos
        step = cel_size

        steps = [(step, 0), (-step, 0), (0, step), (0, -step)]
        neighbors = []

        for dx, dy in steps:
            new = (x + dx, y + dy)

            # snap to grid to avoid mismatch
            new = (
                round(new[0] / cel_size) * cel_size,
                round(new[1] / cel_size) * cel_size
            )

            if new not in self.walls and -500 < new[0] < 500 and -500 < new[1] < 500:
                neighbors.append(new)

        return neighbors
        
    # =========================
    # BFS
    # =========================
    def bfs(self, start, goal):
        queue = deque()
        queue.append((start, []))
        visited = set()

        while queue:
            current, path = queue.popleft()

            if current == goal:
                return path

            if current in visited:
                continue

            visited.add(current)

            for neighbor in self.get_neighbors(current):
                queue.append((neighbor, path + [neighbor]))

        return []

    # =========================
    # A*
    # =========================
    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def astar(self, start, goal):
        open_list = []
        heapq.heappush(open_list, (0, start, []))
        visited = set()

        while open_list:
            cost, current, path = heapq.heappop(open_list)

            if current == goal:
                return path

            if current in visited:
                continue

            visited.add(current)

            for neighbor in self.get_neighbors(current):
                new_cost = len(path) + 1
                priority = new_cost + self.heuristic(neighbor, goal)
                heapq.heappush(open_list, (priority, neighbor, path + [neighbor]))

        return []

    # =========================
    # OPTIMIZED MOVE
    # =========================
    def move(self, player_pos):
        self.counter += 1

        # Recalculate path every few frames
        if self.counter % 10 == 0 or not self.path:
            start = self.to_grid(self.xcor(), self.ycor())
            goal = self.to_grid(player_pos[0], player_pos[1])

            if self.algorithm == "bfs":
                self.path = self.bfs(start, goal)
            else:
                self.path = self.astar(start, goal)

        # Move one tile at a time
        if self.path and self.counter % 4 == 0:
            next_step = self.path[0]  # DON'T pop yet

            # snap to grid (important safety)
            next_step = (
                round(next_step[0] / cel_size) * cel_size,
                round(next_step[1] / cel_size) * cel_size
            )

            # only move if it's NOT a wall
            if next_step not in self.walls:
                self.goto(next_step)
                self.path.pop(0)
            else:
                # path is invalid → recalculate
                self.path = []
