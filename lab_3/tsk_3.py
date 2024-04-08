import pygame
from pygame.draw import *

pygame.init()
#приготовления
FPS = 30
screen = pygame.display.set_mode((3000, 2800))
screen.fill((255, 255, 255))
body_color=(0,1,0)

def pers(i ,r_b,g_b,b_b,r_h ,g_h , b_h, r_y, g_y, b_y):
    #body 
    circle(screen, (r_b,g_b,b_b) , (800+i,1600), 400)
    #head
    ellipse(screen, (245,245,220), (500+i,400,600,900))
    #hair
    polygon(screen, (r_h, g_h, b_h), [[800+i,300], [870+i,420 ], [730+i,420 ]])
    polygon(screen, (r_h, g_h, b_h), [[970+i, 350], [870+i, 420], [970+i, 490]])
    polygon(screen, (r_h, g_h, b_h), [[1120+i, 430], [970+i, 490], [1050+i, 610]])
    polygon(screen, (r_h, g_h, b_h), [[1210+i, 610], [1050+i, 610], [1090+i, 730]])
    polygon(screen, (r_h, g_h, b_h), [[610+i, 350], [730+i, 420], [620+i, 490]])
    polygon(screen, (r_h, g_h, b_h), [[460+i, 430], [620+i, 490], [550+i, 610]])
    polygon(screen, (r_h, g_h, b_h), [[400+i,610], [550+i, 610], [510+i, 730]])
    #left y
    circle(screen, (r_y,g_y,b_y), (650+i,800), 100)
    circle(screen, (0,0,0), (650+i,800), 25)
    #right y
    circle(screen, (r_y,g_y,b_y), (950+i,800), 100)
    circle(screen, (0,0,0), (950+i,800), 25)
    #triangles
    polygon(screen, (139,69,19), [(750+i,900),(850+i,900),(800+i,1000)])
    polygon(screen, (255,0,0), [(600+i,1050),(1000+i,1050),(800+i,1200)])
    #arm R
    polygon(screen, (245,245,220), [(1150+i,1350),(1200+i,1350),(1400+i,300),(1350+i,300)], 0)
    #arm L
    polygon(screen, (245,245,220), [(450+i,1350),(400+i,1350),(200+i,300),(250+i,300)], 0)
    #shoulders R
    polygon(screen, (r_b, g_b, b_b), [(1100+i,1500),(1200+i,1450),(1250+i,1350),(1100+i,1300),(1000+i,1400)], 0)
    polygon(screen, (0, 0, 0), [(1100+i,1500),(1200+i,1450),(1250+i,1350),(1100+i,1300),(1000+i,1400)], 1)
    #shoulders L
    polygon(screen, (r_b, g_b, b_b), [(500+i,1500),(400+i,1450),(350+i,1350),(500+i,1300),(600+i,1400)], 0)
    polygon(screen, (0, 0, 0), [(500+i,1500),(400+i,1450),(350+i,1350),(500+i,1300),(600+i,1400)], 1)
    #hand R
    ellipse(screen, (245,245,220), (1325+i,200,100,150))
    #hand L
    ellipse(screen, (245,245,220), (175+i,200,100,150))


pers(0,255,165,0,128,0,128,0,255,255)

pers(1350,0,128,0,255,255,0,192,192,192)

#table
rect(screen, (100, 255, 0), (175, 120, 2600, 170))
rect(screen, (0, 0, 0), (175, 120, 2600, 170), 1)

#text
font = pygame.font.Font(None, 250)
text = font.render("PYTHON is REALLY AMAZING", True, (0, 0, 0))
text_rect = text.get_rect()
text_rect.center = (1470, 220)
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