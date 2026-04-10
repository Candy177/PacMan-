"""entire game is here"""
import turtle
import pygame


def init_screen() -> turtle.Screen:
    screen= turtle.Screen()
    screen.tracer(0)
    screen.title("Pacman")
    screen.setup(width=1000, height=800)
    screen.bgcolor("black")
    return screen

def game_loop(screen) -> None:
    screen.update()

def main() -> None:
    screen=init_screen()
    game_loop(screen= screen)
    screen.mainloop()

if __name__=="__main__":
    main()
