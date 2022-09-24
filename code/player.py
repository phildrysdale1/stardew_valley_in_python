## ========== Packages ========== ##
import pygame
from settings import *
from support import *

## ========== Classes ========== ##

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.import_assets()
        self.status = 'down_idle'
        self.frame_index = 0

        # general setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)

        # movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    def import_assets(self):
        self.animations = {'up' : [], 'down' : [], 'left' : [], 'right' : [],
                            'right_idle' : [], 'left_idle' : [], 'up_idle' : [], 'down_idle' : [],
                            'right_hoe' : [], 'left_hoe' : [], 'up_hoe' : [], 'down_hoe' : [],
                            'right_axe' : [], 'left_axe' : [], 'up_axe' : [], 'down_axe' : [],
                            'right_water' : [], 'left_water' : [], 'up_water' : [], 'down_water' : []}
        for animation in self.animations.keys():
            full_path = 'stardew_valley_in_python/graphics/character/' + animation
            self.animations[animation] = import_folder(full_path)
        print(self.animations)

    def move(self, dt):
        # normalising the vector
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        # vertical movement     
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0   
            
    def update(self, dt):
        self.input()
        self.move(dt)