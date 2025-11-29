import pygame
import random
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", center=(int(self.position.x), int(self.position.y)), radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            base_vector = self.velocity.copy()
            velocity_one = base_vector.rotate(random_angle) * 1.2
            velocity_two = base_vector.rotate(-random_angle) * 1.2
            new_asteroids_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_position = self.position.copy()
            new_asteroid_one = Asteroid(new_asteroid_position.x, new_asteroid_position.y, new_asteroids_radius)
            new_asteroid_two = Asteroid(new_asteroid_position.x, new_asteroid_position.y, new_asteroids_radius)
            new_asteroid_one.velocity = velocity_one
            new_asteroid_two.velocity = velocity_two
            