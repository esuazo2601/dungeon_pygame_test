import pygame

def get_sprite(row, col, sprite_width, sprite_height, spritesheet):
    x = col * sprite_width
    y = row * sprite_height
    sprite = spritesheet.subsurface(pygame.Rect(x, y, sprite_width, sprite_height))
    return sprite

class Guerrero():
    def __init__(self, x, y, max_hp, fuerza):
        self.max_hp = max_hp
        self.fuerza = fuerza
        self.hp = max_hp  # Añade el campo hp
        self.vivo = True
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

        for i in range(8):
            img = pygame.image.load(f'images/Heroes/Guerrero/Idle/{i}.png')
            img = pygame.transform.scale(img, (img.get_width()*3, img.get_height()*3))
            self.animation_list.append(img)
        self.image = self.animation_list[self.frame_index]
        
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        animation_cooldown = 100
        # handle animation
        # update image
        self.image = self.animation_list[self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

class Mago():
    def __init__(self, x, y, max_hp, daño):
        self.max_hp = max_hp
        self.daño = daño
        self.hp = max_hp  # Añade el campo hp
        self.vivo = True
        spritesheet = pygame.image.load(f'images/Heroes/Mago/Idle.png')
        spritesheet_width = spritesheet.get_width()
        spritesheet_height = spritesheet.get_height()
        rows = 1
        cols = 7
        sprite_width = spritesheet_width // cols
        sprite_height = spritesheet_height // rows
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

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

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        animation_cooldown = 200

        self.image = self.animation_list[self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

class Arquero():
    def __init__(self, x, y, max_hp, daño):
        self.max_hp = max_hp
        self.daño = daño
        self.hp = max_hp  # Añade el campo hp
        self.vivo = True
        spritesheet = pygame.image.load(f'images/Heroes/Cazadora/cazadora.png')
        spritesheet_width = spritesheet.get_width()
        spritesheet_height = spritesheet.get_height()
        rows = 1
        cols = 4
        sprite_width = spritesheet_width // cols
        sprite_height = spritesheet_height // rows
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

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

    def update(self):
        animation_cooldown = 200

        self.image = self.animation_list[self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
