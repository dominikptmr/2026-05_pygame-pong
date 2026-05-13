import pygame

from settings import *


class Paddle:
    def __init__(self):
        self.height = PADDLE_HEIGHT
        self.width = PADDLE_WIDTH

        self.pos_x = 0.5 * WINDOW_SIZE - 0.5 * self.width
        self.pos_y = WINDOW_SIZE - self.height

        self.speed_x = PADDLE_SPEED_X
    
        self.hitbox = pygame.Rect(
            self.pos_x,
            self.pos_y,
            self.width,
            self.height
        )
    
    def update(self):
        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_RIGHT]:
            self.pos_x += self.speed_x
        if keys[pygame.K_LEFT]:
            self.pos_x -= self.speed_x
            
        self.hitbox = pygame.Rect(
            self.pos_x,
            self.pos_y,
            self.width,
            self.height
        ) 
    
    def draw(self, window):
        pygame.draw.rect(
            window,
            PADDLE_COLOR,
            (self.pos_x, WINDOW_SIZE - self.height , self.width , self.height)
        )
        
    
        
    
