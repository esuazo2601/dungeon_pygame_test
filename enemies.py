import pygame

def get_sprite(row, col, sprite_width, sprite_height, spritesheet):
    x = col * sprite_width
    y = row * sprite_height
    sprite = spritesheet.subsurface(pygame.Rect(x, y, sprite_width, sprite_height))
    return sprite

class Enemigo:
    def __init__(self, x, y, max_hp, daño, vivo=True):
        self.max_hp = max_hp
        self.hp = max_hp
        self.daño = daño
        self.vivo = vivo
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def update(self, animation_cooldown):
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

    def draw_hp(self, screen, font):
        text = font.render(f'{self.hp} HP', True, (255, 0, 0), None)
        screen.blit(text, (self.get_x() - 20, self.get_y() - 100))


class Bandido(Enemigo):
    def __init__(self, x, y, max_hp, daño):
        super().__init__(x, y, max_hp, daño)
        for i in range(8):
            img = pygame.image.load(f'images/Enemies/Bandit/Idle/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            self.animation_list.append(img)
        self.image = self.animation_list[self.frame_index]

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)


class Orco(Enemigo):
    def __init__(self, x, y, max_hp, daño):
        super().__init__(x, y, max_hp, daño)
        spritesheet = pygame.image.load(f'images/Enemies/Orc/orcsheet.png')
        spritesheet_width = spritesheet.get_width()
        spritesheet_height = spritesheet.get_height()
        rows = 1
        cols = 5
        sprite_width = spritesheet_width // cols
        sprite_height = spritesheet_height // rows
        for i in range(rows):
            for j in range(cols):
                img = get_sprite(i, j, sprite_width, sprite_height, spritesheet)
                img = pygame.transform.scale(img, (img.get_width() * 2, img.get_height() * 2))
                img = pygame.transform.flip(img, True, False)
                self.animation_list.append(img)
        self.image = self.animation_list[self.frame_index]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class Zombie(Enemigo):
    def __init__(self, x, y, max_hp, daño):
        super().__init__(x, y, max_hp, daño)
        for i in range(8):
            img = pygame.image.load(f'images/Enemies/Zombie/Idle/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 0.25, img.get_height() * 0.25))
            img = pygame.transform.flip(img, True, False)
            self.animation_list.append(img)
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)


class Esqueleto(Enemigo):
    def __init__(self, x, y, max_hp, daño):
        super().__init__(x, y, max_hp, daño)
        for i in range(8):
            img = pygame.image.load(f'images/Enemies/Esqueleto/Idle/left/idle_left000{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            img = pygame.transform.flip(img, True, False)
            self.animation_list.append(img)
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)

    def draw_hp(self, screen, font):
        text = font.render(f'{self.hp} HP', True, (255, 0, 0), None)
        screen.blit(text, (self.get_x() - 20, self.get_y() - 100))
