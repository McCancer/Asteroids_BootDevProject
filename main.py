import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    gameClock = pygame.time.Clock()
    dt = 0
    running = True
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    asteroid_field = AsteroidField()
    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for item in updatable:
            item.update(dt)

        for asteroid in asteroids:
            if(player.checkCollisions(asteroid)):
                print("Game Over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if(asteroid.checkCollisions(shot)):
                    shot.kill()
                    asteroid.split()

        screen.fill(BLACK)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = gameClock.tick(60) / 1000


if __name__ == "__main__":
    main()