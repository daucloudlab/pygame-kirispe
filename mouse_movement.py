import pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 600, 400

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Mouse movement demo")

dragon_image = pygame.image.load('dragon.png').convert_alpha()
dragon_rect = dragon_image.get_rect()
dragon_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

velocity = 5

FPS = 60
clock = pygame.time.Clock()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pressed = pygame.mouse.get_pressed()
    if pressed[0] == 1:
        pos = pygame.mouse.get_pos()
        dragon_rect.center = (pos[0], pos[1])
        

    display_surface.fill((0, 0, 0))
    display_surface.blit(dragon_image, dragon_rect)

    pygame.display.update()
    clock.tick(FPS)
 
pygame.quit()