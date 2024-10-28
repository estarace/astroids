import pygame
import circleshape
from constants import *
import shot

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation=0
        self.shot_timer=0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        #right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        # sub-classes must override
        screen
        ta=self.triangle()
        pygame.draw.polygon(screen,"white",ta,2)

    def rotate(self, dt):
        self.rotation+=(PLAYER_TURN_SPEED*dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-(dt)) 
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-(dt))
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.shot_timer-=dt


    def move(self,dt):
        forward=pygame.Vector2(0,1).rotate(self.rotation)
        self.position+=forward*PLAYER_SPEED*dt

    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        if self.shot_timer <= 0:
            pewpew=shot.Shot(self.position[0],self.position[1])
            pewpew.velocity = pygame.Vector2(0, 1).rotate(self.rotation)*PLAYER_SHOOT_SPEED
            self.shot_timer=PLAYER_SHOOT_COOLDOWN