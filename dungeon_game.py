import pygame
from heroes import Guerrero,Mago,Arquero
from enemies import Esqueleto, Orco, Bandit, Zombie
# pygame setup
pygame.init()
clock = pygame.time.Clock()
fps = 60

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

def draw_bg():
    screen.blit(background_image,(0,0))
def draw_panel():
    screen.blit(panel_image,(0,screen_height-bottom_panel))

#Heroes
knight = Guerrero(120,300,10,10)
mago = Mago(knight.get_x()+100,knight.get_y()+20,10,10)
arquero = Arquero(mago.get_x()+100,knight.get_y(),10,10)
#Enemies
bandit = Bandit(screen_width - 70,300,10,10)
orc = Orco(bandit.get_x()-100,bandit.get_y()+30,10,10)
zombie = Zombie(orc.get_x()-120,orc.get_y()-20,10,10)
esqueleto = Esqueleto(zombie.get_x()-90,zombie.get_y()-10,10,10)

running = True

while running:
    clock.tick(fps)
    #drawing elements
    draw_bg()
    draw_panel()
    knight.draw(screen)
    mago.draw(screen)
    arquero.draw(screen)


    bandit.draw(screen)
    orc.draw(screen)
    zombie.draw(screen)
    esqueleto.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()


pygame.quit()
