import os
import sys
import pygame

SIZE = WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('BossOfGym')
clock = pygame.time.Clock()

def load_image(name, colorkey=None):
    fullname = os.path.join('sprites', name)
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


class Platform1(pygame.sprite.Sprite):
    image = load_image("level1/Платформа1.png")
    image = pygame.transform.scale(image, (600, 300))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Platform1.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = HEIGHT - 300


class Platform2(pygame.sprite.Sprite):
    image = load_image("level1/Платформа2.png")
    image = pygame.transform.scale(image, (432, 155))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Platform2.image
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = HEIGHT - 155


all_sprites = pygame.sprite.Group()
Platform1(all_sprites)
Platform2(all_sprites)

running = True
while running:
    clock.tick(30)
    # all_sprites.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(pygame.Color("white"))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()