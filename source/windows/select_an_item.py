import math
import pygame
from source.ui.text import Text
from source.ui.button import Button
from source.ui.values_switch import ValuesSwitch


# Класс окна для выбора из списка
class SelectAnItem:
    # Инициализация параметров
    def __init__(self, elements, reg, setting_game, audio_player, title='Перебор', current_page=None):
        self.reg = reg
        self.elements = dict()
        if 'is_many' in elements.keys():
            for key, value in elements.items():
                if key == 'is_many':
                    continue
                else:
                    self.elements.update(value)
        else:
            self.elements = elements
        self.setting_game = setting_game
        self.audio_player = audio_player
        self.value = None
        self.max_element_page = 25
        self.pages_count = math.ceil(len(self.elements.keys()) / self.max_element_page)
        self.current_page = 1 if self.pages_count else 0
        if current_page and self.pages_count > 0 and isinstance(current_page, int):
            self.current_page = current_page
        self.title = title

    # Создание страницы
    def create_page(self):
        x = 0
        y = 0
        i_count = 0
        step_down = self.reg.textures['ui']['button']['button_3_motion'].get_height()
        step_right = self.reg.textures['ui']['button']['button_3_motion'].get_width()
        list_element = []
        for key, value in self.elements.items():
            if self.max_element_page <= i_count:
                y = 0
                x = 0
                i_count = 0

            y += step_down
            if y > self.setting_game.resolution[1] * 0.85:
                x += step_right
                y = step_down
            button_ui = Button(texture=self.reg.textures['ui']['button']['button_3'],
                               texture_motion=self.reg.textures['ui']['button']['button_3_motion'],
                               texture_press=self.reg.textures['ui']['button']['button_3_pressed'],
                               text=value['name'],
                               x=x,
                               y=y,
                               width=self.reg.textures['ui']['button']['button_3'].get_width(),
                               height=self.reg.textures['ui']['button']['button_3'].get_height(),
                               font=self.reg.fonts['Konstanting'],
                               font_size=round(40 * self.setting_game.size_k[0]),
                               center_text=True,
                               offset_text_x=0,
                               offset_text_y=self.reg.textures['ui']['button']['button_3'].get_height() * 0.15,
                               offset_text_press_x=0,
                               offset_text_press_y=self.reg.textures['ui']['button']['button_3'].get_height() * 0.1,
                               audio_player=self.audio_player)
            list_element.append({
                'button': button_ui,
                'info': value
            })
            i_count += 1
        return list_element[
               ((self.current_page - 1) * self.max_element_page):(self.current_page * self.max_element_page)]

    # Отрисовка страницы
    def draw(self, screen):
        clock = pygame.time.Clock()
        title_text = Text(texture=self.reg.textures['ui']['label']['label_3'],
                          text=self.title,
                          x=((self.setting_game.resolution[0] // 2) -
                             (self.reg.textures['ui']['label']['label_3'].get_width() // 2)),
                          y=(self.setting_game.resolution[1] * 0.01),
                          width=self.reg.textures['ui']['label']['label_3'].get_width(),
                          height=self.reg.textures['ui']['label']['label_3'].get_height(),
                          font=self.reg.fonts['Konstanting'],
                          font_size=round(40 * self.setting_game.size_k[0]),
                          center_text=True,
                          offset_text_x=0,
                          offset_text_y=self.reg.textures['ui']['label']['label_3'].get_height() * 0.05)

        pages_text = Text(texture=self.reg.textures['ui']['label']['label_3'],
                          text=f'{self.current_page}/{self.pages_count}',
                          x=(self.setting_game.resolution[0] - self.reg.textures['ui']['label'][
                              'label_3'].get_width() * 1.5),
                          y=(self.setting_game.resolution[1] - self.reg.textures['ui']['label'][
                              'label_3'].get_height() * 2),
                          width=self.reg.textures['ui']['label']['label_3'].get_width(),
                          height=self.reg.textures['ui']['label']['label_3'].get_height(),
                          font=self.reg.fonts['Konstanting'],
                          font_size=round(40 * self.setting_game.size_k[0]),
                          center_text=True,
                          offset_text_x=0,
                          offset_text_y=self.reg.textures['ui']['label']['label_3'].get_height() * 0.05)

        page_switch = ValuesSwitch(texture=self.reg.textures['ui']['label']['label_3'],
                                   values=[str(i) for i in range(1, self.pages_count + 1, 1)],
                                   select_value=str(self.current_page),
                                   x=(self.setting_game.resolution[0] - self.reg.textures['ui']['label'][
                                       'label_3'].get_width() * 1.5),
                                   y=(self.setting_game.resolution[1] - self.reg.textures['ui']['label'][
                                       'label_3'].get_height()),
                                   width=self.reg.textures['ui']['label']['label_3'].get_width(),
                                   height=self.reg.textures['ui']['label']['label_3'].get_height(),
                                   font=self.reg.fonts['Konstanting'],
                                   font_size=round(40 * self.setting_game.size_k[0]),
                                   center_text=True,
                                   offset_text_x=0,
                                   offset_text_y=self.reg.textures['ui']['label'][
                                                     'label_3'].get_height() * 0.05,
                                   texture_button=self.reg.textures['ui']['button']['button_1'],
                                   texture_button_motion=self.reg.textures['ui']['button']['button_1_motion'],
                                   texture_button_press=self.reg.textures['ui']['button']['button_1_pressed'],
                                   offset_text_press_x=0,
                                   offset_text_press_y=self.reg.textures['ui']['button'][
                                                           'button_3'].get_height() * 0.1,
                                   audio_player=self.audio_player)

        button_back = Button(texture=self.reg.textures['ui']['button']['button_3'],
                             texture_motion=self.reg.textures['ui']['button']['button_3_motion'],
                             texture_press=self.reg.textures['ui']['button']['button_3_pressed'],
                             text='Назад',
                             x=(self.setting_game.resolution[0] - self.reg.textures['ui']['label'][
                                 'label_3'].get_width()),
                             y=(self.setting_game.resolution[1] * 0.01),
                             width=self.reg.textures['ui']['button']['button_3'].get_width(),
                             height=self.reg.textures['ui']['button']['button_3'].get_height(),
                             font=self.reg.fonts['Konstanting'],
                             font_size=round(40 * self.setting_game.size_k[0]),
                             center_text=True,
                             offset_text_x=0,
                             offset_text_y=self.reg.textures['ui']['button']['button_3'].get_height() * 0.15,
                             offset_text_press_x=0,
                             offset_text_press_y=self.reg.textures['ui']['button']['button_3'].get_height() * 0.1,
                             audio_player=self.audio_player)

        if self.setting_game.show_fps:
            fps_text = Text(texture=None,
                            text=str(round(clock.get_fps())),
                            x=0,
                            y=0,
                            width=self.setting_game.resolution[0] // 10,
                            height=self.setting_game.resolution[1] // 10,
                            font=self.reg.fonts['Konstanting'],
                            font_size=round(40 * self.setting_game.size_k[0]),
                            center_text=False,
                            offset_text_x=0,
                            offset_text_y=0)

        list_element = self.create_page()

        cursor_image = self.reg.textures['ui']['cursor']['cursor']
        clock = pygame.time.Clock()
        running = True
        background_frame = self.reg.textures['ui']['background_menu']
        background_frame = [value for value in background_frame.values()]
        i_next_frame = 2 * self.setting_game.fps_k
        i = -1
        current_frame = 0
        while running:
            if i >= i_next_frame:
                if self.setting_game.show_fps:
                    fps_text.set_text(str(int(clock.get_fps())))
                i = 0
                current_frame += 1
                current_frame %= len(background_frame)
            else:
                i += 1
            screen.blit(background_frame[current_frame], (0, 0))
            is_click = False
            mouse_pos = pygame.mouse.get_pos()
            buttons = pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.value = 'EXIT_GAME'

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        self.value = None

                if event.type == pygame.MOUSEBUTTONDOWN:
                    is_click = True

            for item in list_element:
                item['button'].update(buttons[0], mouse_pos)
                item['button'].draw(screen)
                if 'texture' in item['info'].keys():
                    screen.blit(item['info']['texture'], item['button'].rect)

                if 'texture_start' in item['info'].keys():
                    screen.blit(item['info']['texture_start'], item['button'].rect)

                if 'anim' in item['info'].keys():
                    if 'idle_right' in item['info']['anim'].keys():
                        screen.blit(item['info']['anim']['idle_right'][0]['texture'], item['button'].rect)

                if item['button'].is_up:
                    self.value = item['info']
                    running = False

            title_text.draw(screen)

            pages_text.draw(screen)
            page_switch.update(is_click, mouse_pos)
            page_switch.draw(screen)

            button_back.update(is_click, mouse_pos)
            button_back.draw(screen)

            if button_back.is_up:
                running = False
                self.value = None

            if page_switch.get_value() and self.current_page != int(page_switch.get_value()):
                self.current_page = int(page_switch.get_value())
                list_element = self.create_page()
            pages_text.set_text(f'{self.current_page}/{self.pages_count}')

            screen.blit(cursor_image, mouse_pos)
            pygame.display.flip()
            clock.tick(self.setting_game.fps)
        return self.value
