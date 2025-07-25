import pygame 
import os
base = os.path.dirname(__file__)
os.chdir(base)
from config import window_width, window_height, FPS
from src.engine.game import Game
from src.utils import load_image

def main():
    pygame.init()
    pygame.display.set_caption(" team  --  Stay alive !!!!")
    #pygame.display.set_icon(pygame.image.load("src/assets/images/background-sky.png"))




    screen = pygame.display.set_mode((window_width, window_height))
    clock = pygame.time.Clock()
    game = Game() # ye object az class Game sakhte mishe ke hame chiz ro dar bar migire
    try:
        background = load_image("src/assets/images/background-sky.png", (window_width, window_height))
    except FileNotFoundError:
        print("Warning: 'background-sky.png' not found, using black background")
        background = None
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(f"Mouse clicked: button={event.button}, pos={event.pos}") 
        # berooz resani bazi
        game.update()
        
        # draw kardan ashia 
        if background:
            screen.blit(background, (0, 0)) 
        else:
            screen.fill((0, 0, 0))
        game.draw(screen)
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()