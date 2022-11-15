import pygame
import sys
from pygame.locals import *

pygame.init()

FPS = 30
W = 300
H = 300

screen = pygame.display.set_mode((W, H), HWSURFACE | DOUBLEBUF | RESIZABLE)
pygame.display.set_caption('ТЕСТИРОВАНИЕ')

clock = pygame.time.Clock()

picture = pygame.image.load("image/fon_sc.png").convert_alpha()
picture = pygame.transform.scale(picture, (110, 110))
rect = picture.get_rect()
rect = rect.move((20, 20))
screen.fill((230,230,230))
screen.blit(picture, rect)
# rect = pygame.draw.rect(screen,(255,200,200),(20,20,110,110))
# pygame.display.flip()


while 1:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((230,230,230))
    screen.blit(picture, rect)
    pygame.display.update(rect)