import pygame, pictures, Clases, consts
from Clases import character


pygame.init()

def scale_image(image, scale):
    w = image.get_width()
    
    h = image.get_height()
    
    new_image = pygame.transform.scale(image, (w*scale, h*scale))
    
    return new_image

animations = []
for i in range(11):
    img = pygame.image.load(f"Fotos\Personajes\Personaje_principal\walk{i}.png")
    img = scale_image(img, consts.CHARACTER_SCALE)
    animations.append(img)
    
player_image = pygame.image.load("Fotos\Personajes\Personaje_principal\walk1.png")
player_image = scale_image(player_image, consts.CHARACTER_SCALE)

player = character.Character(50,50,animations)


#SCREEN
screen = pygame.display.set_mode((consts.SCREEN_WIDTH,consts.SCREEN_HEIGHT))

#MOVEMENT VARAIBLES

movement_up = False
movement_down = False
movement_left = False
movement_right = False

#Framerate controller
clock = pygame.time.Clock()

pygame.draw.line(screen,(0,0,0),(20,645),(1600,645),6)
start_flag = True
while start_flag == True:
    
    clock.tick(consts.FPS)
    
    screen.fill(consts.BACKGROUND_COLOR)
    
    mov_x = 0
    mov_y = 0
    
    if movement_up == True:
        mov_y = -consts.SPEED
    if movement_down == True:
        mov_y = consts.SPEED
    if movement_left == True:
        mov_x = -consts.SPEED
    if movement_right == True:
        mov_x = consts.SPEED
    
    player.movement(mov_x, mov_y)
    
    player.update()
        
    player.draw(screen)
    
    for event in pygame.event.get():
            
        if event.type == pygame.QUIT:
            start_flag = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                movement_left = True
            if event.key == pygame.K_s:
                movement_down = True
            if event.key == pygame.K_d:
                movement_right = True
            if event.key == pygame.K_w:
                movement_up = True
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                movement_left = False
            if event.key == pygame.K_s:
                movement_down = False
            if event.key == pygame.K_d:
                movement_right = False
            if event.key == pygame.K_w:
                movement_up = False
            
    pygame.display.update()
    
pygame.quit()