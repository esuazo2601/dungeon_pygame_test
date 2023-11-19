import pygame
from heroes import Guerrero,Mago,Arquero
from enemies import Esqueleto, Orco, Bandido, Zombie
from others import Character_arrow, Dungeon, Sala
# pygame setup
pygame.init()
clock = pygame.time.Clock()
fps = 60
font = pygame.font.SysFont('Times New Roman',26)

#window size
bottom_panel = 200
screen_width = 1000
screen_height = 400 + bottom_panel

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Dungeon')

background_image = pygame.image.load('images/Dungeon/background.jpg').convert_alpha()
background_image = pygame.transform.scale(background_image,(screen_width,screen_height - bottom_panel))
#load background
panel_image = pygame.image.load('images/Dungeon/panel.png').convert_alpha()
panel_image = pygame.transform.scale(panel_image,(screen_width,bottom_panel))

################################ ESTA PARTE CAMBIA DEPENDIENDO DE LA INSTANCIA #########################
dungeon = Dungeon()
#Heroes
heroes_list = []
knight = Guerrero(120,300,10,10)
mago = Mago(knight.get_x()+120,knight.get_y()-50,10,10)
arquero = Arquero(mago.get_x()+60,knight.get_y(),10,10)

heroes_list.append(knight)
heroes_list.append(mago)
heroes_list.append(arquero)

dungeon.addHeroes(heroes_list)
#Enemies
sala0 = Sala(0)
bandit0 = Bandido(screen_width - 70,300,10,10)
orc0 = Orco(bandit0.get_x()-100,bandit0.get_y()-30,10,10)
zombie0 = Zombie(orc0.get_x()-80,orc0.get_y()+40,10,10)
esqueleto0 = Esqueleto(zombie0.get_x()-90,zombie0.get_y()-15,10,10)

sala0.addEnemy(bandit0)
sala0.addEnemy(orc0)
sala0.addEnemy(zombie0)
sala0.addEnemy(esqueleto0)

salas_list = []
salas_list.append(sala0)
dungeon.addSalas(salas_list)

################################ ESTA PARTE CAMBIA DEPENDIENDO DE LA INSTANCIA #########################

def draw_bg():
    screen.blit(background_image,(0,0))
def draw_panel():
    screen.blit(panel_image,(0,screen_height-bottom_panel))

    text_guerrero = font.render(f'Guerrero: {dungeon.Heroes[0].hp} HP',True,(255,255,255), None)
    text_mago = font.render(f'Mago: {dungeon.Heroes[1].hp} HP',True,(255,255,255), None)
    text_arquero = font.render(f'Arquera: {dungeon.Heroes[2].hp} HP',True,(255,255,255), None)
    
    screen.blit(text_guerrero,(20, screen_height-bottom_panel + 40))
    screen.blit(text_mago,(20,screen_height-bottom_panel + 80))
    screen.blit(text_arquero,(20,screen_height-bottom_panel + 120))

running = True

current_sala = 0
selected_hero_index = 0
character_arrow = Character_arrow()
character_arrow.set_target_hero(dungeon.Heroes[selected_hero_index])

while running:
    clock.tick(fps)
    draw_bg()
    for hero in dungeon.Heroes:
        hero.draw(screen)
        hero.update()

    draw_panel()

    for enemy in dungeon.Salas[current_sala].Enemies:
        enemy.draw(screen)
        enemy.draw_hp(screen,font)
        enemy.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Cambiar la selección hacia la derecha
                selected_hero_index = (selected_hero_index + 1) % len(dungeon.Heroes)
                character_arrow.set_target_hero(dungeon.Heroes[selected_hero_index])
            if event.key == pygame.K_LEFT:
                # Cambiar la selección hacia la derecha
                selected_hero_index = (selected_hero_index - 1) % len(dungeon.Heroes)
                character_arrow.set_target_hero(dungeon.Heroes[selected_hero_index])
    character_arrow.draw(screen)
    pygame.display.update()

pygame.quit()
