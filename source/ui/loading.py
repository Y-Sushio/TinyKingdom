import pygame
from source.ui.text import Text


# Класс окна загрузки
class Loading:
    # Инициализация параметров
    def __init__(self, resolution, font, size_k):
        self.loading_text = Text(texture=None,
                                 text='Загрузка',
                                 x=(resolution[0] // 2) - 100,
                                 y=(resolution[1] // 2) - 100,
                                 width=200,
                                 height=200,
                                 font=font,
                                 font_size=round(40 * size_k[0]),
                                 center_text=True,
                                 offset_text_x=0,
                                 offset_text_y=0)

    # Отрисовка окна
    def draw(self, screen):
        screen.fill((0, 0, 0))
        self.loading_text.draw(screen)
        pygame.display.flip()
