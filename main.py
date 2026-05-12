import pygame

from settings import *
from ball import Ball
from paddle import Paddle


def reset_game():
    Ball.balls = []
    Ball.balls.append(Ball())
    paddle = Paddle()
    score_counter = 0
    
    return paddle, score_counter


def main():
    
    clock = pygame.time.Clock()
    
    running = True
    score_counter = 0
    
    paddle = Paddle()
    Ball.balls.append(Ball())

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill((255, 255, 255))
    
        score_text = counter_font.render(f"{score_counter}", True, (0, 0, 0))
        score_text.set_alpha(64)
        score_box = score_text.get_rect(center=(window_size / 2, window_size / 2))
        window.blit(score_text, score_box)
    
        paddle.move_paddle()
        paddle.set_hitbox()
        paddle.draw_paddle()

    
        for ball in Ball.balls[:]:
            ball.set_pos()
            ball.set_hitbox()
            ball.draw_ball()
        
            ball.check_window_collision()
        
            if ball.check_paddle_collision(paddle.hitbox):
                score_counter += 1
                if not score_counter % 3:
                    Ball.balls.append(Ball())
        
            if ball.check_ball_lost():
                ball.remove_ball(ball)
                Ball.balls_in_play -= 1
                if Ball.balls_in_play <= 0:
                    paddle, score_counter = reset_game()
        
        pygame.display.flip()
        
        clock.tick(120)

    pygame.quit()
    
main()
