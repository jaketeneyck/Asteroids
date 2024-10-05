from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):

    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        elif self.radius:
            angle = random.uniform(20, 50)
            v1 = pygame.Vector2()
            v2 = pygame.Vector2()
            v1 = self.velocity.rotate(angle)
            v2 = self.velocity.rotate(-angle)
            r = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, r)
            a1.velocity = v1
            a2 = Asteroid(self.position.x, self.position.y, r)
            a2.velocity = v2
            return


    def update(self, dt):
        self.position += self.velocity * dt