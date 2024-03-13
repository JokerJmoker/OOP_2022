import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))


circle(screen, (255, 255, 0), (200, 200), 150)
circle(screen, (255, 0, 0), (125,150), 30)
circle(screen, (0, 0, 0), (125,150), 15)

circle(screen, (255, 0, 0), (275,150), 20)
circle(screen, (0, 0, 0), (275,150), 10)

polygon(screen, (0,0,0), [(100,275),(100,250),(300,250),(300,275)], 0)
###
polygon_surface=pygame.Surface((400,300), pygame.SRCALPHA)
pygame.draw.polygon(polygon_surface, (0,0,0), [(220,70),(220,45),(370,45),(370,70)], )
rotated_polygon_surface = pygame.transform.rotate(polygon_surface, 35)
screen.blit(rotated_polygon_surface, (0,0))

polygon_surface=pygame.Surface((400,300), pygame.SRCALPHA)
pygame.draw.polygon(polygon_surface, (0,0,0), [(300,200),(300,225),(550,225),(550,200)], )
rotated_polygon_surface = pygame.transform.rotate(polygon_surface, 155)
screen.blit(rotated_polygon_surface, (0,0))



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
   clock.tick(FPS)
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
          finished = True

pygame.quit()