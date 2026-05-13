import pygame

import json
from datetime import datetime

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
        
        
    def add_ball(self):
        self.balls.append(Ball())
        
    def remove_ball(self, ball):
        self.balls.remove(ball)
    
    def balls_in_play(self):
        return len(self.balls) > 0
    
    
    def draw_score(self):
        score_text = self.score_font.render(f"{self.score}", True, SCORE_FONT_COLOR)
        score_text.set_alpha(SCORE_FONT_OPACITY)
        score_box = score_text.get_rect(center=(WINDOW_SIZE / 2, WINDOW_SIZE / 2))
        self.window.blit(score_text, score_box)
    
    
    def quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True    

   
    def update(self):
        self.paddle.update()

        for ball in self.balls[:]:
                ball.update()

   
    def manage_ball_events(self):
        for ball in self.balls[:]:
            ball.check_window_collision()
            
            if ball.check_paddle_collision(self.paddle.hitbox):
                self.score += 1
                if self.score % 3 == 0:
                    self.add_ball()
            
            if ball.lost():
                    self.remove_ball(ball)

 
    def save(self):
        if self.score > 0:
            game_state = {
                "score": self.score,
                "end_time": str(datetime.now()),
            }
            
            if not SAVE_FILE.exists():
                data = {
                    "games_played": 0,
                    "high_score": 0,
                    "game_history": []
                }
            else:
                with SAVE_FILE.open("r") as file:
                    data = json.load(file)

            data["games_played"] += 1
            data["game_history"].append(game_state)
            if self.score > data["high_score"]:
                data["high_score"] = self.score

            with SAVE_FILE.open("w") as file:
                json.dump(data, file, indent=4)
  
                    
    def reset(self):
        self.paddle = Paddle()
        self.balls = [Ball()]
        self.score = 0

                   
    def draw(self):
        self.window.fill(BACKGROUND_COLOR)
        self.draw_score()
        
        self.paddle.draw(self.window)

        for ball in self.balls[:]:
            ball.draw(self.window)
        
    
    def run(self):
        while self.running:
            
            if self.quit_event():
                self.running = False
            
            self.update()
            self.manage_ball_events()
            self.draw()
            
            if not self.balls_in_play():
                self.save()
                self.reset()
        
            pygame.display.flip()
        
            self.clock.tick(FPS)