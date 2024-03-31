import pygame
from pygame import Rect


# Класс подбираемых предметов
class ItemPickedUp(pygame.sprite.Sprite):
    # Инициализируем параметры
    def __init__(self, x, y, block_name, texture, textures=None, is_repeat=False, time_frame=5):
        super().__init__()
        self.name = 'item_picked_up'
        self.block_name = block_name
        self.image = texture
        self.textures = textures
        self.rect = Rect(x, y, self.image.get_width(), self.image.get_height())
        self.is_repeat = is_repeat
        self.time_frame = time_frame
        self.time_i = 0
        self.current_texture = -1

    # Отрисовка объекта
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # Обновление роста объекта
    def update(self):
        if self.textures:
            if self.current_texture < len(self.textures) - 1 or self.is_repeat:
                if self.current_texture == -1:
                    self.current_texture = 0
                    self.image = self.textures[self.current_texture]
                else:
                    self.time_i += 1

                if self.time_i >= self.time_frame:
                    self.time_i = 0
                    self.current_texture += 1

                    if self.current_texture >= len(self.textures):
                        self.current_texture = 0

                    self.image = self.textures[self.current_texture]
