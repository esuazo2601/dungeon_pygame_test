import pygame
import random
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

#load background
background_image = pygame.image.load('images/Dungeon/background.jpg').convert_alpha()
background_image = pygame.transform.scale(background_image,(screen_width,screen_height - bottom_panel))
#load panel
panel_image = pygame.image.load('images/Dungeon/panel.png').convert_alpha()
panel_image = pygame.transform.scale(panel_image,(screen_width,bottom_panel))
#load win
win_imge = pygame.image.load('images/victory.png').convert_alpha()
#load defeat
def_imge = pygame.image.load('images/defeat.png').convert_alpha()
#load exit
exit_image = pygame.image.load('images/exit.png').convert_alpha()
exit_image = pygame.transform.scale(exit_image,(screen_width,screen_height - bottom_panel))
################################ ESTA PARTE CAMBIA DEPENDIENDO DE LA INSTANCIA #########################
dungeon = Dungeon()

# Heroes
heroes_list = []
knight = Guerrero(x=120, y=300, max_hp=40, fuerza=5)
knight.add_Habilidad(2, "Espadazo")
knight.add_Habilidad(3, "Rodillazo")

mago = Mago(x=knight.get_x() + 120, y=knight.get_y() - 50, max_hp=40, poder_magico=5)
mago.add_Habilidad(2, "Bola de fuego")

arquero = Arquero(x=mago.get_x() + 60, y=knight.get_y(), max_hp=40, precision=10)
arquero.add_Habilidad(3, "Flechazo")

heroes_list.append(knight)
heroes_list.append(mago)
heroes_list.append(arquero)

dungeon.addHeroes(heroes_list)

# Enemies
sala0 = Sala(0)
sala1 = Sala(1)

bandido0 = Bandido(x=screen_width - 70, y=300, max_hp=10, daño=2)
bandido0.addAtaque(2, "Espadazo")
sala0.addEnemy(bandido0)

# Orco con un ataque llamado "Hachazo"
orco0 = Orco(x=bandido0.get_x() - 100, y=bandido0.get_y() - 30, max_hp=10, daño=3)
orco0.addAtaque(2, "Hachazo")
sala0.addEnemy(orco0)

# Zombie con un ataque llamado "Mordida"
zombie0 = Zombie(x=screen_width - 70, y=300, max_hp=10, daño=10)
zombie0.addAtaque(2, "Mordida")
sala1.addEnemy(zombie0)

# Esqueleto con un ataque llamado "Lanzamiento de craneo"
esqueleto0 = Esqueleto(x=zombie0.get_x() - 100, y=zombie0.get_y() - 30, max_hp=10, daño=8)
esqueleto0.addAtaque(2, "Lanzamiento de craneo")
sala1.addEnemy(esqueleto0)

sala0.sala_siguiente = sala1
salida = Sala(2)
sala1.sala_siguiente = salida

dungeon.addSala(sala0)
dungeon.addSala(sala1)
dungeon.addSalida(salida)
################################ ESTA PARTE CAMBIA DEPENDIENDO DE LA INSTANCIA #########################
current_sala = sala0
selected_hero_index = 0
selected_skill_index = 0
selected_enemy_index = 0

character_arrow = Character_arrow()
skill_arrow = Skill_arrow()
enemy_arrow = Enemy_arrow()

character_arrow.set_target_hero(dungeon.Heroes[selected_hero_index])
enemy_arrow.set_target_enemy(current_sala.Enemies[selected_enemy_index])

ally_turn = True
confirmed_skill = False
confirmed_hero = False
confirmed_attack = False
total_salas = len(dungeon.Salas)

