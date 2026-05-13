import pygame

from settings import *
from ball import Ball
from paddle import Paddle

class Game:
    
    def __init__(self):
        self.window = pygame.display.set_mode([WINDOW_SIZE, WINDOW_SIZE])
        self.clock = pygame.time.Clock()
    
        self.paddle = Paddle()
        self.balls = [Ball()]
    
        self.running = True
        self.score = 0
    
        self.score_font = pygame.font.Font(None, SCORE_FONT_SIZE)
        
    
    def reset(self):
        self.paddle = Paddle()
        self.balls = [Ball()]
        self.score = 0
    
    def add_ball(self):
        self.balls.append(Ball())
        
    def remove_ball(self, ball):
        self.balls.remove(ball)
        
    def increase_score(self):
        self.score += 1
    
    def get_score(self):
        return self.score
    
    def update_score_text(self):
        score_text = self.score_font.render(f"{self.score}", True, SCORE_FONT_COLOR)
        score_text.set_alpha(SCORE_FONT_OPACITY)
        score_box = score_text.get_rect(center=(WINDOW_SIZE / 2, WINDOW_SIZE / 2))
        self.window.blit(score_text, score_box)
        
    