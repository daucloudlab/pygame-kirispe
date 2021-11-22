import pygame


pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Display Surface demo")

# main loop
running = True
while running:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

pygame.quit()