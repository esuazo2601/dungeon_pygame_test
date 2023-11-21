import pygame

def get_sprite(row, col, sprite_width, sprite_height, spritesheet):
    x = col * sprite_width
    y = row * sprite_height
    sprite = spritesheet.subsurface(pygame.Rect(x, y, sprite_width, sprite_height))
    return sprite

class Habilidad():
    def __init__(self,daño, nombre):
        self.daño = daño,
        self.nombre = nombre

class Heroe:
    def __init__(self, x, y, max_hp, vivo=True):
        self.Habilidades = []
        self.max_hp = max_hp
        self.hp = max_hp
        self.vivo = vivo

        self.animation_list = []
        self.attack_animation_list = []

        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.x = x
        self.y = y
        self.isAttacking = False

    def update(self, animation_cooldown):
        if self.animation_list:
            self.image = self.animation_list[self.frame_index]
            if pygame.time.get_ticks() - self.update_time > animation_cooldown:
                self.update_time = pygame.time.get_ticks()
                self.frame_index += 1
            if self.frame_index >= len(self.animation_list):
                self.frame_index = 0

    def update_attack(self, animation_cooldown):
        if self.attack_animation_list:
            self.image_attack = self.attack_animation_list[self.frame_index]
            if pygame.time.get_ticks() - self.update_time > animation_cooldown:
                self.update_time = pygame.time.get_ticks()
                self.frame_index += 1
            if self.frame_index >= len(self.attack_animation_list):
                self.frame_index = 0
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def draw_attack(self, screen):
        if self.image_attack:
            screen.blit(self.image_attack, self.rect_attack)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def add_Habilidad(self, daño, nombre):
        if len(self.Habilidades) < 3:
            habilidad = Habilidad(daño, nombre)
            self.Habilidades.append(habilidad)

class Guerrero(Heroe):
    def __init__(self, x, y, max_hp, fuerza):
        super().__init__(x, y, max_hp)

        for i in range(8):
            img = pygame.image.load(f'images/Heroes/Guerrero/Idle/{i}.png')
            img = pygame.transform.scale(img, (img.get_width()*3, img.get_height()*3))
            self.animation_list.append(img)
        
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()  
        
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.fuerza = fuerza
    
    def attack(self, target, skill):
        damage = skill.daño[0] + self.fuerza
        target.hp -= damage

    def get_dmg(self):
        return self.fuerza

class Mago(Heroe):
    def __init__(self, x, y, max_hp, poder_magico):
        super().__init__(x, y, max_hp)
        self.poder_magico = poder_magico
        spritesheet = pygame.image.load(f'images/Heroes/Mago/Idle.png')
        spritesheet_width = spritesheet.get_width()
        spritesheet_height = spritesheet.get_height()
        rows = 1
        cols = 7
        sprite_width = spritesheet_width // cols
        sprite_height = spritesheet_height // rows
        for i in range(rows):
            for j in range(cols):
                img = get_sprite(i, j, sprite_width, sprite_height, spritesheet)
                img = pygame.transform.scale(img, (img.get_width()*2, img.get_height()*2))
                self.animation_list.append(img)
        self.image = self.animation_list[self.frame_index]

        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def attack(self, target, skill):
        damage = skill.daño[0] + self.poder_magico
        target.hp -= damage 
        self.isAttacking = True
    
    def get_dmg(self):
        return self.poder_magico

class Arquero(Heroe):
    def __init__(self, x, y, max_hp, precision):
        super().__init__(x, y, max_hp)
        self.precision = precision
        spritesheet = pygame.image.load(f'images/Heroes/Cazadora/cazadora.png')
        spritesheet_width = spritesheet.get_width()
        spritesheet_height = spritesheet.get_height()
        rows = 1
        cols = 4
        sprite_width = spritesheet_width // cols
        sprite_height = spritesheet_height // rows
        for i in range(rows):
            for j in range(cols):
                img = get_sprite(i, j, sprite_width, sprite_height, spritesheet)
                img = pygame.transform.scale(img, (img.get_width()*0.5, img.get_height()*0.5))
                img = pygame.transform.flip(img, True, False)
                self.animation_list.append(img)

        self.image = self.animation_list[self.frame_index]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def attack(self, target, skill):
        damage = skill.daño[0] + self.precision
        target.hp -= damage 
    
    def get_dmg(self):
        return self.precision

