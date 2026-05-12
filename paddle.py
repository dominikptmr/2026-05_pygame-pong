import pygame

from settings import *


class Paddle:
    def __init__(self):
        self.height = 10
        self.width = 100

        self.pos_x = 0.5 * window_size - 0.5 * self.width
        self.pos_y = window_size - self.height

        self.speed_x = 8
    
        self.hitbox = pygame.Rect(
            self.pos_x,
            self.pos_y,
            self.width,
            self.height
        )
    
    def move_paddle(self):
        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_RIGHT]:
            self.pos_x += self.speed_x
        if keys[pygame.K_LEFT]:
            self.pos_x -= self.speed_x
    
    def set_hitbox(self):
        self.hitbox = pygame.Rect(
            self.pos_x,
            self.pos_y,
            self.width,
            self.height
        )
    
    def draw_paddle(self):
        pygame.draw.rect(
            window,
            (0, 0, 0),
            (self.pos_x, window_size - self.height , self.width , self.height)
        )
        
    
        
    
