import pygame
from constants import *
import circleshape
import player   
import asteroid
import asteroidfield

def main():
    pygame.init()
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    x=SCREEN_WIDTH/2
    y=SCREEN_HEIGHT/2
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    asteroids=pygame.sprite.Group()
    player.Player.containers=(updatable,drawable)
    asteroid.Asteroid.containers=(asteroids,updatable,drawable)
    asteroidfield.AsteroidField.containers=(updatable)
    aKiller=player.Player(x,y)
    aField=asteroidfield.AsteroidField()
    
    while True:
        clk=pygame.time.Clock()
        dt=0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        dt=(clk.tick(60)/1000)
        for i in updatable:
            i.update(dt)
        for z in drawable:
            z.draw(screen)
        pygame.display.flip()
        
    
    print("\n")
    print(f"Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()

