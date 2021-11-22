import pygame


pygame.init()


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Surfaces demo")


dragon_image = pygame.image.load('dragon.png').convert_alpha()
# dragon_image.set_colorkey(BLACK)

# Трансформация
# pygame.transform.scale()
# pygame.transform.flip()
# pygame.transform.rotate()
# dragon_image = pygame.transform.rotate(dragon_image, -50)

dragon_rect = dragon_image.get_rect()
print(dragon_rect)
dragon_rect.bottom = WINDOW_HEIGHT
dragon_rect.centerx = WINDOW_WIDTH//2

second_surface = pygame.Surface((50, 80))
second_surface.fill(BLUE)
second_rect = second_surface.get_rect()
second_rect.topleft = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
# print(second_rect)

# pygame.font
# pygame.font.get_fonts()
# pygame.font.match_font()
# pygame.font.SysFont()
# pygame.font.Font()

fonts = pygame.font.get_fonts()
print(fonts)
font_path = pygame.font.match_font('Calibri')
print(font_path)

sys_font = pygame.font.SysFont('Calibri', 32)
sys_text = sys_font.render("System font demo", True, (0, 255, 0))
sys_text_rect = sys_text.get_rect()
sys_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2-100)

custom_font = pygame.font.Font('AttackGraffiti.ttf', 32)
custom_text = custom_font.render("Welcome!", True, (0, 255, 0))
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2-150)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill(WHITE)
    display_surface.blit(second_surface, second_rect)
    pygame.draw.rect(display_surface, (255, 0, 0), second_rect, 3)
    display_surface.blit(dragon_image, dragon_rect)
    pygame.draw.rect(display_surface, (255, 0, 0), dragon_rect, 3)
    display_surface.blit(sys_text, sys_text_rect)
    display_surface.blit(custom_text, custom_text_rect)
    pygame.display.update()    


pygame.quit()