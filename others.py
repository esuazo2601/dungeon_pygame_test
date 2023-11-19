import pygame
from typing import Union, List
from enemies import Esqueleto,Zombie,Bandido,Orco
from heroes import Mago,Guerrero,Arquero

def get_sprite(row, col, sprite_width, sprite_height, spritesheet):
    x = col * sprite_width
    y = row * sprite_height
    sprite = spritesheet.subsurface(pygame.Rect(x, y, sprite_width, sprite_height))
    return sprite

class Character_arrow():
    def __init__(self):
        spritesheet = pygame.image.load(f'images/Arrows.png')
        spritesheet_width = spritesheet.get_width()
        spritesheet_height = spritesheet.get_height()
        rows = 3
        cols = 3
        sprite_width = spritesheet_width // cols
        sprite_height = spritesheet_height // rows
        self.target_hero = None
        img = get_sprite(1,0, sprite_width, sprite_height, spritesheet)
        img = pygame.transform.scale(img, (img.get_width()*0.5, img.get_height()*0.5))

        self.image = img
        self.rect  = self.image.get_rect()
    
    def draw(self, screen):
        if self.target_hero:
            if isinstance(self.target_hero,Mago):
                self.rect = self.image.get_rect()
                self.rect.center = (self.target_hero.get_x()-20, self.target_hero.get_y() - 50)
                screen.blit(self.image, self.rect)
            else:
                self.rect = self.image.get_rect()
                self.rect.center = (self.target_hero.get_x()+10, self.target_hero.get_y() - 80)
                screen.blit(self.image, self.rect)
    
    def set_target_hero(self, hero):
        self.target_hero = hero
    
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
        terminada_temp = True
        for enemy in self.Enemies:
            if enemy.hp > 0:
                terminada_temp = False
        return terminada_temp

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


