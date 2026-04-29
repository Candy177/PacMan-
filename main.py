"""entire game is here"""

import turtle
import random

from cons import scr_hi, scr_wid
from renderer import Wall, Pellet, Powerup
from actors import Player, Ghost


def init_screen() -> turtle.Screen:
    screen = turtle.Screen()
    screen.tracer(0)
    screen.title("Pacman")
    screen.setup(width=scr_wid + 10, height=scr_hi + 10)
    screen.bgcolor("black")
    return screen


def bind_controls(screen, player):
    screen.listen()
    screen.onkeypress(player.turn_right, "d")
    screen.onkeypress(player.turn_left, "a")
    screen.onkeypress(player.turn_up, "w")
    screen.onkeypress(player.turn_down, "s")


def game_loop(screen, player, ghosts) -> None:
    # player
    player.move()
    player.check_wall_collision()

    # ghosts
    for ghost in ghosts:
        ghost.move((player.xcor(), player.ycor()))

    screen.update()

    #  60 FPS (very smooth)
    screen.ontimer(lambda: game_loop(screen, player, ghosts), 1000 // 60)


def main() -> None:
    screen = init_screen()

    wall_pen = Wall()
    pellet_pen = Pellet()
    power_pen = Powerup()

    wall_pen.draw()
    walls = wall_pen.walls

    pellet_pen.draw()
    power_pen.draw()

    # player
    player_start = random.choice(pellet_pen.pellets)
    player = Player(walls)
    player.goto(player_start[0], player_start[1])

    bind_controls(screen, player)

    # ghosts
    ghosts = []
    for i in range(4):
        ghost = Ghost(walls, algorithm="bfs" if i < 2 else "astar")

        start = random.choice(pellet_pen.pellets)
        ghost.goto(start[0], start[1])

        if i < 2:
            ghost.color("red")
        else:
            ghost.color("blue")

        ghosts.append(ghost)

    game_loop(screen, player, ghosts)
    screen.mainloop()


if __name__ == "__main__":
    main()
   

   

    
    
