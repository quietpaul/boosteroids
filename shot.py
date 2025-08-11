from constants import SHOT_RADIUS
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (int(self.position.x), int(self.position.y)), SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity * dt

