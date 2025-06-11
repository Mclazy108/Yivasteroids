from typing import ClassVar, Tuple
import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
from circleshape import CircleShape


class Player(CircleShape):
    containers: ClassVar[Tuple[pygame.sprite.Group, ...]]

    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(x, y, PLAYER_RADIUS)
            super().add(*self.containers)
        else:
            super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation) * self.radius
        right = pygame.Vector2(1, 0).rotate(self.rotation) * self.radius / 1.5
        a = self.position + forward
        b = self.position - forward - right
        c = self.position - forward + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
