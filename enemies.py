import pygame

def get_sprite(row, col, sprite_width, sprite_height, spritesheet):
    x = col * sprite_width
    y = row * sprite_height
    sprite = spritesheet.subsurface(pygame.Rect(x, y, sprite_width, sprite_height))
    return sprite

class Bandit():
    def __init__(self,x,y,max_hp,daño):
        self.max_hp = max_hp,
        self.daño = daño,
        self.vivo = True,
        img = pygame.image.load(f'images/Enemies/Bandit/Idle/0.png')
        self.image = pygame.transform.scale(img, (img.get_width()*3, img.get_height()*3))
        self.rect  = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x,y)

    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def get_x (self):
        return self.x
    def get_y (self):
        return self.y


class Orco():
    def __init__(self,x,y,max_hp,daño):
        self.max_hp = max_hp,
        self.daño = daño,
        self.vivo = True,
        spritesheet = pygame.image.load(f'images/Enemies/Orc/orcsheet.png')
        spritesheet_width = spritesheet.get_width()
        spritesheet_height = spritesheet.get_height()
        rows = 4
        cols = 3
        sprite_width = spritesheet_width // cols
        sprite_height = spritesheet_height // rows
        image = get_sprite(0,0,sprite_width,sprite_height,spritesheet)
        self.image = pygame.transform.scale(image,(image.get_width()*3, image.get_height()*3))
        self.x = x
        self.y = y
        self.rect  = self.image.get_rect()
        self.rect.center = (x,y)

    def draw(self,screen):
        screen.blit(self.image,self.rect)
    def get_x (self):
        return self.x
    def get_y (self):
        return self.y

class Zombie():
    def __init__(self,x,y,max_hp,daño):
        self.max_hp = max_hp,
        self.daño = daño,
        self.vivo = True,
        img = pygame.image.load(f'images/Enemies/Zombie/Idle/__Zombie01_Idle_000.png')
        img = pygame.transform.flip(img,True,False)
        self.image = pygame.transform.scale(img, (img.get_width()*0.25, img.get_height()*0.25))
        self.rect  = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x,y)

    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def get_x (self):
        return self.x
    def get_y (self):
        return self.y


class Esqueleto():
    def __init__(self,x,y,max_hp,daño):
        self.max_hp = max_hp,
        self.daño = daño,
        self.vivo = True,
        img = pygame.image.load(f'images/Enemies/Esqueleto/Idle/left/idle_left0000.png')
        img = pygame.transform.flip(img,True,False)
        self.image = pygame.transform.scale(img, (img.get_width()*3, img.get_height()*3))
        self.rect  = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x,y)

    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def get_x (self):
        return self.x
    def get_y (self):
        return self.y