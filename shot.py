import pygame
import circleshape
import constants

class Shot(circleshape.CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,SHOT_RADIUS)
        

