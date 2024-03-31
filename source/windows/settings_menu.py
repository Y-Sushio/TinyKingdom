import pygame
from source.ui.text import Text
from source.ui.button import Button
from source.ui.value_switch import ValueSwitch
from source.ui.values_switch import ValuesSwitch


# Класс меню настроек
class SettingsMenu:
    # Инициализация параметров
    def __init__(self, screen, setting_game, audio_player, reg):
        self.next_window = 'main_window'
        self.screen = screen
        self.setting_game = setting_game
        self.audio_player = audio_player
        self.reg = reg
        self.data_save = None

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
                     text='Настройки',
                     x=((self.setting_game.resolution[0] // 2) -
                        (self.reg.textures['ui']['label']['label_3'].get_width() // 2)),
                     y=-(self.setting_game.resolution[1] * 0.005),
                     width=self.reg.textures['ui']['label']['label_3'].get_width(),
                     height=self.reg.textures['ui']['label']['label_3'].get_height(),
                     font=self.reg.fonts['Konstanting'],
                     font_size=round(40 * self.setting_game.size_k[0]),
                     center_text=True,
                     offset_text_x=0,
                     offset_text_y=self.reg.textures['ui']['label']['label_3'].get_height() * 0.05)

        text_full_screen = Text(texture=self.reg.textures['ui']['label']['label_3'],
                                text='Полноэкранный режим',
                                x=((self.setting_game.resolution[0] // 2) -
                                   (self.reg.textures['ui']['label']['label_3'].get_width() * 2)),
                                y=(self.setting_game.resolution[1] * 0.145),
                                width=self.reg.textures['ui']['label']['label_3'].get_width(),
                                height=self.reg.textures['ui']['label']['label_3'].get_height(),
                                font=self.reg.fonts['Konstanting'],
                                font_size=round(40 * self.setting_game.size_k[0]),
                                center_text=True,
                                offset_text_x=0,
                                offset_text_y=self.reg.textures['ui']['label']['label_3'].get_height() * 0.05)

        button_full_screen = ValueSwitch(texture=self.reg.textures['ui']['button']['button_3'],
                                         texture_motion=self.reg.textures['ui']['button']['button_3_motion'],
                                         texture_press=self.reg.textures['ui']['button']['button_3_pressed'],
                                         values=['Да', 'Нет'],
                                         select_value='Да' if self.setting_game.full_screen else 'Нет',
                                         x=((self.setting_game.resolution[0] // 2) -
                                            (self.reg.textures['ui']['button']['button_3'].get_width() // 2)),
                                         y=(self.setting_game.resolution[1] * 0.145),
                                         width=self.reg.textures['ui']['button']['button_3'].get_width(),
                                         height=self.reg.textures['ui']['button']['button_3'].get_height(),
                                         font=self.reg.fonts['Konstanting'],
                                         font_size=round(40 * self.setting_game.size_k[0]),
                                         center_text=True,
                                         offset_text_x=0,
                                         offset_text_y=self.reg.textures['ui']['button'][
                                                           'button_3'].get_height() * 0.15,
                                         offset_text_press_x=0,
                                         offset_text_press_y=self.reg.textures['ui']['button'][
                                                                 'button_3'].get_height() * 0.1,
                                         audio_player=self.audio_player)

        text_relation = Text(texture=self.reg.textures['ui']['label']['label_3'],
                             text='Разрешение',
                             x=((self.setting_game.resolution[0] // 2) -
                                (self.reg.textures['ui']['label']['label_3'].get_width() * 2)),
                             y=(self.setting_game.resolution[1] * 0.295),
                             width=self.reg.textures['ui']['label']['label_3'].get_width(),
                             height=self.reg.textures['ui']['label']['label_3'].get_height(),
                             font=self.reg.fonts['Konstanting'],
                             font_size=round(40 * self.setting_game.size_k[0]),
                             center_text=True,
                             offset_text_x=0,
                             offset_text_y=self.reg.textures['ui']['label']['label_3'].get_height() * 0.05)

        button_relations = ValuesSwitch(texture=self.reg.textures['ui']['label']['label_3'],
                                        values=["x".join(map(str, resolution)) for resolution in
                                                pygame.display.list_modes()[::-1]],
                                        select_value='x'.join(map(str, self.setting_game.resolution)),
                                        x=((self.setting_game.resolution[0] // 2) -
                                           (self.reg.textures['ui']['label']['label_3'].get_width() // 2)),
                                        y=(self.setting_game.resolution[1] * 0.295),
                                        width=self.reg.textures['ui']['label']['label_3'].get_width(),
                                        height=self.reg.textures['ui']['label']['label_3'].get_height(),
                                        font=self.reg.fonts['Konstanting'],
                                        font_size=round(40 * self.setting_game.size_k[0]),
                                        center_text=True,
                                        offset_text_x=0,
                                        offset_text_y=self.reg.textures['ui']['label']['label_3'].get_height() * 0.05,
                                        texture_button=self.reg.textures['ui']['button']['button_1'],
                                        texture_button_motion=self.reg.textures['ui']['button']['button_1_motion'],
                                        texture_button_press=self.reg.textures['ui']['button']['button_1_pressed'],
                                        offset_text_press_x=0,
                                        offset_text_press_y=self.reg.textures['ui']['button'][
                                                                'button_3'].get_height() * 0.1,
                                        audio_player=self.audio_player)

        text_volume_sound = Text(texture=self.reg.textures['ui']['label']['label_3'],
                                 text='Звук',
                                 x=((self.setting_game.resolution[0] // 2) -
                                    (self.reg.textures['ui']['label']['label_3'].get_width() * 2)),
                                 y=(self.setting_game.resolution[1] * 0.445),
                                 width=self.reg.textures['ui']['label']['label_3'].get_width(),
                                 height=self.reg.textures['ui']['label']['label_3'].get_height(),
                                 font=self.reg.fonts['Konstanting'],
                                 font_size=round(40 * self.setting_game.size_k[0]),
                                 center_text=True,
                                 offset_text_x=0,
                                 offset_text_y=self.reg.textures['ui']['label']['label_3'].get_height() * 0.05)

        button_volume_sound = ValuesSwitch(texture=self.reg.textures['ui']['label']['label_3'],
                                           values=[d for d in map(str, range(0, 110, 10))],
                                           select_value=str(self.setting_game.volume_sound),
                                           x=((self.setting_game.resolution[0] // 2) -
                                              (self.reg.textures['ui']['label']['label_3'].get_width() // 2)),
                                           y=(self.setting_game.resolution[1] * 0.445),
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

        text_volume_music = Text(texture=self.reg.textures['ui']['label']['label_3'],
                                 text='Громкость',
                                 x=((self.setting_game.resolution[0] // 2) -
                                    (self.reg.textures['ui']['label']['label_3'].get_width() * 2)),
                                 y=(self.setting_game.resolution[1] * 0.595),
                                 width=self.reg.textures['ui']['label']['label_3'].get_width(),
                                 height=self.reg.textures['ui']['label']['label_3'].get_height(),
                                 font=self.reg.fonts['Konstanting'],
                                 font_size=round(40 * self.setting_game.size_k[0]),
                                 center_text=True,
                                 offset_text_x=0,
                                 offset_text_y=self.reg.textures['ui']['label']['label_3'].get_height() * 0.05)

        button_volume_music = ValuesSwitch(texture=self.reg.textures['ui']['label']['label_3'],
                                           values=[d for d in map(str, range(0, 110, 10))],
                                           select_value=str(self.setting_game.volume_music),
                                           x=((self.setting_game.resolution[0] // 2) -
                                              (self.reg.textures['ui']['label']['label_3'].get_width() // 2)),
                                           y=(self.setting_game.resolution[1] * 0.595),
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

        text_fps = Text(texture=self.reg.textures['ui']['label']['label_3'],
                        text='FPS',
                        x=((self.setting_game.resolution[0] // 2) -
                           (self.reg.textures['ui']['label']['label_3'].get_width() * 2)),
                        y=(self.setting_game.resolution[1] * 0.745),
                        width=self.reg.textures['ui']['label']['label_3'].get_width(),
                        height=self.reg.textures['ui']['label']['label_3'].get_height(),
                        font=self.reg.fonts['Konstanting'],
                        font_size=round(40 * self.setting_game.size_k[0]),
                        center_text=True,
                        offset_text_x=0,
                        offset_text_y=self.reg.textures['ui']['label']['label_3'].get_height() * 0.05)

        button_fps = ValuesSwitch(texture=self.reg.textures['ui']['label']['label_3'],
                                  values=['30', '60', '90'],
                                  select_value=str(self.setting_game.fps),
                                  x=((self.setting_game.resolution[0] // 2) -
                                     (self.reg.textures['ui']['label']['label_3'].get_width() // 2)),
                                  y=(self.setting_game.resolution[1] * 0.745),
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

        text_show_fps = Text(texture=self.reg.textures['ui']['label']['label_3'],
                             text='Показывать FPS',
                             x=((self.setting_game.resolution[0] // 2) +
                                (self.reg.textures['ui']['label']['label_3'].get_width())),
                             y=(self.setting_game.resolution[1] * 0.595),
                             width=self.reg.textures['ui']['label']['label_3'].get_width(),
                             height=self.reg.textures['ui']['label']['label_3'].get_height(),
                             font=self.reg.fonts['Konstanting'],
                             font_size=round(40 * self.setting_game.size_k[0]),
                             center_text=True,
                             offset_text_x=0,
                             offset_text_y=self.reg.textures['ui']['label']['label_3'].get_height() * 0.05)

        button_show_fps = ValueSwitch(texture=self.reg.textures['ui']['button']['button_3'],
                                      texture_motion=self.reg.textures['ui']['button']['button_3_motion'],
                                      texture_press=self.reg.textures['ui']['button']['button_3_pressed'],
                                      values=['Да', 'Нет'],
                                      select_value='Да' if self.setting_game.show_fps else 'Нет',
                                      x=((self.setting_game.resolution[0] // 2) +
                                         (self.reg.textures['ui']['label']['label_3'].get_width())),
                                      y=(self.setting_game.resolution[1] * 0.745),
                                      width=self.reg.textures['ui']['button']['button_3'].get_width(),
                                      height=self.reg.textures['ui']['button']['button_3'].get_height(),
                                      font=self.reg.fonts['Konstanting'],
                                      font_size=round(40 * self.setting_game.size_k[0]),
                                      center_text=True,
                                      offset_text_x=0,
                                      offset_text_y=self.reg.textures['ui']['button'][
                                                        'button_3'].get_height() * 0.15,
                                      offset_text_press_x=0,
                                      offset_text_press_y=self.reg.textures['ui']['button'][
                                                              'button_3'].get_height() * 0.1,
                                      audio_player=self.audio_player)

        button_restart = Button(texture=self.reg.textures['ui']['button']['button_3'],
                                texture_motion=self.reg.textures['ui']['button']['button_3_motion'],
                                texture_press=self.reg.textures['ui']['button']['button_3_pressed'],
                                text='Сохранить',
                                x=((self.setting_game.resolution[0] // 2) -
                                   (self.reg.textures['ui']['button']['button_3'].get_width() // 2)),
                                y=(self.setting_game.resolution[1] * 0.895),
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

        button_cancel = Button(texture=self.reg.textures['ui']['button']['button_3'],
                               texture_motion=self.reg.textures['ui']['button']['button_3_motion'],
                               texture_press=self.reg.textures['ui']['button']['button_3_pressed'],
                               text='Отмена',
                               x=((self.setting_game.resolution[0] // 2) +
                                  (self.reg.textures['ui']['label']['label_3'].get_width())),
                               y=(self.setting_game.resolution[1] * 0.895),
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

            text_full_screen.draw(self.screen)
            button_full_screen.update(buttons[0], mouse_pos)
            button_full_screen.draw(self.screen)

            text_relation.draw(self.screen)
            button_relations.update(buttons[0], mouse_pos)
            button_relations.draw(self.screen)

            text_volume_sound.draw(self.screen)
            button_volume_sound.update(buttons[0], mouse_pos)
            button_volume_sound.draw(self.screen)

            text_volume_music.draw(self.screen)
            button_volume_music.update(buttons[0], mouse_pos)
            button_volume_music.draw(self.screen)

            text_fps.draw(self.screen)
            button_fps.update(buttons[0], mouse_pos)
            button_fps.draw(self.screen)

            text_show_fps.draw(self.screen)
            button_show_fps.update(buttons[0], mouse_pos)
            button_show_fps.draw(self.screen)

            button_restart.update(buttons[0], mouse_pos)
            button_restart.draw(self.screen)

            button_cancel.update(buttons[0], mouse_pos)
            button_cancel.draw(self.screen)
            self.screen.blit(cursor_image, mouse_pos)

            if button_restart.is_up:
                data_save = dict()
                if button_full_screen.get_value() == 'Да':
                    data_save['full_screen'] = '1'
                else:
                    data_save['full_screen'] = '0'

                data_save['resolution'] = button_relations.get_value()
                data_save['volume_sound'] = button_volume_sound.get_value()
                data_save['volume_music'] = button_volume_music.get_value()
                data_save['fps'] = button_fps.get_value()
                if button_show_fps.get_value() == 'Да':
                    data_save['show_fps'] = '1'
                else:
                    data_save['show_fps'] = '0'
                self.data_save = data_save

                running = False
                self.next_window = 'restart'

            if button_cancel.is_up:
                running = False
                self.next_window = 'main_menu'

            pygame.display.flip()
            clock.tick(self.setting_game.fps)

        return self.next_window
