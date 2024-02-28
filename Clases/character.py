import pygame, consts

class Character():

    def __init__(self, x, y, animations):
        self.flip = False
        self.animations = animations
        #Image Animation
        self.frame_index = 0
        #Here is stored the time (in miliseconds) since pygame was started
        self.update_time = pygame.time.get_ticks()
        self.character_image = animations[self.frame_index]
        self.shape = pygame.Rect(0,0,consts.CHARACTER_WIDTH, consts.CHARACTER_HEIGHT)
        self.shape.center = (x,y)
    
    def update(self):
        #Here you have (in miliseconds) the 
        animation_cooldown = 100
        self.character_image = self.animations[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= animation_cooldown:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animations):
            self.frame_index = 0
            
    def draw(self, screen):
        imagen_flip = pygame.transform.flip(self.character_image, self.flip, False)
        screen.blit(imagen_flip, self.shape)
        #pygame.draw.rect(screen, (255,255,0), self.shape, 1)
    
    def movement(self, mov_x, mov_y):
        if mov_x < 0:
            self.flip = False
        if mov_x > 0:
            self.flip = True
        
        self.shape.x = self.shape.x + mov_x
        self.shape.y = self.shape.y + mov_y

    
# def draw_character(self, screen):
#     screen.blit(self.player_image, self.player_size)
#     pygame.draw.rect(screen, (0,0,0), self.player_size)
    
# def jump(platform):
#     pass

# def verify_floor_collection(floors_list):
#     pass

# def verify_items_collection(items_list):
#     pass

# def shoot_projectile(target):
#     pass