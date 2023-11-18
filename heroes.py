import pygame
class Guerrero():
    def __init__(self,x,y,max_hp,fuerza):
        self.max_hp = max_hp,
        self.fuerza = fuerza,
        self.vivo = True,
        img = pygame.image.load(f'images/Heroes/Guerrero/Idle/0.png')
        self.image = pygame.transform.scale(img, (img.get_width()*3, img.get_height()*3))
        self.rect  = self.image.get_rect()
        self.rect.center = (x,y)

    def draw(self,screen):
        screen.blit(self.image,self.rect)

class Bandit():
    def __init__(self,x,y,max_hp,Fuerza):
        self.max_hp = max_hp,
        self.Fuerza = Fuerza,
        self.vivo = True,
        img = pygame.image.load(f'images/Enemies/Bandit/Idle/0.png')
        self.image = pygame.transform.scale(img, (img.get_width()*3, img.get_height()*3))
        self.rect  = self.image.get_rect()
        self.rect.center = (x,y)

    def draw(self,screen):
        screen.blit(self.image,self.rect)

class Sala():
    def __init__(self,num,enemies):
        Enemies = []
        for enemy in enemies:
            Enemies.append(enemy)
        self.Enemies = Enemies
        self.terminada = False        
        self.num = num