import os
import json
import pygame
from source.ui.text import Text
from source.ui.button import Button


# Класс окна статистики
class StatisticsMenu:
    # Инициализация параметров
    def __init__(self, screen, setting_game, audio_player, reg):
        self.next_window = 'main_window'
        self.screen = screen
        self.setting_game = setting_game
        self.audio_player = audio_player
        self.reg = reg

        self.data_save = {}
        if self.reg.file_exist('statistics.json'):
            with open('statistics.json') as f:
                data = json.load(f)
                self.data_save = data

            os.remove('statistics.json')

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

        time = ''
        # Секунды
        time += str(self.data_save['time'] % 60)
        if len(time) == 1:
            time = '0' + time
        self.data_save['time'] //= 60

        # Минуты
        if len(str(self.data_save['time'] % 60)) == 1:
            time = '0' + str(self.data_save['time'] % 60) + ':' + time
        else:
            time = str(self.data_save['time'] % 60) + ':' + time
        self.data_save['time'] //= 60

        # Часы
        if len(str(self.data_save['time'] % 24)) == 1:
            time = '0' + str(self.data_save['time'] % 24) + ':' + time
        else:
            time = str(self.data_save['time'] % 24) + ':' + time
        self.data_save['time'] //= 24

        # Дни
        time = str(self.data_save['time']) + ':' + time

        text_time = Text(texture=self.reg.textures['ui']['label']['label_3'],
                         text=time,
                         x=((self.setting_game.resolution[0] // 2) -
                            (self.reg.textures['ui']['label']['label_3'].get_width() * 1.5)),
                         y=(self.setting_game.resolution[1] * 0.01),
                         width=self.reg.textures['ui']['label']['label_3'].get_width(),
                         height=self.reg.textures['ui']['label']['label_3'].get_height(),
                         font=self.reg.fonts['Konstanting'],
                         font_size=round(40 * self.setting_game.size_k[0]),
                         center_text=True,
                         offset_text_x=0,
                         offset_text_y=self.reg.textures['ui']['label']['label_3'].get_height() * 0.05)

        title = Text(texture=self.reg.textures['ui']['label']['label_3'],
                     text='Итоговое окно',
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

        text_name_map = Text(texture=self.reg.textures['ui']['label']['label_3'],
                             text=self.data_save['map'],
                             x=((self.setting_game.resolution[0] // 2) +
                                (self.reg.textures['ui']['label']['label_3'].get_width() // 2)),
                             y=(self.setting_game.resolution[1] * 0.01),
                             width=self.reg.textures['ui']['label']['label_3'].get_width(),
                             height=self.reg.textures['ui']['label']['label_3'].get_height(),
                             font=self.reg.fonts['Konstanting'],
                             font_size=round(40 * self.setting_game.size_k[0]),
                             center_text=True,
                             offset_text_x=0,
                             offset_text_y=self.reg.textures['ui']['label']['label_3'].get_height() * 0.05)

        text_kill_enemy_des = Text(texture=self.reg.textures['ui']['label']['label_3'],
                                   text='Побеждено врагов:',
                                   x=((self.setting_game.resolution[0] // 2) -
                                      (self.reg.textures['ui']['label']['label_3'].get_width() * 1.5)),
                                   y=(self.setting_game.resolution[1] * 0.15),
                                   width=self.reg.textures['ui']['label']['label_3'].get_width(),
                                   height=self.reg.textures['ui']['label']['label_3'].get_height(),
                                   font=self.reg.fonts['Konstanting'],
                                   font_size=round(40 * self.setting_game.size_k[0]),
                                   center_text=True,
                                   offset_text_x=0,
                                   offset_text_y=self.reg.textures['ui']['label']['label_3'].get_height() * 0.05)

        text_kill_enemy = Text(texture=self.reg.textures['ui']['label']['label_3'],
                               text=str(self.data_save['kill_enemy']),
                               x=((self.setting_game.resolution[0] // 2) -
                                  (self.reg.textures['ui']['label']['label_3'].get_width() // 2)),
                               y=(self.setting_game.resolution[1] * 0.15),
                               width=self.reg.textures['ui']['label']['label_3'].get_width(),
                               height=self.reg.textures['ui']['label']['label_3'].get_height(),
                               font=self.reg.fonts['Konstanting'],
                               font_size=round(40 * self.setting_game.size_k[0]),
                               center_text=True,
                               offset_text_x=0,
                               offset_text_y=self.reg.textures['ui']['label']['label_3'].get_height() * 0.05)

        text_kill_units_died_des = Text(texture=self.reg.textures['ui']['label']['label_3'],
                                        text='Потеряно юнитов:',
                                        x=((self.setting_game.resolution[0] // 2) -
                                           (self.reg.textures['ui']['label']['label_3'].get_width() * 1.5)),
                                        y=(self.setting_game.resolution[1] * 0.30),
                                        width=self.reg.textures['ui']['label']['label_3'].get_width(),
                                        height=self.reg.textures['ui']['label']['label_3'].get_height(),
                                        font=self.reg.fonts['Konstanting'],
                                        font_size=round(40 * self.setting_game.size_k[0]),
                                        center_text=True,
                                        offset_text_x=0,
                                        offset_text_y=self.reg.textures['ui']['label']['label_3'].get_height() * 0.05)

        text_kill_units_died = Text(texture=self.reg.textures['ui']['label']['label_3'],
                                    text=str(self.data_save['kill_units_died']),
                                    x=((self.setting_game.resolution[0] // 2) -
                                       (self.reg.textures['ui']['label']['label_3'].get_width() // 2)),
                                    y=(self.setting_game.resolution[1] * 0.30),
                                    width=self.reg.textures['ui']['label']['label_3'].get_width(),
                                    height=self.reg.textures['ui']['label']['label_3'].get_height(),
                                    font=self.reg.fonts['Konstanting'],
                                    font_size=round(40 * self.setting_game.size_k[0]),
                                    center_text=True,
                                    offset_text_x=0,
                                    offset_text_y=self.reg.textures['ui']['label']['label_3'].get_height() * 0.05)

        text_gold_des = Text(texture=self.reg.textures['ui']['label']['label_3'],
                             text='Осталось золота:',
                             x=((self.setting_game.resolution[0] // 2) -
                                (self.reg.textures['ui']['label']['label_3'].get_width() * 1.5)),
                             y=(self.setting_game.resolution[1] * 0.45),
                             width=self.reg.textures['ui']['label']['label_3'].get_width(),
                             height=self.reg.textures['ui']['label']['label_3'].get_height(),
                             font=self.reg.fonts['Konstanting'],
                             font_size=round(40 * self.setting_game.size_k[0]),
                             center_text=True,
                             offset_text_x=0,
                             offset_text_y=self.reg.textures['ui']['label']['label_3'].get_height() * 0.05)

        text_gold = Text(texture=self.reg.textures['ui']['label']['label_3'],
                         text=str(self.data_save['gold']),
                         x=((self.setting_game.resolution[0] // 2) -
                            (self.reg.textures['ui']['label']['label_3'].get_width() // 2)),
                         y=(self.setting_game.resolution[1] * 0.45),
                         width=self.reg.textures['ui']['label']['label_3'].get_width(),
                         height=self.reg.textures['ui']['label']['label_3'].get_height(),
                         font=self.reg.fonts['Konstanting'],
                         font_size=round(40 * self.setting_game.size_k[0]),
                         center_text=True,
                         offset_text_x=0,
                         offset_text_y=self.reg.textures['ui']['label']['label_3'].get_height() * 0.05)

        text_food_des = Text(texture=self.reg.textures['ui']['label']['label_3'],
                             text='Осталось еды:',
                             x=((self.setting_game.resolution[0] // 2) -
                                (self.reg.textures['ui']['label']['label_3'].get_width() * 1.5)),
                             y=(self.setting_game.resolution[1] * 0.60),
                             width=self.reg.textures['ui']['label']['label_3'].get_width(),
                             height=self.reg.textures['ui']['label']['label_3'].get_height(),
                             font=self.reg.fonts['Konstanting'],
                             font_size=round(40 * self.setting_game.size_k[0]),
                             center_text=True,
                             offset_text_x=0,
                             offset_text_y=self.reg.textures['ui']['label']['label_3'].get_height() * 0.05)

        text_food = Text(texture=self.reg.textures['ui']['label']['label_3'],
                         text=str(self.data_save['food']),
                         x=((self.setting_game.resolution[0] // 2) -
                            (self.reg.textures['ui']['label']['label_3'].get_width() // 2)),
                         y=(self.setting_game.resolution[1] * 0.60),
                         width=self.reg.textures['ui']['label']['label_3'].get_width(),
                         height=self.reg.textures['ui']['label']['label_3'].get_height(),
                         font=self.reg.fonts['Konstanting'],
                         font_size=round(40 * self.setting_game.size_k[0]),
                         center_text=True,
                         offset_text_x=0,
                         offset_text_y=self.reg.textures['ui']['label']['label_3'].get_height() * 0.05)

        text_wood_des = Text(texture=self.reg.textures['ui']['label']['label_3'],
                             text='Осталось дерева:',
                             x=((self.setting_game.resolution[0] // 2) -
                                (self.reg.textures['ui']['label']['label_3'].get_width() * 1.5)),
                             y=(self.setting_game.resolution[1] * 0.75),
                             width=self.reg.textures['ui']['label']['label_3'].get_width(),
                             height=self.reg.textures['ui']['label']['label_3'].get_height(),
                             font=self.reg.fonts['Konstanting'],
                             font_size=round(40 * self.setting_game.size_k[0]),
                             center_text=True,
                             offset_text_x=0,
                             offset_text_y=self.reg.textures['ui']['label']['label_3'].get_height() * 0.05)

        text_wood = Text(texture=self.reg.textures['ui']['label']['label_3'],
                         text=str(self.data_save['wood']),
                         x=((self.setting_game.resolution[0] // 2) -
                            (self.reg.textures['ui']['label']['label_3'].get_width() // 2)),
                         y=(self.setting_game.resolution[1] * 0.75),
                         width=self.reg.textures['ui']['label']['label_3'].get_width(),
                         height=self.reg.textures['ui']['label']['label_3'].get_height(),
                         font=self.reg.fonts['Konstanting'],
                         font_size=round(40 * self.setting_game.size_k[0]),
                         center_text=True,
                         offset_text_x=0,
                         offset_text_y=self.reg.textures['ui']['label']['label_3'].get_height() * 0.05)

        button_back = Button(texture=self.reg.textures['ui']['button']['button_3'],
                             texture_motion=self.reg.textures['ui']['button']['button_3_motion'],
                             texture_press=self.reg.textures['ui']['button']['button_3_pressed'],
                             text='Выход в меню',
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

            text_time.draw(self.screen)
            title.draw(self.screen)
            text_name_map.draw(self.screen)
            text_kill_enemy_des.draw(self.screen)
            text_kill_enemy.draw(self.screen)
            text_kill_units_died_des.draw(self.screen)
            text_kill_units_died.draw(self.screen)
            text_gold_des.draw(self.screen)
            text_gold.draw(self.screen)
            text_food_des.draw(self.screen)
            text_food.draw(self.screen)
            text_wood_des.draw(self.screen)
            text_wood.draw(self.screen)

            button_back.update(buttons[0], mouse_pos)
            button_back.draw(self.screen)

            self.screen.blit(cursor_image, mouse_pos)

            if button_back.is_up:
                running = False
                self.next_window = 'main_menu'

            pygame.display.flip()
            clock.tick(self.setting_game.fps)

        return self.next_window
