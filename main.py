"""entire game is here"""
import turtle
import pygame
from cons import scr_hi,scr_wid
from renderer import Wall, Pellet, Powerup


def init_screen() -> turtle.Screen:
    screen= turtle.Screen()
    screen.tracer(0)
    screen.title("Pacman")
    screen.setup(width=scr_wid+10, height=scr_hi+10)
    screen.bgcolor("black")
    return screen

def game_loop(screen) -> None:
    screen.update()

def main() -> None:
    screen=init_screen()
    wall_pen=Wall()
    pellet_pen=Pellet()
    power_pen=Powerup()

    wall_pen.draw()
    pellet_pen.draw()
    power_pen.draw()
    game_loop(screen= screen)
    screen.mainloop()
    

if __name__=="__main__":
    main()
