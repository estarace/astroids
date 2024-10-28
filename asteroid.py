import pygame
import circleshape
from constants import *
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        #self.position = pygame.Vector2(x, y)
        #self.velocity = pygame.Vector2(0, 0)
        #self.radius = radius

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,width=2)

    def update(self,dt):
        new_val=self.velocity*dt
        self.position+=new_val

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rand_angle=random.uniform(20,50)
        a1=self.velocity.rotate(rand_angle)
        a2=self.velocity.rotate(-(rand_angle))
        new_rad=self.radius-ASTEROID_MIN_RADIUS
        ast1=Asteroid(self.position[0],self.position[1],new_rad)
        ast2=Asteroid(self.position[0],self.position[1],new_rad)
        ast1.velocity=a1*1.2
        ast2.velocity=a2*1.2