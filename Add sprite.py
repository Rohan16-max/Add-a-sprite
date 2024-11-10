import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 800, 600


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame Rectangles')



cyan = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


RECT_WIDTH, RECT_HEIGHT = 50, 50


rect1_x, rect1_y = 200, 200  
rect2_x, rect2_y = 100, 100  


speed = 8


running = True
while running:
    screen.fill(cyan)

    
    pygame.draw.rect(screen, RED, (rect1_x, rect1_y, RECT_WIDTH, RECT_HEIGHT))  
    pygame.draw.rect(screen, BLUE, (rect2_x, rect2_y, RECT_WIDTH, RECT_HEIGHT))  

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect2_x -= speed
    if keys[pygame.K_RIGHT]:
        rect2_x += speed
    if keys[pygame.K_UP]:
        rect2_y -= speed
    if keys[pygame.K_DOWN]:
        rect2_y += speed

    
    rect2_x = max(0, min(rect2_x, WIDTH - RECT_WIDTH))
    rect2_y = max(0, min(rect2_y, HEIGHT - RECT_HEIGHT))

    # Update the screen
    pygame.display.flip()

    
    pygame.time.Clock().tick(60)


pygame.quit()
sys.exit()
