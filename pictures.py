import pygame

background1_lvl1 = pygame.image.load("Background\Background1.jpg")
background2_lvl1 = pygame.image.load("Background\Background2.jpg")
background3_lvl1 = pygame.image.load("Background\Background3.jpg")
background1_lvl1_scaled = pygame.transform.scale(background1_lvl1,(1500,600))
background2_lvl1_scaled = pygame.transform.scale(background2_lvl1,(1500,600))
background3_lvl1_scaled = pygame.transform.scale(background3_lvl1,(1500,600))

def drawBackground(background):
    
    pygame.draw.line(background,(255,0,0),(20,645),(1600,645),6)
    pygame.draw.line(background,(255,0,0),(1600,645),(1600,465),6)
    pygame.draw.line(background,(255,0,0),(1600,465),(1600,645),6)
