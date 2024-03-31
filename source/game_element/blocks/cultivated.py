import pygame
from pygame import Rect


# Класс выращиваемых растений
class Cultivated(pygame.sprite.Sprite):
    # Инициализируем параметры
    def __init__(self, x, y, block_name, texture_start, texture_end, food=5, rate_growth=30):
        super().__init__()
        self.name = 'cultivated'
        self.block_name = block_name
        self.image = texture_start
        self.texture_end = texture_end
        self.rect = Rect(x, y, self.image.get_width(), self.image.get_height())
        self.rate_growth = rate_growth
        self.is_growth = True
        self.food = food
        self.time_i = 0

    # Отрисовка объекта
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # Обновление роста объекта
    def update(self):
        if self.is_growth:
            self.time_i += 1
            if self.time_i >= self.rate_growth:
                self.image = self.texture_end
                self.is_growth = False
