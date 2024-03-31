import json
import math
import pygame

from source.game_element.map_ai import get_ai_map
from source.ui.grid import Grid
from source.ui.text import Text
from source.game_element.camera import Camera
from source.windows.select_an_item import SelectAnItem


# Класс игрового процесса
class Game:
    # Инициализация параметров
    def __init__(self, screen, setting_game, audio_player, reg, loading_map):
        self.next_window = 'statistics_menu'
        self.screen = screen
        self.setting_game = setting_game
        self.audio_player = audio_player
        self.reg = reg
        self.loading_map = loading_map
        self.ai_map = None
        self.data_save = {
            'map': self.loading_map.replace('.json', ''),
            'kill_enemy': 0,
            'kill_units_died': 0,
            'gold': 0,
            'food': 0,
            'wood': 0,
            'time': 0
        }

    # Запуск окна игры
    def run_window(self):
        clock = pygame.time.Clock()
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

        grid = Grid(rows=math.ceil(self.setting_game.resolution[1] / self.setting_game.size_block[1]),
                    columns=math.ceil(self.setting_game.resolution[0] / self.setting_game.size_block[0]),
                    cell_size=self.setting_game.size_block,
                    cursor_block=self.reg.textures['ui']['cursor']['cursor_block'],
                    reg=self.reg,
                    setting_game=self.setting_game)
        grid.show_grid = False

        if self.loading_map:
            grid.load_map(self.loading_map)
        else:
            print('Новая карта')

        self.ai_map = get_ai_map(grid)
        grid.set_ai_map(self.ai_map, grid.grid)

        camera = Camera(min_x=0,
                        min_y=0,
                        max_x=grid.columns * self.setting_game.size_block[0],
                        max_y=(grid.rows + 4) * self.setting_game.size_block[1],
                        setting_game=self.setting_game)

        running = True
        cursor_image = self.reg.textures['ui']['cursor']['cursor']
        time_i = 0
        max_time_i = self.setting_game.fps * 10000
        while running:
            time_i += 1
            if time_i % self.setting_game.fps == 0:
                self.data_save['time'] += 1
                if time_i >= max_time_i:
                    time_i = 1

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
                        self.next_window = 'statistics_menu'

                    if event.key == pygame.K_g:
                        if grid.show_grid:
                            grid.show_grid = False
                        else:
                            grid.show_grid = True

                    if event.key == pygame.K_h:
                        select_an_item = SelectAnItem(self.reg.colors, self.reg, self.setting_game, self.audio_player,
                                                      'Цвет')
                        value = select_an_item.draw(self.screen)
                        if value == 'EXIT_GAME':
                            running = False
                            self.next_window = 'exit'
                        if value is None:
                            grid.color_grid = 'white'
                        elif 'name' in value:
                            grid.color_grid = value['color']

            self.screen.fill((0, 0, 0))

            camera.update(mouse_pos)
            grid.draw_grid(self.screen, camera, mouse_pos)

            if self.setting_game.show_fps:
                fps_text.draw(self.screen)

            self.screen.blit(cursor_image, pygame.mouse.get_pos())
            pygame.display.flip()
            clock.tick(self.setting_game.fps)

        with open('statistics.json', encoding='utf-8', mode='w') as f:
            json.dump(self.data_save, f)
        return self.next_window
