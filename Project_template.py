import pygame
import sys

class Hurdle:
    # Insert the method name
    def       (self, x, y, h, w):
        self.rect = pygame.Rect(x, y, h, w)
    
    def draw_hurdle(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)
    
    def paste_image(self, image):
        screen.blit(image, (self.rect.x, self.rect.y-14))

class Thief:
    # Insert the method name
    def        (self, x, y, h, w):
        self.rect = pygame.Rect(x, y, h, w)
    
    def draw_thief(self, surface):
        pygame.draw.rect(surface, (109,23,230), self.rect)
    
    def paste_image(self, image):
        screen.blit(image, self.rect)
        
pygame.init()
screen = pygame.display.set_mode((400, 400))
font = pygame.font.Font("freesansbold.ttf", 16)

hurdle_1 = Hurdle(0, 200, 200, 2)
#Create a second object of the Hurdle Class at coordinates 200,198.
hurdle_2 = 

hurdle_change = 1

#Load the hurdle image
hurdle_img = pygame.image.load("          ")
hurdle_img = pygame.transform.scale(hurdle_img, (200,25))

thief = Thief(10, 380, 15, 15)
thief_x_change = 0
thief_y_change = 0

jewel = pygame.Rect(350, 10, 40, 40)

#Load the jewel image
jewel_image = pygame.image.load("       ")
jewel_image = pygame.transform.scale(jewel_image, (50,50))

while True:
    screen.fill((100,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    thief_x_change = -1
                if event.key == pygame.K_RIGHT:
                    thief_x_change = 1
                if event.key == pygame.K_DOWN:
                    thief_y_change = 1
                if event.key == pygame.K_UP:
                    thief_y_change = -1
        if event.type == pygame.KEYUP:
            thief_x_change = 0
            thief_y_change = 0
                    
    thief.rect.x += thief_x_change
    thief.rect.y += thief_y_change
    
    if hurdle_1.rect.y > 398:
        hurdle_change = -1
    elif hurdle_1.rect.y < 0:
        hurdle_change = 1
    
    hurdle_1.rect.y += hurdle_change
    hurdle_2.rect.y -= hurdle_change
    
    hurdle_1.paste_image(hurdle_img)
    hurdle_2.paste_image(hurdle_img)
    thief.draw_thief(screen)
    screen.blit(jewel_image, jewel)
    
    if hurdle_1.rect.colliderect(thief.rect) or hurdle_2.rect.colliderect(thief.rect):
        text = font.render("Failed, you lost", True, (0,0,0))
        screen.blit(text, (125,175))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()
    #Check if theif collided with jewel
    if thief.rect.          (jewel):
        text = font.render("Congratulations, you won", True, (0,0,0))
        screen.blit(text, (125,175))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()
    
    pygame.display.update()
    pygame.time.delay(10)
