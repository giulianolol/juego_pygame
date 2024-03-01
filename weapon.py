import pygame

class Weapon():
    def __init__(self, weapon_image):
        self.weapon_image = weapon_image
        self.weapon_angle = 0
        self.weapon_image = pygame.transform.rotate(self.weapon_image, self.weapon_angle)
        self.shape = self.weapon_image.get_rect()
        
    def rotate_weapon(self, rotate):
        if rotate == True:
            img_flip = pygame.transform.flip(self.weapon_image, True, False)
            self.weapon_image = pygame.transform.rotate(self.weapon_image, self.weapon_angle)
        else:
            img_flip = pygame.transform.flip(self.weapon_image, False, False)
    
    def update(self, character):
        self.shape.center = character.shape.center
        self.shape.x = self.shape.x + character.shape.width / 2 - 35
        self.shape.y = self.shape.y + character.shape.width / 2 - 45
        
    def draw(self, screen):
        screen.blit(self.weapon_image, self.shape)   