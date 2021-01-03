import os
import sys
import pygame

size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
pygame.display.set_caption('BossOfGym')
clock = pygame.time.Clock()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


# all_sprites = pygame.sprite.Group()


running = True
while running:
    clock.tick(30)
    # all_sprites.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(pygame.Color("white"))
    # all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
