import pygame
from pygame.draw import *

pygame.init()
#приготовления
FPS = 30
screen = pygame.display.set_mode((1600, 1600))
screen.fill((255, 255, 255))

#body 
circle(screen, (255, 165, 0), (800,1600), 400)
#head
ellipse(screen, (245,245,220), (500,400,600,900))
#hair
polygon(screen, (197, 0, 127), [[800,300], [870,420 ], [730,420 ]])
polygon(screen, (197, 0, 127), [[970, 350], [870, 420], [970, 490]])
polygon(screen, (197, 0, 127), [[1120, 430], [970, 490], [1050, 610]])
polygon(screen, (197, 0, 127), [[1210, 610], [1050, 610], [1090, 730]])
polygon(screen, (197, 0, 127), [[610, 350], [730, 420], [620, 490]])
polygon(screen, (197, 0, 127), [[460, 430], [620, 490], [550, 610]])
polygon(screen, (197, 0, 127), [[400,610], [550, 610], [510, 730]])
#left y
circle(screen, (0,191,255), (650,800), 100)
circle(screen, (0,0,0), (650,800), 25)
#right y
circle(screen, (0,191,255), (950,800), 100)
circle(screen, (0,0,0), (950,800), 25)
#triangles
polygon(screen, (139,69,19), [(750,900),(850,900),(800,1000)])
polygon(screen, (255,0,0), [(600,1050),(1000,1050),(800,1200)])
#arm R
polygon(screen, (245,245,220), [(1150,1350),(1200,1350),(1400,300),(1350,300)], 0)
#arm L
polygon(screen, (245,245,220), [(450,1350),(400,1350),(200,300),(250,300)], 0)
#shoulders R
polygon(screen, (255, 165, 0), [(1100,1500),(1200,1450),(1250,1350),(1100,1300),(1000,1400)], 0)
polygon(screen, (0, 0, 0), [(1100,1500),(1200,1450),(1250,1350),(1100,1300),(1000,1400)], 1)
#shoulders L
polygon(screen, (255, 165, 0), [(500,1500),(400,1450),(350,1350),(500,1300),(600,1400)], 0)
polygon(screen, (0, 0, 0), [(500,1500),(400,1450),(350,1350),(500,1300),(600,1400)], 1)
#hand R
ellipse(screen, (245,245,220), (1325,200,100,150))
#hand L
ellipse(screen, (245,245,220), (175,200,100,150))

#table
rect(screen, (100, 255, 0), (175, 150, 1250, 150))
rect(screen, (0, 0, 0), (175, 150, 1250, 150), 1)

#text
font = pygame.font.Font(None, 165)
text = font.render("PYTHON is AMAZING", True, (0, 0, 0))
text_rect = text.get_rect()
text_rect.center = (800, 240)
screen.blit(text, text_rect)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
   clock.tick(FPS)
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
          finished = True

pygame.quit()