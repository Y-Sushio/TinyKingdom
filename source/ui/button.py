from source.ui.text import Text


# Класс кнопки
class Button(Text):
    # Инициализация параметров
    def __init__(self, texture, texture_motion, texture_press, text, x, y, width, height, font, font_size,
                 center_text, offset_text_x, offset_text_y, offset_text_press_x, offset_text_press_y,
                 audio_player):
        super().__init__(texture, text, x, y, width, height, font, font_size, center_text, offset_text_x, offset_text_y)
        self.is_pressed = False
        self.is_motion = False
        self.image_motion = texture_motion
        self.image_press = texture_press
        self.offset_text_x = offset_text_x
        self.offset_text_y = offset_text_y
        self.offset_text_press_x = offset_text_press_x
        self.offset_text_press_y = offset_text_press_y
        self.audio_player = audio_player
        self.is_up = False
        self.call = False

    # Отрисовка кнопки
    def draw(self, screen):
        if self.is_pressed:
            screen.blit(self.image_press, self.rect)
        elif self.is_motion:
            screen.blit(self.image_motion, self.rect)
        else:
            screen.blit(self.image, self.rect)

        text_render = self.font.render(self.text, True, self.inverse_color(self.text_color))
        if self.center_text:
            text_rect = text_render.get_rect(center=self.rect.center)
        else:
            text_rect = text_render.get_rect()
        if not self.is_pressed:
            text_rect.y -= self.offset_text_y
        else:
            text_rect.y -= (self.offset_text_y - self.offset_text_press_y)
        text_rect.y += self.font_size // 16
        text_rect.x += self.font_size // 16
        text_rect.x -= self.offset_text_x
        screen.blit(text_render, text_rect)

        text_render = self.font.render(self.text, True, self.text_color)
        if self.center_text:
            text_rect = text_render.get_rect(center=self.rect.center)
        else:
            text_rect = text_render.get_rect()
        if not self.is_pressed:
            text_rect.y -= self.offset_text_y
        else:
            text_rect.y -= (self.offset_text_y - self.offset_text_press_y)
        screen.blit(text_render, text_rect)

    # Обновление кнопки по событиям
    def update(self, is_click, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            if is_click:
                if not self.is_pressed and self.audio_player:
                    self.audio_player.play_sound('button_press')
                self.is_pressed = True
            else:
                self.is_up = False
                if self.is_pressed:
                    self.is_up = True
                self.is_pressed = False
                self.is_motion = True
        else:
            self.is_pressed = False
            self.is_motion = False
            self.is_up = False
