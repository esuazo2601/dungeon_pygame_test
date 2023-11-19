import pygame

def get_sprite(row, col, sprite_width, sprite_height, spritesheet):
    x = col * sprite_width
    y = row * sprite_height
    sprite = spritesheet.subsurface(pygame.Rect(x, y, sprite_width, sprite_height))
    return sprite

class Guerrero():
    def __init__(self,x,y,max_hp,fuerza):
        self.max_hp = max_hp,
        self.fuerza = fuerza,
        self.vivo = True,
        img = pygame.image.load(f'images/Heroes/Guerrero/Idle/0.png')
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

class Mago():
    def __init__(self,x,y,max_hp,daño):
        self.max_hp = max_hp,
        self.daño = daño,
        self.vivo = True,
        spritesheet = pygame.image.load(f'images/Heroes/Mago/mago.png')
        spritesheet_width = spritesheet.get_width()
        spritesheet_height = spritesheet.get_height()
        rows = 4
        cols = 5
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

class Arquero():
    def __init__(self,x,y,max_hp,daño):
        self.max_hp = max_hp,
        self.daño = daño,
        self.vivo = True,
        spritesheet = pygame.image.load(f'images/Heroes/Cazadora/cazadora.png')
        spritesheet_width = spritesheet.get_width()
        spritesheet_height = spritesheet.get_height()
        rows = 1
        cols = 4
        sprite_width = spritesheet_width // cols
        sprite_height = spritesheet_height // rows
        image = get_sprite(0,0,sprite_width,sprite_height,spritesheet)
        image = pygame.transform.flip(image,True,False)
        self.image = pygame.transform.scale(image,(image.get_width()*0.5, image.get_height()*0.5))
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

class Sala():
    def __init__(self,num,enemies):
        Enemies = []
        for enemy in enemies:
            Enemies.append(enemy)
        self.Enemies = Enemies
        self.terminada = False        
        self.num = num


