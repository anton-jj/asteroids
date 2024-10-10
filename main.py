# this allows is to use code
# from the open-source pygame library

import pygame

# import the hello_function
# import the variable_player varaible
# into the current file

from constants import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
    while True:
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
