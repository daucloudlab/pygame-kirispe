import pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 600, 400

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Keyboard movement demo")

dragon_image = pygame.image.load('dragon.png').convert_alpha()
dragon_rect = dragon_image.get_rect()
dragon_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

velocity = 5

FPS = 60
clock = pygame.time.Clock()

fl_left = fl_right = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                fl_left = True
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                fl_right = True
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_a, pygame.K_d]:
                fl_left = fl_right = False

    if fl_left:
        dragon_rect.x -= velocity
    elif fl_right:
        dragon_rect.x += velocity

    display_surface.fill((0,0,0))
    display_surface.blit(dragon_image, dragon_rect)

    pygame.display.update()
    clock.tick(FPS)
 
pygame.quit()