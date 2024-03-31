import random

import pygame
from pygame import Rect


# Базовый класс персонажей
class BaseCharacter(pygame.sprite.Sprite):
    # Инициализация параметров
    def __init__(self, setting_game, params, x=0, y=0):
        super().__init__()
        self.setting_game = setting_game
        self.params = {
            'block_name': params['block_name'],
            'cursor_column': params['cursor_column'],
            'cursor_row': params['cursor_row']
        }
        # Параметры принадлежности
        self.name = 'Персонаж'
        if 'name' in params.keys():
            self.name = params['name']

        self.block_name = 'character'
        if 'block_name' in params.keys():
            self.block_name = params['block_name']

        self.type = 'character'
        if 'type' in params.keys():
            self.type = params['type']

        self.group = 0
        if 'group' in params.keys():
            self.group = params['group']

        # Параметры здоровья
        self.health = 100.0
        self.max_health = 100.0
        if 'health' in params.keys():
            self.health = params['health']
            self.max_health = params['health']

        self.speed_regeneration = 0.01
        if 'speed_regeneration' in params.keys():
            self.speed_regeneration = params['speed_regeneration']

        self.is_dead = False

        # Параметры видимости
        self.range_visibility = 0.01
        if 'range_visibility' in params.keys():
            self.range_visibility = params['range_visibility']

        # Параметры передвижения
        self.speed = 5
        if 'speed' in params.keys():
            self.speed = params['speed']

        # Параметры атаки
        self.attack = (1, 2)
        if 'attack' in params.keys():
            self.attack = params['attack']

        self.time_frame_attack = 10 * setting_game.fps_k
        if 'time_attack' in params.keys():
            self.time_frame_attack = params['time_attack']

        self.type_attack = 'melee'
        if 'type_attack' in params.keys():
            self.type_attack = params['type_attack']

        self.is_attack = False

        # Параметры анимации
        self.time_i = 0
        self.time_frame = 10 * setting_game.fps_k

        self.anim = dict()
        if 'anim' in params.keys():
            self.anim = params['anim']

        self.dead_anim = dict()
        if 'dead_anim' in params.keys():
            self.dead_anim = params['dead_anim']

        self.current_frame = 0
        self.directions = ['right', 'left']
        self.direction = random.choice(self.directions)
        self.status = 'idle'

        # Настройки спрайта
        self.image = self.get_texture()
        self.rect = Rect(x, y, self.image.get_width(), self.image.get_height())
        self.x = x
        self.y = y

        self.path_target = None
        self.point_target = None
        self.column_current = 0
        self.row_current = 0

        self.ai_map = None
        self.full_map = None

    # Отрисовка
    def draw(self, screen, camera):
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        self.image = self.get_texture()
        screen.blit(self.image, camera.get_offset(self.rect))

    # Получение текстуры
    def get_texture(self):
        if self.is_dead and self.dead_anim:
            return self.dead_anim[self.current_frame]
        elif self.anim:
            return self.anim[f'{self.status}_{self.direction}'][self.current_frame]['texture']

    # Новое направление персонажа
    def new_direction(self, direction):
        self.direction = direction

    # Новое состояние персонажа
    def new_status(self, status):
        self.status = status
        self.current_frame = 0
        self.time_i = 0

    # Установка маршрута для движения
    def set_move_target(self, path):
        self.path_target = path

    # Установить карту маршрутов
    def set_ai_map(self, ai_map, full_map):
        self.ai_map = ai_map
        self.full_map = full_map

    # Обновление персонажа
    def update(self, cell_size):
        # Смерть персонажа
        if self.health <= 0:
            if self.time_i > 0 and not self.is_dead:
                self.new_status('dead')
                self.is_dead = True
            else:
                self.time_i += 1

                if self.time_i >= self.time_frame:
                    self.current_frame += 1
                    self.time_i = 0

                if self.current_frame > len(self.dead_anim):
                    self.kill()
        else:
            if self.path_target:
                if self.status != 'move':
                    self.new_status('move')
                if self.point_target:
                    if self.point_target[0] * cell_size[1] == self.y and self.point_target[1] * cell_size[0] == self.x:
                        self.point_target = None
                    # Двигаемся вниз
                    elif self.point_target[0] * cell_size[1] > self.y:
                        self.y += self.speed
                        if self.point_target[0] * cell_size[1] < self.y:
                            self.y = self.point_target[0] * cell_size[1]
                    # Двигаемся вверх
                    elif self.point_target[0] * cell_size[1] < self.y:
                        self.y -= self.speed
                        if self.point_target[0] * cell_size[1] > self.y:
                            self.y = self.point_target[0] * cell_size[1]
                    # Двигаемся вправо
                    elif self.point_target[1] * cell_size[0] > self.x:
                        if self.direction != 'right':
                            self.new_direction('right')
                        self.x += self.speed
                        if self.point_target[1] * cell_size[0] < self.x:
                            self.x = self.point_target[1] * cell_size[0]
                    # Двигаемся влево
                    elif self.point_target[1] * cell_size[0] < self.x:
                        if self.direction != 'left':
                            self.new_direction('left')
                        self.x -= self.speed
                        if self.point_target[1] * cell_size[0] > self.x:
                            self.x = self.point_target[1] * cell_size[0]
                else:
                    self.point_target = self.path_target[0]
                    self.path_target = self.path_target[1:]
            else:
                if self.status != 'idle':
                    self.new_status('idle')

            # Регенерация персонажа
            if self.max_health > self.health and self.speed_regeneration:
                self.health += self.speed_regeneration

                if self.health > self.max_health:
                    self.health = self.max_health

            self.time_i += 1

            if self.time_i >= self.time_frame:
                self.current_frame += 1
                self.time_i = 0

            if self.current_frame >= len(self.anim[f'{self.status}_{self.direction}']):
                self.current_frame = 0
