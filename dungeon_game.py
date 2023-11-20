import pygame
from heroes import Guerrero,Mago,Arquero
from enemies import Esqueleto, Orco, Bandido, Zombie
from others import Character_arrow, Dungeon, Sala, Skill_arrow, Enemy_arrow
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
knight = Guerrero(120,300,10,5)
knight.add_Habilidad(2,"Espadazo")
knight.add_Habilidad(3,"Rodillazo")

mago = Mago(knight.get_x()+120,knight.get_y()-50,10,5)
mago.add_Habilidad(2,"Bola de fuego")

arquero = Arquero(mago.get_x()+60,knight.get_y(),10,10)
arquero.add_Habilidad(3, "Flechazo")

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
current_sala = 0
selected_hero_index = 0
selected_enemy_index = 0

character_arrow = Character_arrow()
skill_arrow = Skill_arrow()
enemy_arrow = Enemy_arrow()

character_arrow.set_target_hero(dungeon.Heroes[selected_hero_index])
enemy_arrow.set_target_enemy(dungeon.Salas[current_sala].Enemies[selected_enemy_index])

ally_turn = True
confirmed_skill = False
selected_skill_index = 0
confirmed_hero = False

def draw_bg():
    screen.blit(background_image,(0,0))
def draw_panel():
    screen.blit(panel_image, (0, screen_height - bottom_panel))

    health_guerrero = font.render(f'Guerrero: {dungeon.Heroes[0].hp} HP', True, (255, 255, 255), None)
    health_mago = font.render(f'Mago: {dungeon.Heroes[1].hp} HP', True, (255, 255, 255), None)
    health_arquero = font.render(f'Arquera: {dungeon.Heroes[2].hp} HP', True, (255, 255, 255), None)

    screen.blit(health_guerrero, (20, screen_height - bottom_panel + 40))
    screen.blit(health_mago, (20, screen_height - bottom_panel + 80))
    screen.blit(health_arquero, (20, screen_height - bottom_panel + 120))

    skills_hero = dungeon.Heroes[selected_hero_index].Habilidades
    separation = 0  # Mueve esta línea fuera del bucle
    for skill in skills_hero:
        dmg = skill.daño[0] * dungeon.Heroes[selected_hero_index].get_dmg()
        skill_desc = f'{skill.nombre} : {dmg} DMG'
        render = font.render(skill_desc, True, (255, 255, 0), None)
        screen.blit(render, (20 + screen_width // 2, screen_height - bottom_panel + 40 + separation))
        separation += 40



running = True
while running:
    clock.tick(fps)
    draw_bg()
    for hero in dungeon.Heroes:
        hero.draw(screen)
        hero.update(100)

    draw_panel()

    for enemy_index, enemy in enumerate(dungeon.Salas[current_sala].Enemies):
        enemy.draw(screen)
        enemy.draw_hp(screen, font)
        enemy.update(200)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if ally_turn == True:
            if confirmed_hero == False:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        # Cambiar la selección hacia la derecha
                        selected_hero_index = (selected_hero_index + 1) % len(dungeon.Heroes)
                        character_arrow.set_target_hero(dungeon.Heroes[selected_hero_index])
                    if event.key == pygame.K_LEFT:
                        # Cambiar la selección hacia la izquierda
                        selected_hero_index = (selected_hero_index - 1) % len(dungeon.Heroes)
                        character_arrow.set_target_hero(dungeon.Heroes[selected_hero_index])
                    if event.key == pygame.K_z:
                        confirmed_hero = True
            elif confirmed_hero == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        selected_skill_index = (selected_skill_index + 1) % len(dungeon.Heroes[selected_hero_index].Habilidades)
                    elif event.key == pygame.K_UP:
                        selected_skill_index = (selected_skill_index - 1) % len(dungeon.Heroes[selected_hero_index].Habilidades)
                    if event.key == pygame.K_z:
                        confirmed_skill = True
                        print(confirmed_skill)

            if confirmed_hero == True and confirmed_skill == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        selected_enemy_index = (selected_enemy_index - 1) % len(dungeon.Salas[current_sala].Enemies)
                        selected_enemy = dungeon.Salas[current_sala].Enemies[selected_enemy_index]
                        enemy_arrow.set_target_enemy(selected_enemy)
                    elif event.key == pygame.K_LEFT:
                        selected_enemy_index = (selected_enemy_index + 1) % len(dungeon.Salas[current_sala].Enemies)
                        selected_enemy = dungeon.Salas[current_sala].Enemies[selected_enemy_index]
                        enemy_arrow.set_target_enemy(selected_enemy)
                    elif event.key == pygame.K_x:
                        # Confirma el enemigo seleccionado y realiza la acción
                        selected_enemy = dungeon.Salas[current_sala].Enemies[selected_enemy_index]
                        hero_selected = dungeon.Heroes[selected_hero_index]
                        skill_selected = dungeon.Heroes[selected_hero_index].Habilidades[selected_skill_index]
                        hero_selected.attack(selected_enemy, skill_selected)
                        print(f"Atacar al enemigo {selected_enemy_index + 1} con la habilidad {selected_skill_index + 1}")
                        # Restablece las variables de selección
                        confirmed_hero = False
                        confirmed_skill = False
                        selected_enemy_index = 0
                        selected_skill_index = 0
                        #ally_turn = False
                        
    if confirmed_hero == True and ally_turn == True:
        skill_arrow.draw(screen, 330 + screen_width // 2, screen_height - bottom_panel + 40 + selected_skill_index * 40)

    if confirmed_hero and confirmed_skill and ally_turn:
        enemy_arrow.draw(screen)
    
    character_arrow.draw(screen)
    pygame.display.update()

pygame.quit()

