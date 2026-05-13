import pygame

import random

from settings import *


class Ball:
    radius = BALL_RADIUS
    
    def __init__(self):
        self.speed_x = random.random() * 6 - 3
        self.speed_y = random.random() * 3 + 3
        self.pos_x = random.random() * (0.5 * WINDOW_SIZE) + 0.25 * WINDOW_SIZE
        self.pos_y = float(self.radius)

        self.hitbox = pygame.Rect(
            self.pos_x - self.radius,
            self.pos_y - self.radius,
            self.radius * 2,
            self.radius * 2
            )
        
        self.color = (int(random.random() * 155), int(random.random() * 155), int(random.random() * 155))
        
        
    def check_window_collision(self):
        if self.pos_y <= self.radius:
            self.speed_y *= -1
        if self.pos_x > WINDOW_SIZE - self.radius:
            self.speed_x *= -1
        elif self.pos_x < self.radius:
            self.speed_x *= -1
    
    def check_paddle_collision(self, paddle_hitbox):
        if self.hitbox.colliderect(paddle_hitbox) and self.speed_y > 0:
            self.speed_y *= -(0.9 + (random.random() * 0.2))
            self.speed_x *= 0.7 + (random.random() * 0.6)
            return True
        return False
    
    def check_ball_lost(self):
        return self.pos_y > WINDOW_SIZE + self.radius
    
    def update(self):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
        
        self.hitbox = pygame.Rect(
            self.pos_x - self.radius,
            self.pos_y - self.radius,
            self.radius * 2,
            self.radius * 2
            )
        
    
    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.pos_x, self.pos_y), self.radius)
