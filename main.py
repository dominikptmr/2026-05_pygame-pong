import pygame

from game import Game


def main():
    pygame.init()
    
    game = Game()
    game.run()

    pygame.quit()
    
main()