import pygame
import os
from constants import *

def main():
    pygame.init()
    running = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        pygame.display.flip()


if __name__ == "__main__":
    os.environ["SDL_AUDIODRIVER"] = "dsp"
    main()