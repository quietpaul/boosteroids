from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.init(x, y, radius)

    def update(self, speed):
        speed += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2) 



