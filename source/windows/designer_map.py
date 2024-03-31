import os
import json
import math
import pygame
from source.ui.grid import Grid
from source.ui.text import Text
from source.ui.button import Button
from source.game_element.camera import Camera
from source.ui.value_switch import ValueSwitch
from source.windows.enter_string import EnterString
from source.windows.select_an_item import SelectAnItem


# Класс окна конструктора карт
class DesignerMap:
    # Инициализация параметров
    def __init__(self, screen, setting_game, audio_player, reg, loading_map=None):
        self.next_window = 'main_window'
        self.screen = screen
        self.setting_game = setting_game
        self.audio_player = audio_player
        self.reg = reg
        self.loading_map = loading_map

    # Окно запуска окна и работы конструктора
    def run_window(self):
        element = None
        color_grid = None
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

        button_show_grid = ValueSwitch(texture=self.reg.textures['ui']['button']['button_3'],
                                       texture_motion=self.reg.textures['ui']['button']['button_3_motion'],
                                       texture_press=self.reg.textures['ui']['button']['button_3_pressed'],
                                       values=['Показывать сетку', 'Не показывать сетку'],
                                       select_value='Показывать сетку',
                                       x=(self.setting_game.resolution[0] - self.reg.textures['ui']['button'][
                                           'button_3'].get_width() * 4),
                                       y=(self.setting_game.resolution[1] - self.reg.textures['ui']['button'][
                                           'button_3'].get_height() * 2),
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

        button_select_color_grid = Button(texture=self.reg.textures['ui']['button']['button_3'],
                                          texture_motion=self.reg.textures['ui']['button']['button_3_motion'],
                                          texture_press=self.reg.textures['ui']['button']['button_3_pressed'],
                                          text='Цвет' if color_grid is None else color_grid['name'],
                                          x=(self.setting_game.resolution[0] - self.reg.textures['ui']['button'][
                                              'button_3'].get_width() * 5),
                                          y=(self.setting_game.resolution[1] - self.reg.textures['ui']['button'][
                                              'button_3'].get_height() * 2),
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

        button_del_map = Button(texture=self.reg.textures['ui']['button']['button_3'],
                                texture_motion=self.reg.textures['ui']['button']['button_3_motion'],
                                texture_press=self.reg.textures['ui']['button']['button_3_pressed'],
                                text='Удалить',
                                x=(self.setting_game.resolution[0] - self.reg.textures['ui']['button'][
                                    'button_3'].get_width() * 5),
                                y=(self.setting_game.resolution[1] - self.reg.textures['ui']['button'][
                                    'button_3'].get_height()),
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

        button_select_element = Button(texture=self.reg.textures['ui']['button']['button_3'],
                                       texture_motion=self.reg.textures['ui']['button']['button_3_motion'],
                                       texture_press=self.reg.textures['ui']['button']['button_3_pressed'],
                                       text='Элемент' if element is None else element['name'],
                                       x=(self.setting_game.resolution[0] - self.reg.textures['ui']['button'][
                                           'button_3'].get_width() * 4),
                                       y=(self.setting_game.resolution[1] - self.reg.textures['ui']['button'][
                                           'button_3'].get_height()),
                                       width=self.reg.textures['ui']['button']['button_3'].get_width(),
                                       height=self.reg.textures['ui']['button']['button_3'].get_height(),
                                       font=self.reg.fonts['Konstanting'],
                                       font_size=round(40 * self.setting_game.size_k[0]),
                                       center_text=True,
                                       offset_text_x=0,
                                       offset_text_y=self.reg.textures['ui']['button']['button_3'].get_height() * 0.15,
                                       offset_text_press_x=0,
                                       offset_text_press_y=self.reg.textures['ui']['button'][
                                                               'button_3'].get_height() * 0.1,
                                       audio_player=self.audio_player)

        button_add_column = Button(texture=self.reg.textures['ui']['button']['button_3'],
                                   texture_motion=self.reg.textures['ui']['button']['button_3_motion'],
                                   texture_press=self.reg.textures['ui']['button']['button_3_pressed'],
                                   text='Добавить колонку',
                                   x=(self.setting_game.resolution[0] - self.reg.textures['ui']['button'][
                                       'button_3'].get_width() * 2),
                                   y=(self.setting_game.resolution[1] - self.reg.textures['ui']['button'][
                                       'button_3'].get_height() * 2),
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

        button_del_column = Button(texture=self.reg.textures['ui']['button']['button_3'],
                                   texture_motion=self.reg.textures['ui']['button']['button_3_motion'],
                                   texture_press=self.reg.textures['ui']['button']['button_3_pressed'],
                                   text='Удалить колонку',
                                   x=(self.setting_game.resolution[0] - self.reg.textures['ui']['button'][
                                       'button_3'].get_width() * 2),
                                   y=(self.setting_game.resolution[1] - self.reg.textures['ui']['button'][
                                       'button_3'].get_height()),
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

        button_add_row = Button(texture=self.reg.textures['ui']['button']['button_3'],
                                texture_motion=self.reg.textures['ui']['button']['button_3_motion'],
                                texture_press=self.reg.textures['ui']['button']['button_3_pressed'],
                                text='Добавить строку',
                                x=(self.setting_game.resolution[0] - self.reg.textures['ui']['button'][
                                    'button_3'].get_width() * 3),
                                y=(self.setting_game.resolution[1] - self.reg.textures['ui']['button'][
                                    'button_3'].get_height() * 2),
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

        button_del_row = Button(texture=self.reg.textures['ui']['button']['button_3'],
                                texture_motion=self.reg.textures['ui']['button']['button_3_motion'],
                                texture_press=self.reg.textures['ui']['button']['button_3_pressed'],
                                text='Удалить строку',
                                x=(self.setting_game.resolution[0] - self.reg.textures['ui']['button'][
                                    'button_3'].get_width() * 3),
                                y=(self.setting_game.resolution[1] - self.reg.textures['ui']['button'][
                                    'button_3'].get_height()),
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

        button_save = Button(texture=self.reg.textures['ui']['button']['button_3'],
                             texture_motion=self.reg.textures['ui']['button']['button_3_motion'],
                             texture_press=self.reg.textures['ui']['button']['button_3_pressed'],
                             text='Сохранить',
                             x=(self.setting_game.resolution[0] - self.reg.textures['ui']['button'][
                                 'button_3'].get_width()),
                             y=(self.setting_game.resolution[1] - self.reg.textures['ui']['button'][
                                 'button_3'].get_height() * 2),
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
                             x=(self.setting_game.resolution[0] - self.reg.textures['ui']['button'][
                                 'button_3'].get_width()),
                             y=(self.setting_game.resolution[1] - self.reg.textures['ui']['button'][
                                 'button_3'].get_height()),
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

        grid = Grid(rows=math.ceil(self.setting_game.resolution[1] / self.setting_game.size_block[1]),
                    columns=math.ceil(self.setting_game.resolution[0] / self.setting_game.size_block[0]),
                    cell_size=self.setting_game.size_block,
                    cursor_block=self.reg.textures['ui']['cursor']['cursor_block'],
                    reg=self.reg,
                    setting_game=self.setting_game)

        if self.loading_map:
            grid.load_map(self.loading_map)

        camera = Camera(min_x=0,
                        min_y=0,
                        max_x=grid.columns * self.setting_game.size_block[0],
                        max_y=(grid.rows + 4) * self.setting_game.size_block[1],
                        setting_game=self.setting_game)

        select_an_item_elements = None
        while running:
            self.screen.fill((0, 0, 0))
            if self.setting_game.show_fps:
                fps_text.set_text(str(int(clock.get_fps())))

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

                    if event.key == pygame.K_g:
                        button_show_grid.value_text.call = True

                    if event.key == pygame.K_h:
                        button_select_color_grid.call = True

            # Дизайнер ------- #
            # Смещение
            camera.update(mouse_pos)
            grid.draw_grid(self.screen, camera, mouse_pos)

            if not any((button_show_grid.is_motion, button_del_map.is_motion,
                        button_select_element.is_motion, button_select_color_grid.is_motion,
                        button_save.is_motion, button_back.is_motion,
                        button_add_row.is_motion, button_del_row.is_motion,
                        button_del_column.is_motion, button_add_column.is_motion)):
                if buttons[0] and grid.cursor_on_grid:
                    if element is not None:
                        grid.add_block(element)
                if buttons[2] and grid.cursor_on_grid:
                    grid.delete_block()
            # Дизайнер ------- #

            if self.setting_game.show_fps:
                fps_text.draw(self.screen)

            button_show_grid.update(buttons[0], mouse_pos)
            button_show_grid.draw(self.screen)

            button_select_color_grid.update(buttons[0], mouse_pos)
            button_select_color_grid.draw(self.screen)

            button_select_element.update(buttons[0], mouse_pos)
            button_select_element.draw(self.screen)

            button_add_column.update(buttons[0], mouse_pos)
            button_add_column.draw(self.screen)

            button_del_column.update(buttons[0], mouse_pos)
            button_del_column.draw(self.screen)

            button_add_row.update(buttons[0], mouse_pos)
            button_add_row.draw(self.screen)

            button_del_row.update(buttons[0], mouse_pos)
            button_del_row.draw(self.screen)

            if self.loading_map:
                button_del_map.update(buttons[0], mouse_pos)
                button_del_map.draw(self.screen)

            button_save.update(buttons[0], mouse_pos)
            button_save.draw(self.screen)

            button_back.update(buttons[0], mouse_pos)
            button_back.draw(self.screen)

            self.screen.blit(cursor_image, mouse_pos)

            if button_show_grid.get_value() == 'Показывать сетку':
                grid.show_grid = True
            elif button_show_grid.get_value() == 'Не показывать сетку':
                grid.show_grid = False

            if button_select_color_grid.is_up or button_select_color_grid.call:
                button_select_color_grid.call = False
                select_an_item = SelectAnItem(self.reg.colors, self.reg, self.setting_game, self.audio_player, 'Цвет')
                value = select_an_item.draw(self.screen)
                if value == 'EXIT_GAME':
                    running = False
                    self.next_window = 'exit'
                if value is None:
                    button_select_color_grid.set_text('Цвет')
                    grid.color_grid = 'white'
                elif 'name' in value:
                    button_select_color_grid.set_text(value['name'])
                    grid.color_grid = value['color']

            if button_select_element.is_up:
                elements = {
                    'is_many': True,
                    'block': self.reg.blocks,
                    'coverage': self.reg.coverage,
                    'objects': self.reg.objects,
                    'cultivated': self.reg.cultivated,
                    'characters': self.reg.characters
                }
                if select_an_item_elements and isinstance(select_an_item_elements, int):
                    select_an_item = SelectAnItem(elements, self.reg, self.setting_game, self.audio_player,
                                                  'Элемент', select_an_item_elements)
                else:
                    select_an_item = SelectAnItem(elements, self.reg, self.setting_game, self.audio_player,
                                                  'Элемент')
                value = select_an_item.draw(self.screen)
                if value == 'EXIT_GAME':
                    running = False
                    self.next_window = 'exit'
                else:
                    select_an_item_elements = select_an_item.current_page

                if value is None:
                    button_select_element.set_text('Элемент')
                elif 'name' in value:
                    button_select_element.set_text(value['name'])
                element = value

            if button_add_column.is_up:
                grid.add_column()
                camera.set_max_x(grid.columns * self.setting_game.size_block[0])

            if button_del_column.is_up:
                grid.delete_column()
                camera.set_max_x(grid.columns * self.setting_game.size_block[0])

            if button_add_row.is_up:
                grid.add_row()
                camera.set_max_y((grid.rows + 5) * self.setting_game.size_block[1])

            if button_del_row.is_up:
                grid.delete_row()
                camera.set_max_y((grid.rows + 5) * self.setting_game.size_block[1])

            if button_del_map.is_up and self.loading_map:
                if self.reg.file_exist(f"levels/{self.loading_map}"):
                    os.remove(f"levels/{self.loading_map}")
                running = False
                self.next_window = 'map_new_or_load_menu'

            if button_save.is_up:
                if self.loading_map:
                    value = self.loading_map
                else:
                    value = EnterString(value='Уровень',
                                        resolution=self.setting_game.resolution,
                                        font=self.reg.fonts['Konstanting'],
                                        size_k=self.setting_game.size_k).draw(self.screen)
                if value == 'EXIT_GAME':
                    running = False
                    self.next_window = 'exit'
                elif value is not None:
                    json_data = {
                        'name': value,
                        'columns': grid.columns,
                        'rows': grid.rows,
                        'grid': [],
                        'goblins': [],
                        'sheep': [],
                        'humans': [],
                    }
                    value = value.replace('.json', '')
                    with open(f"levels/{value}.json", mode='w', encoding='utf-8') as f:
                        for i in grid.goblins:
                            json_data['goblins'].append({'params': i.params})
                        for i in grid.people:
                            json_data['humans'].append({'params': i.params})
                        for i in grid.sheep:
                            json_data['sheep'].append({'params': i.params})
                        for row in grid.grid:
                            row_grid = []
                            for col in row:
                                col_dict = dict()
                                if 'block' in col:
                                    col_dict['block'] = {
                                        'block_name': col['block'].block_name
                                    }
                                if 'coverage' in col:
                                    col_dict['coverage'] = {
                                        'block_name': col['coverage'].block_name
                                    }

                                if 'object' in col:
                                    col_dict['object'] = {
                                        'block_name': col['object'].block_name
                                    }

                                if 'cultivated' in col:
                                    col_dict['cultivated'] = {
                                        'block_name': col['cultivated'].block_name
                                    }
                                row_grid.append(col_dict)
                            json_data['grid'].append(row_grid)
                        json.dump(json_data, f)
                    self.loading_map = f'{value}.json'
                else:
                    pass

            if button_back.is_up:
                running = False
                self.next_window = 'map_new_or_load_menu'

            pygame.display.flip()
            clock.tick(self.setting_game.fps)

        return self.next_window
