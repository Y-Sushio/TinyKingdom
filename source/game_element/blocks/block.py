import pygame.sprite
from pygame import Rect


# Класс блоков
class Block(pygame.sprite.Sprite):
    # Инициализация параметров
    def __init__(self, x, y, block_name, is_solid=True, texture=None, color=(255, 255, 255), size_block=(64, 64),
                 size_block_skeleton=(64, 64)):
        super().__init__()
        self.block_name = block_name
        if size_block[0] < size_block_skeleton[0]:
            size_block = (size_block_skeleton[0], size_block[1])
        if size_block[1] < size_block_skeleton[1]:
            size_block = (size_block[0], size_block_skeleton[1])

        if texture:
            self.image = texture
        else:
            self.image = pygame.Surface(size_block)
            self.image.fill(color)
        self.rect = Rect(x, y, self.image.get_width(), self.image.get_height())

        self.rect_skeleton = Rect(x + ((size_block[0] - size_block_skeleton[0]) // 2),
                                  y - (size_block[1] - size_block_skeleton[1]),
                                  size_block_skeleton[0],
                                  size_block_skeleton[1])
        self.is_solid = is_solid
        self.name = 'block'

    # Отрисовка блока
    def draw(self, screen):
        screen.blit(self.image, self.rect)
