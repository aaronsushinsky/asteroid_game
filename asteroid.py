import pygame
from constants import *
from circleshape import CircleShape
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw (self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        elif self.radius > ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            new_angle = random.uniform(20, 50)
            asteroid1 = self.velocity.rotate(new_angle)
            asteroid2 = self.velocity.rotate(-new_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
            new_asteroid1.velocity = asteroid1 * 1.2
            new_asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
            new_asteroid2.velocity = asteroid2 * 1.2
        

