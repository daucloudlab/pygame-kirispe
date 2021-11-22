import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Sound effects and musics demo")

# pygame.mixer.Sound()
# pygame.mixer.music

sound_1 = pygame.mixer.Sound('sound_1.wav')
sound_1.play()

pygame.time.delay(5000)

sound_2 = pygame.mixer.Sound('sound_2.wav')
sound_2.play()

pygame.time.delay(5000)
sound_2.set_volume(0.2)
sound_2.play()

pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1, 0.0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()    

pygame.quit()