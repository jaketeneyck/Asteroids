import pygame
from constants import *

def main():
    # Initialize pygame and set the game window size
    pygame.init()
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create clock to limit FPS
    clock = pygame.time.Clock()
    dt = 0

    # Main game loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill((0,0,0))
        pygame.display.flip()   

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
