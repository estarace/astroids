import pygame
import circleshape
from constants import *

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