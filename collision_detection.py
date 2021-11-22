import pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 600, 400

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Collison detection demo")

dragon_image = pygame.image.load('dragon.png').convert_alpha()
dragon_rect = dragon_image.get_rect()
dragon_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

dragon_left = pygame.image.load("dragon_left.png").convert_alpha()
dragon_left_rect = dragon_left.get_rect()
dragon_left_rect.topleft = (10, 10)

velocity = 5

FPS = 60
clock = pygame.time.Clock()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    buttons = pygame.key.get_pressed()
    if buttons[pygame.K_LEFT] and dragon_rect.left > 0:
        dragon_rect.x -= velocity
    elif buttons[pygame.K_RIGHT] and dragon_rect.right < WINDOW_WIDTH:
        dragon_rect.x += velocity
    elif buttons[pygame.K_UP] and dragon_rect.top > 0:
        dragon_rect.y -= velocity
    elif buttons[pygame.K_DOWN] and dragon_rect.bottom < WINDOW_HEIGHT:
        dragon_rect.y += velocity

    if dragon_rect.colliderect(dragon_left_rect):
        print("HIT")

    display_surface.fill((0,0,0))
    display_surface.blit(dragon_image, dragon_rect)
    display_surface.blit(dragon_left, dragon_left_rect)
    pygame.draw.rect(display_surface, (255, 0, 0), dragon_rect, 2)
    pygame.draw.rect(display_surface, (255, 0, 0), dragon_left_rect, 2)

    pygame.display.update()
    clock.tick(FPS)
 
pygame.quit()