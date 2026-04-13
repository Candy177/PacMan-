"""entire game is here"""
import turtle
import random
import pygame
from cons import scr_hi,scr_wid
from renderer import Wall, Pellet, Powerup
from actors import Player

def init_screen() -> turtle.Screen:
    screen= turtle.Screen()
    screen.tracer(0)
    screen.title("Pacman")
    screen.setup(width=scr_wid+10, height=scr_hi+10)
    screen.bgcolor("black")
    return screen

def bind_controls(screen , player):
    screen.listen()
    screen.onkeypress(player.turn_right , "d")
    screen.onkeypress(player.turn_left , "a")
    screen.onkeypress(player.turn_up , "w")
    screen.onkeypress(player.turn_down , "s")


def game_loop(screen , player) -> None:
    player.move()
    player.check_wall_collision()
    screen.update()
    screen.ontimer(lambda : game_loop(screen, player), 1000 // 60)

def main() -> None:
    screen=init_screen()
    wall_pen=Wall()
    pellet_pen=Pellet()
    power_pen=Powerup()

    wall_pen.draw()
    walls = wall_pen.walls
    pellet_pen.draw()
    power_pen.draw()
    # Player starting posistion(on random pellet)
    player_start_coor = random.choice(seq = pellet_pen.pellets)
    player_start_x =  player_start_coor[0]
    player_start_y =  player_start_coor[1]
  
    # Create Pac-man
    player = Player(walls)
    player.goto(player_start_x , player_start_y)
    bind_controls(screen , player)

    game_loop(screen= screen , player = player)
    screen.mainloop()
    

if __name__=="__main__":
    main()
