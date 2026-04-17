"""entire game is here"""

import turtle
import random

from cons import scr_hi, scr_wid
from renderer import Wall, Pellet, Powerup
from actors import Player, Ghost


def init_screen() -> turtle.Screen:
    # Initialize the game screen
    screen = turtle.Screen()
    screen.tracer(0)
    screen.title("Pacman")
    screen.setup(width=scr_wid + 10, height=scr_hi + 10)
    screen.bgcolor("black")
    return screen


def bind_controls(screen, player):
    # Bind keyboard controls to player movement
    screen.listen()
    screen.onkeypress(player.turn_right, "d")
    screen.onkeypress(player.turn_left, "a")
    screen.onkeypress(player.turn_up, "w")
    screen.onkeypress(player.turn_down, "s")


def game_loop(screen, player, ghosts) -> None:
    # Main game loop (runs continuously)

    # Move player and check wall collision
    player.move()
    player.check_wall_collision()

    # Move all ghosts toward the player
    for ghost in ghosts:
        ghost.move((player.xcor(), player.ycor()))

    # Update screen
    screen.update()

    # Repeat the loop (about 10 FPS)
    screen.ontimer(lambda: game_loop(screen, player, ghosts), 1000//60)


def main() -> None:
    # Initialize screen
    screen = init_screen()

    # Create and draw maze elements
    wall_pen = Wall()
    pellet_pen = Pellet()
    power_pen = Powerup()

    wall_pen.draw()
    walls = wall_pen.walls  # Get wall positions

    pellet_pen.draw()
    power_pen.draw()

    # Choose random starting position for player
    player_start = random.choice(pellet_pen.pellets)

    # Create player
    player = Player(walls)
    player.goto(player_start[0], player_start[1])

    # Bind controls
    bind_controls(screen, player)

    # ===============================
    # Create ghosts

    ghosts = []

    for i in range(4):
        # First 2 ghosts use BFS, last 2 use A*
        ghost = Ghost(walls, algorithm="bfs" if i < 2 else "astar")

        # Set random starting position
        start = random.choice(pellet_pen.pellets)
        ghost.goto(start[0], start[1])

        # Color coding for algorithms
        if i < 2:
            ghost.color("red")   # BFS ghosts
        else:
            ghost.color("blue")  # A* ghosts

        ghosts.append(ghost)

    # ===============================

    # Start the game loop
    game_loop(screen, player, ghosts)

    # Keep the window open
    screen.mainloop()


if __name__ == "__main__":
    main()

    
