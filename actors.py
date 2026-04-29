"""Actors: Player + Ghosts with fast movement and optimized AI"""

import turtle
from collections import deque
import heapq

from cons import cel_size, scr_wid, scr_hi


# =========================
# Base Actor
# =========================
class actor(turtle.Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)

    def get_heading(self):
        return round(self.heading())


# =========================
# Player
# =========================
class Player(actor):

    def __init__(self, walls):
        super().__init__()
        self.showturtle()
        self.shape("circle")
        self.shapesize(1.4)
        self.fillcolor("yellow")

        self.state = "stop"
        self.move_speed = 10   # 🔥 faster
        self.walls = walls

    def move(self):
        if self.state != "stop":
            self.forward(self.move_speed)

            # wrapping
            if self.xcor() > scr_wid / 2:
                self.setx(-scr_wid / 2)
            elif self.xcor() < -scr_wid / 2:
                self.setx(scr_wid / 2)

            if self.ycor() > scr_hi / 2:
                self.sety(-scr_hi / 2)
            elif self.ycor() < -scr_hi / 2:
                self.sety(scr_hi / 2)

    def check_wall_collision(self):
        for x, y in self.walls:
            if self.distance(x, y) < cel_size / 2:
                self.backward(self.move_speed)

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
# Ghosts
# =========================
class Ghost(actor):

    def __init__(self, walls, algorithm="bfs"):
        super().__init__()
        self.showturtle()
        self.shape("circle")

        self.walls = walls
        self.algorithm = algorithm

        self.path = []
        self.counter = 0
        self.move_speed = 6   # 🔥 smooth speed

    def to_grid(self, x, y):
        return (round(x), round(y))

    def get_neighbors(self, pos):
        x, y = pos
        steps = [(30, 0), (-30, 0), (0, 30), (0, -30)]
        result = []

        for dx, dy in steps:
            nxt = (x + dx, y + dy)
            if nxt not in self.walls:
                result.append(nxt)

        return result

    # BFS
    def bfs(self, start, goal):
        queue = deque([(start, [])])
        visited = set()

        while queue:
            current, path = queue.popleft()

            if current == goal:
                return path

            if current in visited:
                continue

            visited.add(current)

            for n in self.get_neighbors(current):
                queue.append((n, path + [n]))

        return []

    # A*
    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def astar(self, start, goal):
        pq = [(0, start, [])]
        visited = set()

        while pq:
            cost, current, path = heapq.heappop(pq)

            if current == goal:
                return path

            if current in visited:
                continue

            visited.add(current)

            for n in self.get_neighbors(current):
                new_cost = len(path) + 1
                priority = new_cost + self.heuristic(n, goal)
                heapq.heappush(pq, (priority, n, path + [n]))

        return []

    # 🔥 FAST MOVE
    def move(self, player_pos):
        self.counter += 1

        # recalc path every 10 frames (faster reaction)
        if self.counter % 10 == 0:
            start = self.to_grid(self.xcor(), self.ycor())
            goal = self.to_grid(player_pos[0], player_pos[1])

            if self.algorithm == "bfs":
                self.path = self.bfs(start, goal)
            else:
                self.path = self.astar(start, goal)

        # smooth movement instead of teleport
        if self.path:
            target = self.path[0]

            dx = target[0] - self.xcor()
            dy = target[1] - self.ycor()

            dist = (dx**2 + dy**2) ** 0.5

            if dist < self.move_speed:
                self.goto(target)
                self.path.pop(0)
            else:
                self.setx(self.xcor() + self.move_speed * dx / dist)
                self.sety(self.ycor() + self.move_speed * dy / dist)

                
       
       
            

        

        
