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
        
    
    def check_quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def reset(self):
        self.paddle = Paddle()
        self.balls = [Ball()]
        self.score = 0
        
    def add_ball(self):
        self.balls.append(Ball())
        
    def remove_ball(self, ball):
        self.balls.remove(ball)
        
    def increase_score_and_add_ball(self):
        self.score += 1
        
    def draw_score(self):
        score_text = self.score_font.render(f"{self.score}", True, SCORE_FONT_COLOR)
        score_text.set_alpha(SCORE_FONT_OPACITY)
        score_box = score_text.get_rect(center=(WINDOW_SIZE / 2, WINDOW_SIZE / 2))
        self.window.blit(score_text, score_box)
        
    def run(self):
        while self.running:
        
            self.check_quit_event()
        
            self.window.fill(BACKGROUND_COLOR)

            self.draw_score()
    
            self.paddle.update()
            self.paddle.draw(self.window)
    
            for ball in self.balls[:]:
                ball.update()
                ball.draw(self.window)
        
                ball.check_window_collision()
        
                if ball.check_paddle_collision(self.paddle.hitbox):
                    self.score += 1
                    if self.score % 3 == 0:
                        self.add_ball()
        
                if ball.lost():
                    self.remove_ball(ball)
            
                if len(self.balls) == 0:
                    self.reset()
        
            pygame.display.flip()
        
            self.clock.tick(FPS)
    