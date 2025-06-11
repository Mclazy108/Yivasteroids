import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(x, y, radius)
            super().add(*self.containers)
        else:
            super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        from asteroid import Asteroid  # local import to avoid circular import

        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity1
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity2
