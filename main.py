import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    # Initialize pygame and set the game window size
    pygame.init()
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create clock to limit FPS
    clock = pygame.time.Clock()
    dt = 0

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    # Create objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()

    # Main game loop
    while True:
        # Check that the player hasn't quit the game, quit if yes
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Fill the screen black       
        screen.fill((0,0,0))

        # Make any object changes 
        for item in updatable:
            item.update(dt)
        for item in drawable:
            item.draw(screen)

        # Check if any asteroids have hit the player, if yes then end
        for item in asteroids:
            if item.checkCollision(player):
                print("Game over!")
                exit()

        # Check if any bullets have hit an asteroid
        print(len(shots))
        for item in asteroids:
            for s in shots:
                if s.checkCollision(item):
                    item.kill()
                    s.kill()

        # Re-render the screen

        pygame.display.flip()   

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
