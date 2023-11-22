import pygame
from typing import Union
from enemies import Esqueleto,Zombie,Bandido,Orco
from heroes import Mago

def get_sprite(row, col, sprite_width, sprite_height, spritesheet):
    x = col * sprite_width
    y = row * sprite_height
    sprite = spritesheet.subsurface(pygame.Rect(x, y, sprite_width, sprite_height))
    return sprite

class Character_arrow():
    def __init__(self):
        self.target_hero = None
        img = pygame.image.load(f'images/character_arrow.png')
        img = pygame.transform.scale(img, (img.get_width()*0.2, img.get_height()*0.2))
        img = pygame.transform.flip(img,False,True)
        self.image = img
        self.rect  = self.image.get_rect()
    
    def draw(self, screen):
        if self.target_hero:
            if isinstance(self.target_hero,Mago):
                self.rect = self.image.get_rect()
                self.rect.center = (self.target_hero.get_x()-30, self.target_hero.get_y() - 80)
                screen.blit(self.image, self.rect)
            else:
                self.rect = self.image.get_rect()
                self.rect.center = (self.target_hero.get_x(), self.target_hero.get_y() - 100)
                screen.blit(self.image, self.rect)
    
    def set_target_hero(self, hero):
        self.target_hero = hero
    
    def get_x (self):
        return self.x
    
    def get_y (self):
        return self.y

class Skill_arrow():
    def __init__(self):
        spritesheet = pygame.image.load(f'images/Arrows.png')
        spritesheet_width = spritesheet.get_width()
        spritesheet_height = spritesheet.get_height()
        rows = 3
        cols = 3
        sprite_width = spritesheet_width // cols
        sprite_height = spritesheet_height // rows
        self.selected_skill = None
        img = get_sprite(2,1, sprite_width, sprite_height, spritesheet)
        img = pygame.transform.scale(img, (img.get_width()*0.5, img.get_height()*0.5))

        self.image = img
        self.rect  = self.image.get_rect()
    
    def draw(self, screen, x, y):
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        screen.blit(self.image, self.rect)

    def set_target_hero(self, hero):
        self.target_hero = hero
    
    def get_x (self):
        return self.x
    
    def get_y (self):
        return self.y
    
class Enemy_arrow():
    def __init__(self):
        spritesheet = pygame.image.load(f'images/Arrows.png')
        spritesheet_width = spritesheet.get_width()
        spritesheet_height = spritesheet.get_height()
        rows = 3
        cols = 3
        sprite_width = spritesheet_width // cols
        sprite_height = spritesheet_height // rows
        self.selected_enemy = None
        img = get_sprite(2,0, sprite_width, sprite_height, spritesheet)
        img = pygame.transform.rotate(img,-90)
        img = pygame.transform.scale(img, (img.get_width()*0.5, img.get_height()*0.5))

        self.image = img
        self.rect  = self.image.get_rect()
    
    def draw(self, screen):
        if self.selected_enemy:
            self.rect = self.image.get_rect()
            self.rect.center = (self.selected_enemy.get_x()+10, self.selected_enemy.get_y() - 180)
            screen.blit(self.image, self.rect)

    def set_target_enemy(self, enemy):
        self.selected_enemy = enemy
    
    def get_x (self):
        return self.x
    
    def get_y (self):
        return self.y


class Sala():
    def __init__(self,num):
        self.Enemies = []
        self.terminada = False        
        self.num = num
    
    def addEnemy(self,enemy: Union[Orco,Esqueleto,Zombie,Bandido]):
        self.Enemies.append(enemy)

    def check_terminada(self):
        if len (self.Enemies) <= 0:
            return True

class Dungeon():
    def __init__(self):
        self.Heroes = []
        self.Salas = []
    
    def addHeroes (self, heroes):
        for heroe in heroes:
            self.Heroes.append(heroe)
    def addSalas (self,salas):
        for sala in salas:
            self.Salas.append(sala)

