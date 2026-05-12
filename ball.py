import random

from settings import *


class Ball:
    balls_total = 0
    balls_in_play = 0
    
    radius = 10
    color = (0, 0, 0)
    
    balls = []
    
    def __init__(self):
        Ball.balls_total += 1
        Ball.balls_in_play += 1
        
        self.speed_x = random.random() * 0.8 - 0.4
        self.speed_y = random.random() * 0.4 - 0.2
        self.pos_x = random.random() * (0.5 * window_size) + 0.25 * window_size
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
        if self.pos_x > window_size - self.radius:
            self.speed_x *= -1
        elif self.pos_x < self.radius:
            self.speed_x *= -1
    
    def check_schlaeger_collision(self, schlaeger_hitbox):
        if self.hitbox.colliderect(schlaeger_hitbox) and self.speed_y > 0:
            self.speed_y *= -1
            return True
        return False
    
    def check_ball_lost(self):
        return self.pos_y > window_size + self.radius
    
    def set_hitbox(self):
        self.hitbox = pygame.Rect(
            self.pos_x - self.radius,
            self.pos_y - self.radius,
            self.radius * 2,
            self.radius * 2
            )
    
    def set_pos(self):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
        
    
    def draw_ball(self):
        pygame.draw.circle(window, self.color, (self.pos_x, self.pos_y), self.radius)
    
    def remove_ball(self, ball):
        self.balls.remove(ball)