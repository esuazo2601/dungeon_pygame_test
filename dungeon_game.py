import pygame
from classes import *
# pygame setup
pygame.init()
clock = pygame.time.Clock()
fps = 60

#window size
bottom_panel = 250
screen_width = 1200
screen_height = 700 + bottom_panel

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Dungeon')

background_image = pygame.image.load('images/background.jpg').convert_alpha()
background_image = pygame.transform.scale(background_image,(screen_width,screen_height - bottom_panel))
#load background
panel_image = pygame.image.load('images/panel.png').convert_alpha()
panel_image = pygame.transform.scale(panel_image,(screen_width,bottom_panel))

def draw_bg():
    screen.blit(background_image,(0,0))
def draw_panel():
    screen.blit(panel_image,(0,screen_height-bottom_panel))

running = True

while running:
    clock.tick(fps)
    #drawing elements
    draw_bg()
    draw_panel()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()



pygame.quit()





