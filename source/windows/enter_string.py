import pygame
from source.ui.text import Text


# Класс окна для ввода значения
class EnterString:
    # Инициализация параметров
    def __init__(self, value, resolution, font, size_k):
        self.value = value
        self.enter_text = Text(texture=None,
                               text=self.value,
                               x=(resolution[0] // 2) - 100,
                               y=(resolution[1] // 2) - 100,
                               width=200,
                               height=200,
                               font=font,
                               font_size=round(40 * size_k[0]),
                               center_text=True,
                               offset_text_x=0,
                               offset_text_y=0)

        self.title = Text(texture=None,
                          text='Введите текст',
                          x=(resolution[0] // 2) - 100,
                          y=(resolution[1] // 2) - self.enter_text.rect.height,
                          width=200,
                          height=200,
                          font=font,
                          font_size=round(40 * size_k[0]),
                          center_text=True,
                          offset_text_x=0,
                          offset_text_y=0)

    # Отрисовка окна
    def draw(self, screen):
        access_unicode = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        access_unicode += "йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
        access_unicode += "1234567890_"
        pygame.key.set_repeat(1000, 1000)
        running = True
        while running:
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.value = 'EXIT_GAME'

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        self.value = None

                    if event.key == pygame.K_RETURN:
                        if len(self.value) > 0:
                            running = False

                    if event.key == pygame.K_BACKSPACE:
                        if len(self.value):
                            self.value = self.value[:-1]

                    if event.unicode in access_unicode and len(self.value) < 30:
                        self.value += event.unicode

            self.enter_text.text = self.value
            self.title.draw(screen)
            self.enter_text.draw(screen)
            pygame.display.flip()
        pygame.key.set_repeat(5000, 5000)
        return self.value