def draw_bg():
    screen.blit(background_image,(0,0))
    num_sala = font.render(f'Sala: {current_sala.num}', True, (0, 255, 255), None)
    screen.blit(num_sala, (screen_width // 2 - 20,  100))
def draw_panel():
    screen.blit(panel_image, (0, screen_height - bottom_panel))

    sep = 0
    for hero in dungeon.Heroes:
        render = font.render(f'{hero.__class__.__name__}: {hero.hp} HP', True, (255, 255, 255), None)
        screen.blit(render, (20, screen_height - bottom_panel + 40 + sep))
        sep += 40

    
    if len(dungeon.Heroes) > 0:  
        selected_hero = dungeon.Heroes[selected_hero_index]
        if selected_hero.vivo == True:  # Verifica si el héroe seleccionado está vivo
            skills_hero = selected_hero.Habilidades
            separation = 0
            for skill in skills_hero:
                dmg = selected_hero.get_dmg() + skill.daño[0]
                skill_desc = f'{skill.nombre} : {dmg} DMG'
                render = font.render(skill_desc, True, (255, 255, 0), None)
                screen.blit(render, (20 + screen_width // 2, screen_height - bottom_panel + 40 + separation))
                separation += 40


damage_text_group = pygame.sprite.Group()

running = True
while running:
    clock.tick(fps)
    draw_bg()
    
    for hero in dungeon.Heroes:
        if hero.hp > 0:
            hero.update(100)
            hero.draw(screen)
        elif hero.hp <= 0: 
            hero.vivo = False
            dungeon.Heroes.remove(hero)
            selected_hero_index = 0


    draw_panel()

    for enemy in current_sala.Enemies:
        if enemy.hp > 0:
            enemy.draw(screen)
            enemy.draw_hp(screen, font)
            enemy.update(200)
        if enemy.hp <= 0:
            current_sala.Enemies.remove(enemy)
            if len(current_sala.Enemies) > 0:
                enemy_arrow.set_target_enemy(selected_enemy_index % len(current_sala.Enemies))
    
    damage_text_group.update()
    damage_text_group.draw(screen)

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
                        if len(dungeon.Heroes) > 0:
                            selected_hero_index = (selected_hero_index - 1) % len(dungeon.Heroes)
                            character_arrow.set_target_hero(dungeon.Heroes[selected_hero_index])
                    if event.key == pygame.K_z:
                        confirmed_hero = True
            
            elif confirmed_hero == True and len(dungeon.Heroes) > 0:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        selected_skill_index = (selected_skill_index + 1) % len(dungeon.Heroes[selected_hero_index].Habilidades)
                    elif event.key == pygame.K_UP:
                        selected_skill_index = (selected_skill_index - 1) % len(dungeon.Heroes[selected_hero_index].Habilidades)
                    if event.key == pygame.K_z:
                        confirmed_skill = True

            if confirmed_hero == True and confirmed_skill == True and len(current_sala.Enemies) > 0:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        selected_enemy_index = (selected_enemy_index - 1) % len(current_sala.Enemies)
                        selected_enemy = current_sala.Enemies[selected_enemy_index]
                        enemy_arrow.set_target_enemy(selected_enemy)
                    elif event.key == pygame.K_LEFT:
                        selected_enemy_index = (selected_enemy_index + 1) % len(current_sala.Enemies)
                        selected_enemy = current_sala.Enemies[selected_enemy_index]
                        enemy_arrow.set_target_enemy(selected_enemy)
                    elif event.key == pygame.K_x:
                        # Confirma el enemigo seleccionado y realiza la acción
                        selected_enemy = current_sala.Enemies[selected_enemy_index]
                        hero_selected = dungeon.Heroes[selected_hero_index]
                        skill_selected = hero_selected.Habilidades[selected_skill_index]
                        hero_selected.attack(selected_enemy, skill_selected, damage_text_group, font)

                        type_of_enemy = selected_enemy.__class__.__name__
                        type_of_ally = hero_selected.__class__.__name__

                        # Restablece las variables de selección 
                        confirmed_hero = False    
                        confirmed_skill = False
                        selected_enemy_index = 0
                        selected_skill_index = 0
                        ally_turn = False

                        
    if confirmed_hero == True and ally_turn == True:
        skill_arrow.draw(screen, 330 + screen_width // 2, screen_height - bottom_panel + 40 + selected_skill_index * 40)

    if confirmed_hero and confirmed_skill and ally_turn:
        enemy_arrow.draw(screen)
    
    if ally_turn == True:
        character_arrow.draw(screen)

    if current_sala.check_terminada() == True:
        if current_sala.sala_siguiente:
            current_sala = current_sala.sala_siguiente
            print(current_sala.num) 

    if current_sala == salida:
        screen.blit(exit_image,(0,0))

        for hero in dungeon.Heroes:
            if hero.hp > 0:
                hero.update(100)
                hero.draw(screen)
        screen.blit(win_imge,(screen_width//2 - 120, 120))

    if len (dungeon.Heroes) <= 0:
        screen.blit(def_imge,(screen_width//2 - 120, 120))

    if not ally_turn:
        random_enemy_index = random.randint(0,len (current_sala.Enemies)-1)
        random_ally_index = random.randint(0,len(dungeon.Heroes)-1)
        
        enemy_selected = current_sala.Enemies[random_enemy_index]
        ally_selected = dungeon.Heroes[random_ally_index]

        enemy_selected.attack(ally_selected, damage_text_group, font)

        ally_turn = True

    pygame.display.update()

pygame.quit()

