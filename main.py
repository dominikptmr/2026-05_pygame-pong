import pygame

from settings import *
from ball import Ball
from schlaeger import Schlaeger

pygame.init()

running = True
score_counter = 0

schlaeger = Schlaeger()
Ball.balls.append(Ball())

while not ende:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.fill((255, 255, 255))
    
    score_text = font.render(f"{score_counter}", True, (0, 0, 0))
    score_text.set_alpha(64)
    score_box = score_text.get_rect(center=(window_size / 2, window_size / 2))
    window.blit(score_text, score_box)
    
    schlaeger.move_schlaeger()
    schlaeger.set_hitbox()
    schlaeger.draw_schlaeger()

    
    for ball in Ball.balls[:]:
        ball.set_pos()
        ball.set_hitbox()
        ball.draw_ball()
        
        ball.check_window_collision()
        
        if ball.check_schlaeger_collision(schlaeger.hitbox):
            score_counter += 1
            if not score_counter % 2:
                Ball.balls.append(Ball())
        
        if ball.check_ball_lost():
            ball.remove_ball(ball)
            Ball.balls_in_play -= 1
            if Ball.balls_in_play <= 0:
                running = False
        
    pygame.display.flip()

pygame.quit()
