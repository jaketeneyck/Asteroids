import pygame
from constants import *
from player import *

def main():
    # Initialize pygame and set the game window size
    pygame.init()
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create clock to limit FPS
    clock = pygame.time.Clock()
    dt = 0

    # Create player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    updatable.add(player)
    drawable.add(player)

    # Main game loop
    while True:
        # Check that the player hasn't quit the game, quit if yes
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            

        # Make any object changes 
        for item in updatable:
            item.update(dt)
        for item in drawable:
            item.draw(screen)

        # Re-render the screen
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()   

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
