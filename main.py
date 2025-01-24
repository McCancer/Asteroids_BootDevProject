import pygame
import os
from player import Player
from constants import *

def main():
    pygame.init()
    gameClock = pygame.time.Clock()
    dt = 0
    running = True
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Player.containers = (updatable, drawable)
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for item in updatable:
            item.update(dt)
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()
        dt = gameClock.tick(60) / 1000


if __name__ == "__main__":
    main()