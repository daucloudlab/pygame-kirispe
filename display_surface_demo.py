import pygame


pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)
DARKGREEN = (10,50,10)

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Display Surface demo")

display_surface.fill(WHITE)
pygame.draw.line(display_surface, RED, (0,0), (100, 50), 3)
pygame.draw.aaline(display_surface, RED, (10, 50), (100, 50),3)
pygame.draw.lines(display_surface, GREEN,True, [(10, 10),(80, 50),(50, 80)],3)
pygame.draw.aalines(display_surface, BLUE,True, [(10, 10),(200, 50),(100, 100)],3)
pygame.draw.rect(display_surface, GREEN, (400, 200, 100, 100), 4)
pygame.draw.circle(display_surface, YELLOW, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 100, 2)
pygame.draw.ellipse(display_surface, YELLOW, (100, 200, 200, 100),3)
pi = 3.1415
pygame.draw.arc(display_surface, RED, (10, 100, 100, 50), pi/2, 0)
pygame.display.update()

# main loop
running = True
while running:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

pygame.quit()