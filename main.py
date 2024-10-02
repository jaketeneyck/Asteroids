import pygame
from asteroids.constants import *

def main():
    # Initialize pygame and set the game window size
    pygame.init()
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    while True:
        screen.fill((0,0,0))
        pygame.display.flip()   

if __name__ == "__main__":
    main()
