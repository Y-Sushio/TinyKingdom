import pygame
from source.ui.text import Text
from source.ui.button import Button
from source.windows.select_an_item import SelectAnItem


# Класс меню для выбора, создавать карту или загрузить существующую
class MapNewOrLoadMenu:
    # Инициализация параметров
    def __init__(self, screen, setting_game, audio_player, reg):
        self.next_window = 'main_window'
        self.screen = screen
        self.setting_game = setting_game
        self.audio_player = audio_player
        self.reg = reg

    # Запуск окна
    def run_window(self):
        clock = pygame.time.Clock()
        running = True
        cursor_image = self.reg.textures['ui']['cursor']['cursor']
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

        title = Text(texture=self.reg.textures['ui']['label']['label_3'],
                     text='Создать или загрузить?',
                     x=((self.setting_game.resolution[0] // 2) -
                        (self.reg.textures['ui']['label']['label_3'].get_width() // 2)),
                     y=(self.setting_game.resolution[1] * 0.10),
                     width=self.reg.textures['ui']['label']['label_3'].get_width(),
                     height=self.reg.textures['ui']['label']['label_3'].get_height(),
                     font=self.reg.fonts['Konstanting'],
                     font_size=round(40 * self.setting_game.size_k[0]),
                     center_text=True,
                     offset_text_x=0,
                     offset_text_y=self.reg.textures['ui']['label']['label_3'].get_height() * 0.05)

        button_load = Button(texture=self.reg.textures['ui']['button']['button_3'],
                             texture_motion=self.reg.textures['ui']['button']['button_3_motion'],
                             texture_press=self.reg.textures['ui']['button']['button_3_pressed'],
                             text='Загрузить существующую',
                             x=((self.setting_game.resolution[0] // 2) -
                                (self.reg.textures['ui']['button']['button_3'].get_width() // 2)),
                             y=(self.setting_game.resolution[1] * 0.25),
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

        button_new = Button(texture=self.reg.textures['ui']['button']['button_3'],
                            texture_motion=self.reg.textures['ui']['button']['button_3_motion'],
                            texture_press=self.reg.textures['ui']['button']['button_3_pressed'],
                            text='Создать новую',
                            x=((self.setting_game.resolution[0] // 2) -
                               (self.reg.textures['ui']['button']['button_3'].get_width() // 2)),
                            y=(self.setting_game.resolution[1] * 0.4),
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

        button_back = Button(texture=self.reg.textures['ui']['button']['button_3'],
                             texture_motion=self.reg.textures['ui']['button']['button_3_motion'],
                             texture_press=self.reg.textures['ui']['button']['button_3_pressed'],
                             text='Назад',
                             x=((self.setting_game.resolution[0] // 2) -
                                (self.reg.textures['ui']['button']['button_3'].get_width() // 2)),
                             y=(self.setting_game.resolution[1] * 0.7),
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
            self.screen.blit(background_frame[current_frame], (0, 0))
            mouse_pos = pygame.mouse.get_pos()
            buttons = pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.next_window = 'exit'

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        self.next_window = 'main_menu'

            if self.setting_game.show_fps:
                fps_text.draw(self.screen)

            title.draw(self.screen)

            button_load.update(buttons[0], mouse_pos)
            button_load.draw(self.screen)

            button_new.update(buttons[0], mouse_pos)
            button_new.draw(self.screen)

            button_back.update(buttons[0], mouse_pos)
            button_back.draw(self.screen)

            self.screen.blit(cursor_image, mouse_pos)

            if button_load.is_up:
                levels = dict()

                for level in self.reg.get_files('levels', 'json'):
                    levels[level['name']] = level
                select_an_item = SelectAnItem(levels, self.reg, self.setting_game, self.audio_player, 'Уровни')
                value = select_an_item.draw(self.screen)
                if value == 'EXIT_GAME':
                    running = False
                    self.next_window = 'exit'
                if value is None:
                    pass
                elif 'name' in value:
                    self.next_window = f'designer_map_{value["name"]}'
                    running = False

            if button_new.is_up:
                running = False
                self.next_window = 'designer_map'

            if button_back.is_up:
                running = False
                self.next_window = 'main_menu'

            pygame.display.flip()
            clock.tick(self.setting_game.fps)

        return self.next_window
