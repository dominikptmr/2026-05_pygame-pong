import pygame

from settings import *
from ball import Ball
from paddle import Paddle


def reset_game():
    balls = [Ball()]
    paddle = Paddle()
    score_counter = 0
    
    return paddle, balls, score_counter


def main():
    
    pygame.init()
    
    window = pygame.display.set_mode([WINDOW_SIZE, WINDOW_SIZE])
    clock = pygame.time.Clock()
    
    paddle = Paddle()
    balls = [Ball()]
    
    running = True
    score = 0
    
    score_font = pygame.font.Font(None, SCORE_FONT_SIZE)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill(BACKGROUND_COLOR)
    
        score_text = score_font.render(f"{score}", True, SCORE_FONT_COLOR)
        score_text.set_alpha(SCORE_FONT_OPACITY)
        score_box = score_text.get_rect(center=(WINDOW_SIZE / 2, WINDOW_SIZE / 2))
        window.blit(score_text, score_box)
    
        paddle.update()
        paddle.draw(window)

    
        for ball in balls[:]:
            ball.update()
            ball.draw(window)
        
            ball.check_window_collision()
        
            if ball.check_paddle_collision(paddle.hitbox):
                score += 1
                if score % 3 == 0:
                    balls.append(Ball())
        
            if ball.check_ball_lost():
                balls.remove(ball)
            
            if len(balls) <= 0:
                paddle, balls, score = reset_game()
        
        pygame.display.flip()
        
        clock.tick(FPS)

    pygame.quit()
    
main()
