import pygame
import circleshape
from constants import *

class Shot(circleshape.CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,SHOT_RADIUS)
        position=pygame.Vector2(x, y)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,width=2)

    def update(self,dt):
        new_val=self.velocity*dt
        self.position+=new_val    

