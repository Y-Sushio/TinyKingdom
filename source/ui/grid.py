import json
import pygame
from source.game_element.blocks.block import Block
from source.game_element.blocks.cultivated import Cultivated
from source.game_element.characters.bot_passive import BotPassive


# Класс игровой сетки
class Grid:
    # Инициализация параметров
    def __init__(self, rows, columns, cell_size, cursor_block, reg, setting_game):
        self.cursor_row = None
        self.color_grid = (255, 255, 255)
        self.cursor_column = None
        self.cursor_on_grid = False
        self.rows = rows
        self.columns = columns
        self.cell_size = cell_size
        self.grid = [[dict() for _ in range(columns)] for _ in range(rows)]
        self.window_size = (self.columns * self.cell_size, self.rows * self.cell_size)
        self.cursor_block = cursor_block
        self.show_grid = True
        self.reg = reg
        self.setting_game = setting_game
        self.goblins = pygame.sprite.Group()
        self.people = pygame.sprite.Group()
        self.sheep = pygame.sprite.Group()

    # Добавление колонки в конец сетки
    def add_column(self):
        if self.grid:
            for row in range(len(self.grid)):
                self.grid[row].append(dict())
            self.columns += 1

    # Удаление последней колонки из сетки
    def delete_column(self):
        if self.grid:
            for row in range(len(self.grid)):
                self.grid[row].pop()
            self.columns -= 1

    # Добавление строки в конец сетки
    def add_row(self):
        self.grid.append([dict() for _ in range(self.columns)])
        self.rows += 1

    # Удаление последней строки из сетки
    def delete_row(self):
        if self.grid:
            self.grid.pop()
            self.rows -= 1

    # Добавление блока/объекта на сетку
    def add_block(self, block):
        if block['type'] == 'character':
            block['cursor_column'] = self.cursor_column
            block['cursor_row'] = self.cursor_row
            if block['block_name'] == 'sheep':
                check = True
                for i in self.sheep:
                    if (i.x == self.cursor_column * self.cell_size[0]
                            and i.y == self.cursor_row * self.cell_size[1]):
                        check = False

                if check:
                    character = BotPassive(setting_game=self.setting_game,
                                           params=block,
                                           x=self.cursor_column * self.cell_size[0],
                                           y=self.cursor_row * self.cell_size[1])
                    self.sheep.add(character)

            if block['block_name'] in ['archer', 'warrior', 'peasant']:
                check = True
                for i in self.people:
                    if (i.x == self.cursor_column * self.cell_size[0]
                            and i.y == self.cursor_row * self.cell_size[1]):
                        check = False

                if check:
                    character = BotPassive(setting_game=self.setting_game,
                                           params=block,
                                           x=self.cursor_column * self.cell_size[0],
                                           y=self.cursor_row * self.cell_size[1])
                    self.people.add(character)

            if block['block_name'] == 'goblin':
                check = True
                for i in self.goblins:
                    if (i.x == self.cursor_column * self.cell_size[0]
                            and i.y == self.cursor_row * self.cell_size[1]):
                        check = False

                if check:
                    character = BotPassive(setting_game=self.setting_game,
                                           params=block,
                                           x=self.cursor_column * self.cell_size[0],
                                           y=self.cursor_row * self.cell_size[1])
                    self.goblins.add(character)

        if block['type'] == 'block':
            self.grid[self.cursor_row][self.cursor_column]['block'] = Block(x=self.cursor_column * self.cell_size[0],
                                                                            y=self.cursor_row * self.cell_size[1],
                                                                            block_name=block['block_name'],
                                                                            is_solid=block['is_solid'],
                                                                            texture=block['texture'])

        if block['type'] == 'coverage':
            self.grid[self.cursor_row][self.cursor_column]['coverage'] = Block(x=self.cursor_column * self.cell_size[0],
                                                                               y=self.cursor_row * self.cell_size[1],
                                                                               block_name=block['block_name'],
                                                                               is_solid=block['is_solid'],
                                                                               texture=block['texture'])

        if block['type'] == 'object':
            self.grid[self.cursor_row][self.cursor_column]['object'] = Block(x=self.cursor_column * self.cell_size[0],
                                                                             y=self.cursor_row * self.cell_size[1],
                                                                             block_name=block['block_name'],
                                                                             texture=block['texture'])

        if block['type'] == 'cultivated':
            self.grid[self.cursor_row][self.cursor_column]['cultivated'] = Cultivated(
                x=self.cursor_column * self.cell_size[0],
                y=self.cursor_row * self.cell_size[1],
                block_name=block['block_name'],
                texture_start=block['texture_start'],
                texture_end=block['texture_end'],
                rate_growth=block['rate_growth'],
                food=block['food']
            )

    # Очистка выбранной клетки сетки
    def delete_block(self):
        if self.cursor_row >= 0 and self.cursor_column >= 0:
            if 0 <= self.cursor_row <= len(self.grid):
                if 0 <= self.cursor_column <= len(self.grid[self.cursor_row]):
                    self.grid[self.cursor_row][self.cursor_column] = dict()

                    for i in self.sheep:
                        if (i.x == self.cursor_column * self.cell_size[0]
                                and i.y == self.cursor_row * self.cell_size[1]):
                            i.kill()

                    for i in self.people:
                        if (i.x == self.cursor_column * self.cell_size[0]
                                and i.y == self.cursor_row * self.cell_size[1]):
                            i.kill()

                    for i in self.goblins:
                        if (i.x == self.cursor_column * self.cell_size[0]
                                and i.y == self.cursor_row * self.cell_size[1]):
                            i.kill()

    # Установки карты маршрутов всем персонажам
    def set_ai_map(self, ai_map, full_map):
        for character in self.people:
            character.set_ai_map(ai_map, full_map)

        for character in self.goblins:
            character.set_ai_map(ai_map, full_map)

        for character in self.sheep:
            character.set_ai_map(ai_map, full_map)

    # Отрисовка сетки
    def draw_grid(self, screen, camera, cursor_pos):
        self.cursor_column = (cursor_pos[0] + camera.pos_camera_x) // self.cell_size[0]
        self.cursor_row = (cursor_pos[1] + camera.pos_camera_y) // self.cell_size[1]
        self.cursor_on_grid = False
        for row in range(self.rows):
            for col in range(self.columns):
                rect = pygame.Rect(col * self.cell_size[0], row * self.cell_size[1],
                                   self.cell_size[0], self.cell_size[1])

                if 'block' in self.grid[row][col]:
                    screen.blit(self.grid[row][col]['block'].image, camera.get_offset(rect))

                if 'coverage' in self.grid[row][col]:
                    screen.blit(self.grid[row][col]['coverage'].image, camera.get_offset(rect))

                if 'object' in self.grid[row][col] and 'cultivated' not in self.grid[row][col]:
                    screen.blit(self.grid[row][col]['object'].image, camera.get_offset(rect))

                if 'cultivated' in self.grid[row][col]:
                    screen.blit(self.grid[row][col]['cultivated'].image, camera.get_offset(rect))

                if self.cursor_row == row and self.cursor_column == col:
                    screen.blit(self.cursor_block, camera.get_offset(rect))
                    self.cursor_on_grid = True

                if self.show_grid:
                    pygame.draw.rect(screen, pygame.Color(self.color_grid), camera.get_offset(rect), 1)

        for character in self.people:
            character.column_current = character.x // self.cell_size[0]
            character.row_current = character.y // self.cell_size[1]
            character.ai_controller()
            character.update(self.cell_size)
            character.draw(screen, camera)

        for character in self.goblins:
            character.column_current = character.x // self.cell_size[0]
            character.row_current = character.y // self.cell_size[1]
            character.ai_controller()
            character.update(self.cell_size)
            character.draw(screen, camera)

        for character in self.sheep:
            character.column_current = character.x // self.cell_size[0]
            character.row_current = character.y // self.cell_size[1]
            character.ai_controller()
            character.update(self.cell_size)
            character.draw(screen, camera)

    # Загрузка сетки из файла
    def load_map(self, path_map):
        path_map = f'levels/{path_map}'
        if self.reg.file_exist(path_map):
            data = None
            with open(path_map) as jf:
                data = json.load(jf)
            if data:
                self.columns = data['columns']
                self.rows = data['rows']
                self.grid = [[dict() for _ in range(data['columns'])] for _ in range(data['rows'])]
                for i in range(self.rows):
                    self.cursor_row = i
                    for j in range(self.columns):
                        self.cursor_column = j
                        if 'block' in data['grid'][i][j].keys():
                            self.add_block(self.reg.blocks[data['grid'][i][j]['block']['block_name']])
                        if 'coverage' in data['grid'][i][j].keys():
                            self.add_block(self.reg.coverage[data['grid'][i][j]['coverage']['block_name']])
                        if 'object' in data['grid'][i][j].keys():
                            self.add_block(self.reg.objects[data['grid'][i][j]['object']['block_name']])

                if 'sheep' in data:
                    for i in data['sheep']:
                        self.cursor_column = i['params']['cursor_column']
                        self.cursor_row = i['params']['cursor_row']
                        self.add_block(self.reg.characters[i['params']['block_name']])

                if 'humans' in data:
                    for i in data['humans']:
                        self.cursor_column = i['params']['cursor_column']
                        self.cursor_row = i['params']['cursor_row']
                        self.add_block(self.reg.characters[i['params']['block_name']])

                if 'goblins' in data:
                    for i in data['goblins']:
                        self.cursor_column = i['params']['cursor_column']
                        self.cursor_row = i['params']['cursor_row']
                        self.add_block(self.reg.characters[i['params']['block_name']])
