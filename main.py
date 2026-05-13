import pygame

from settings import *
from game import Game


def main():
    
    pygame.init()
    
    game = Game()

    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False

        game.window.fill(BACKGROUND_COLOR)

        game.update_score_text()
    
        game.paddle.update()
        game.paddle.draw(game.window)
    
        for ball in game.balls[:]:
            ball.update()
            ball.draw(game.window)
        
            ball.check_window_collision()
        
            if ball.check_paddle_collision(game.paddle.hitbox):
                game.increase_score()
                if game.get_score() % 3 == 0:
                    game.add_ball()
        
            if ball.lost():
                game.remove_ball(ball)
            
            if len(game.balls) <= 0:
                game.reset()
        
        pygame.display.flip()
        
        game.clock.tick(FPS)

    pygame.quit()
    
main()