import os
import pygame


# Класс реестра ресурсов
class ResourceRegistry:
    # Инициализация параметров
    def __init__(self, k_size, fps):
        self.textures_path = None
        self.textures = None
        self.audio_music_path = {
            'menu': 'resources/music/menu.mp3',
            'game': 'resources/music/game.mp3'
        }
        self.audio_sounds_path = {
            'button_press': 'resources/sounds/press_button.mp3',
            'button_up': 'resources/sounds/press_button.mp3'
        }
        self.icon = self.load_image_alpha('icon.png')
        self.fonts = {
            'Konstanting': 'resources/fonts/Konstanting.ttf'
        }
        self.k_size = k_size
        self.colors = {
            'white':
                {
                    'name': 'Белый',
                    'color': 'white'
                },
            'red':
                {
                    'name': 'Красный',
                    'color': 'red'
                },
            'blue':
                {
                    'name': 'Синий',
                    'color': 'blue'
                },
            'green':
                {
                    'name': 'Зелёный',
                    'color': 'green'
                },
        }
        self.fps = fps
        self.blocks = dict()
        self.coverage = dict()
        self.objects = dict()
        self.cultivated = dict()
        self.effects = dict()
        self.characters = dict()

    # Проверка существования файла
    def file_exist(self, path):
        if os.path.exists(path):
            return True
        else:
            print(f"Файл '{path}' не найден!")
            return False

    # Загрузка изображения
    def load_image(self, path):
        if self.file_exist(path):
            image = pygame.image.load(path)
            image = image.convert()
            return image
        return None

    # Загрузка прозрачного изображения
    def load_image_alpha(self, path):
        if self.file_exist(path):
            image = pygame.image.load(path)
            image = image.convert_alpha()
            return image
        return None

    # Загрузка реестра, решил в данном этапе не хранить в файле, т.к. нужен тогда отдельный модуль
    def load_registry(self):
        self.textures_path = {
            'characters': {
                'peasant': {
                    'peasant': ('peasant.png', True, (64, 64), {
                        'type': 'several_parts',
                        'crop': (0.25, 0.25, 0.25, 0.25),
                        'column': 6,
                        'row': 6
                    })
                },
                'goblin': {
                    'goblin': ('goblin.png', True, (64, 64), {
                        'type': 'several_parts',
                        'crop': (0.15, 0.25, 0.25, 0.25),
                        'column': 7,
                        'row': 5
                    })
                },
                'archer': {
                    'archer': ('archer.png', True, (64, 64), {
                        'type': 'several_parts',
                        'crop': (0.25, 0.25, 0.25, 0.25),
                        'column': 8,
                        'row': 7
                    })
                },
                'warrior': {
                    'warrior': ('warrior.png', True, (64, 64), {
                        'type': 'several_parts',
                        'crop': (0.25, 0.25, 0.25, 0.25),
                        'column': 6,
                        'row': 8
                    })
                },
                'sheep': {
                    'sheep': ('sheep.png', True, (64, 64), {
                        'type': 'several_parts',
                        'crop': (0.2, 0.2, 0.2, 0.2),
                        'column': 8,
                        'row': 2
                    })
                },
            },
            'effects': {
                'dead': {
                    'dead': ('dead.png', True, (64, 64), {
                        'type': 'several_parts',
                        'column': 7,
                        'row': 2
                    })
                },
                'explosion': {
                    'explosion': ('explosion.png', True, (64, 64), {
                        'type': 'several_parts',
                        'column': 9,
                        'row': 1
                    })
                },
                'fire': {
                    'fire': ('fire.png', True, (64, 64), {
                        'type': 'several_parts',
                        'column': 7,
                        'row': 1
                    })
                },
            },
            'terrain': {
                'water': {
                    'water': ('water.png', False, (64, 64))
                },
                'ground': {
                    'ground': ('ground.png', True, (64, 64), {
                        'type': 'several_parts',
                        'column': 4,
                        'row': 6
                    })
                },
                'ladder': {
                    'ladder_left': ('ladder_left.png', True, (64, 64), {
                        'type': 'several_parts',
                        'column': 1,
                        'row': 4
                    }),
                    'ladder_right': ('ladder_right.png', True, (64, 64), {
                        'type': 'several_parts',
                        'column': 1,
                        'row': 4
                    }),
                    'ladder_up': ('ladder_up.png', True, (64, 64), {
                        'type': 'several_parts',
                        'column': 4,
                        'row': 1
                    }),
                    'ladder_down': ('ladder_down.png', True, (64, 64), {
                        'type': 'several_parts',
                        'column': 4,
                        'row': 1
                    })
                },
                'grass': {
                    'grass': ('grass.png', True, (64, 64), {
                        'type': 'several_parts',
                        'column': 4,
                        'row': 4
                    })
                },
                'sand': {
                    'sand': ('sand.png', True, (64, 64), {
                        'type': 'several_parts',
                        'column': 4,
                        'row': 4
                    })
                },
            },
            'objects': {
                'big_bush': ('big_bush.png', True, (64, 64)),
                'medium_bush': ('medium_bush.png', True, (64, 64)),
                'small_bush': ('small_bush.png', True, (64, 64)),
                'big_mushroom': ('big_mushroom.png', True, (64, 64)),
                'medium_mushroom': ('big_mushroom.png', True, (64, 64)),
                'small_mushroom': ('big_mushroom.png', True, (64, 64)),
                'big_stone': ('big_stone.png', True, (64, 64)),
                'medium_stone': ('medium_stone.png', True, (64, 64)),
                'small_stone': ('small_stone.png', True, (64, 64)),
                'bone': ('bone.png', True, (64, 64)),
                'bone_broken': ('bone_broken.png', True, (64, 64)),
                'left_pointer': ('left_pointer.png', True, (64, 64)),
                'right_pointer': ('right_pointer.png', True, (64, 64)),
                'scarecrow': ('scarecrow.png', True, (64, 64)),
                'totem': ('totem.png', True, (64, 64))
            },
            'cultivated': {
                'greens_end': ('greens_end.png', True, (64, 64)),
                'greens_start': ('greens_start.png', True, (64, 64)),
                'pumpkin_end': ('pumpkin_end.png', True, (64, 64)),
                'pumpkin_start': ('pumpkin_start.png', True, (64, 64))
            },
            'ui': {
                'cursor': {
                    'cursor': ('cursor.png', True, (64, 64)),
                    'cursor_block': ('cursor_block.png', True, (64, 64)),
                },
                'button': {
                    'button_3': ('button_3.png', True, (384, 128)),
                    'button_3_motion': ('button_3_motion.png', True, (384, 128)),
                    'button_3_pressed': ('button_3_pressed.png', True, (384, 128)),
                    'button_1': ('button_3.png', True, (128, 128)),
                    'button_1_motion': ('button_3_motion.png', True, (128, 128)),
                    'button_1_pressed': ('button_3_pressed.png', True, (128, 128))
                },
                'label': {
                    'label_3_simple': ('label_3_simple.png', True, (384, 128)),
                    'label_3': ('label_3.png', True, (384, 128)),
                },
                'background_menu': {
                    '1': ('1.png', False, (1920, 1080)),
                    '2': ('2.png', False, (1920, 1080)),
                    '3': ('3.png', False, (1920, 1080)),
                    '4': ('4.png', False, (1920, 1080)),
                    '5': ('5.png', False, (1920, 1080)),
                    '6': ('6.png', False, (1920, 1080)),
                    '7': ('7.png', False, (1920, 1080)),
                    '8': ('8.png', False, (1920, 1080))
                }
            }
        }
        self.textures = dict()
        self.load_textures(self.textures_path, self.textures, 'resources/textures/')
        self.load_blocks()

    # Загрузка текстур
    def load_textures(self, textures_path, textures, path):
        for key, value in textures_path.items():
            if isinstance(value, dict) and key not in textures:
                textures[key] = dict()

            if isinstance(value, dict) and key in textures:
                self.load_textures(textures_path[key], textures[key], path + f"{key}/")

            if isinstance(value, tuple):
                if len(value) > 3:
                    data_dict = value[3]
                    if data_dict['type'] == 'several_parts':
                        if value[1]:
                            image = self.load_image_alpha(path + value[0])
                        else:
                            image = self.load_image(path + value[0])
                        if not image:
                            continue

                        frames = []
                        rect = pygame.Rect(0, 0, image.get_width() // data_dict['column'],
                                           image.get_height() // data_dict['row'])
                        for i in range(data_dict['row']):
                            for j in range(data_dict['column']):
                                if 'crop' in data_dict.keys():
                                    frame_location = (rect.w * j + round(rect.w * data_dict['crop'][0]),
                                                      rect.h * i + round(rect.h * data_dict['crop'][1]))
                                    frames.append(image.subsurface(pygame.Rect(frame_location,
                                                                               (rect.w - round(
                                                                                   rect.w * data_dict['crop'][2] * 2),
                                                                                rect.h - round(
                                                                                    rect.h * data_dict['crop'][
                                                                                        3] * 2)))))
                                else:
                                    frame_location = (rect.w * j, rect.h * i)
                                    frames.append(image.subsurface(pygame.Rect(frame_location, rect.size)))
                        if frames:
                            for i in range(len(frames)):
                                textures[key + '_' + str(i)] = pygame.transform.scale(frames[i], (
                                    round(value[2][0] * self.k_size[0]),
                                    round(value[2][1] * self.k_size[1])))
                        else:
                            for i in range(len(frames)):
                                textures[key + '_' + str(i)] = frames[i]
                else:
                    if value[1]:
                        image = self.load_image_alpha(path + value[0])
                    else:
                        image = self.load_image(path + value[0])
                    if image:
                        textures[key] = pygame.transform.scale(image, (round(value[2][0] * self.k_size[0]),
                                                                       round(value[2][1] * self.k_size[1])))

    # Загрузка блоков и объектов
    def load_blocks(self):
        self.blocks = dict()
        for key, value in self.textures['terrain'].items():
            if key == 'water':
                self.blocks['water'] = {
                    'name': 'Вода',
                    'type': 'block',
                    'block_name': key,
                    'texture': value['water'],
                    'is_solid': True,
                    'size_block': (value['water'].get_width(),
                                   value['water'].get_height())
                }

            if key == 'ground':
                for key_texture, value_texture in value.items():
                    self.blocks[key_texture] = {
                        'name': f'Земля_{key_texture.replace("ground_", "")}',
                        'type': 'block',
                        'block_name': key_texture,
                        'texture': value_texture,
                        'is_solid': False,
                        'size_block': (value_texture.get_width(),
                                       value_texture.get_height()),
                        'move': 'all'
                    }

            if key == 'ladder':
                for key_texture, value_texture in value.items():

                    if 'ladder_up' in key_texture:
                        self.blocks[key_texture] = {
                            'name': f'Лестница_вверх_{key_texture.replace("ladder_up_", "")}',
                            'type': 'block',
                            'block_name': key_texture,
                            'texture': value_texture,
                            'is_solid': False,
                            'size_block': (value_texture.get_width(),
                                           value_texture.get_height()),
                            'move': 'down_up'
                        }

                    if 'ladder_down' in key_texture:
                        self.blocks[key_texture] = {
                            'name': f'Лестница_вниз_{key_texture.replace("ladder_down_", "")}',
                            'type': 'block',
                            'block_name': key_texture,
                            'texture': value_texture,
                            'is_solid': False,
                            'size_block': (value_texture.get_width(),
                                           value_texture.get_height()),
                            'move': 'down_up'
                        }

                    if 'ladder_left' in key_texture:
                        self.blocks[key_texture] = {
                            'name': f'Лестница_влево_{key_texture.replace("ladder_left_", "")}',
                            'type': 'block',
                            'block_name': key_texture,
                            'texture': value_texture,
                            'is_solid': False,
                            'size_block': (value_texture.get_width(),
                                           value_texture.get_height()),
                            'move': 'left_right'
                        }

                    if 'ladder_right' in key_texture:
                        self.blocks[key_texture] = {
                            'name': f'Лестница_вправо_{key_texture.replace("ladder_right_", "")}',
                            'type': 'block',
                            'block_name': key_texture,
                            'texture': value_texture,
                            'is_solid': False,
                            'size_block': (value_texture.get_width(),
                                           value_texture.get_height()),
                            'move': 'left_right'
                        }

        self.coverage = dict()
        for key, value in self.textures['terrain'].items():
            if key == 'grass':
                for key_texture, value_texture in value.items():
                    self.coverage[key_texture] = {
                        'name': f'Трава_{key_texture.replace("grass_", "")}',
                        'type': 'coverage',
                        'block_name': key_texture,
                        'texture': value_texture,
                        'is_solid': False,
                        'size_block': (value_texture.get_width(),
                                       value_texture.get_height())
                    }

            if key == 'sand':
                for key_texture, value_texture in value.items():
                    self.coverage[key_texture] = {
                        'name': f'Песок_{key_texture.replace("sand_", "")}',
                        'type': 'coverage',
                        'block_name': key_texture,
                        'texture': value_texture,
                        'is_solid': False,
                        'size_block': (value_texture.get_width(),
                                       value_texture.get_height())
                    }

        self.objects = dict()
        for key_texture, value_texture in self.textures['objects'].items():
            if 'big_bush' == key_texture:
                self.objects[key_texture] = {
                    'name': f'Большой куст',
                    'type': 'object',
                    'block_name': key_texture,
                    'texture': value_texture,
                    'size_block': (value_texture.get_width(),
                                   value_texture.get_height())
                }

            if 'medium_bush' == key_texture:
                self.objects[key_texture] = {
                    'name': f'Обычный куст',
                    'type': 'object',
                    'block_name': key_texture,
                    'texture': value_texture,
                    'size_block': (value_texture.get_width(),
                                   value_texture.get_height())
                }

            if 'small_bush' == key_texture:
                self.objects[key_texture] = {
                    'name': f'Меленький куст',
                    'type': 'object',
                    'block_name': key_texture,
                    'texture': value_texture,
                    'size_block': (value_texture.get_width(),
                                   value_texture.get_height())
                }

            if 'big_mushroom' == key_texture:
                self.objects[key_texture] = {
                    'name': f'Большой гриб',
                    'type': 'object',
                    'block_name': key_texture,
                    'texture': value_texture,
                    'size_block': (value_texture.get_width(),
                                   value_texture.get_height())
                }

            if 'medium_mushroom' == key_texture:
                self.objects[key_texture] = {
                    'name': f'Обычный гриб',
                    'type': 'object',
                    'block_name': key_texture,
                    'texture': value_texture,
                    'size_block': (value_texture.get_width(),
                                   value_texture.get_height())
                }

            if 'small_mushroom' == key_texture:
                self.objects[key_texture] = {
                    'name': f'Меленький гриб',
                    'type': 'object',
                    'block_name': key_texture,
                    'texture': value_texture,
                    'size_block': (value_texture.get_width(),
                                   value_texture.get_height())
                }

            if 'big_stone' == key_texture:
                self.objects[key_texture] = {
                    'name': f'Большой камень',
                    'type': 'object',
                    'block_name': key_texture,
                    'texture': value_texture,
                    'size_block': (value_texture.get_width(),
                                   value_texture.get_height())
                }

            if 'medium_stone' == key_texture:
                self.objects[key_texture] = {
                    'name': f'Обычный камень',
                    'type': 'object',
                    'block_name': key_texture,
                    'texture': value_texture,
                    'size_block': (value_texture.get_width(),
                                   value_texture.get_height())
                }

            if 'small_stone' == key_texture:
                self.objects[key_texture] = {
                    'name': f'Меленький камень',
                    'type': 'object',
                    'block_name': key_texture,
                    'texture': value_texture,
                    'size_block': (value_texture.get_width(),
                                   value_texture.get_height())
                }

            if 'bone' == key_texture:
                self.objects[key_texture] = {
                    'name': f'Кость',
                    'type': 'object',
                    'block_name': key_texture,
                    'texture': value_texture,
                    'size_block': (value_texture.get_width(),
                                   value_texture.get_height())
                }

            if 'bone_broken' == key_texture:
                self.objects[key_texture] = {
                    'name': f'Сломанная кость',
                    'type': 'object',
                    'block_name': key_texture,
                    'texture': value_texture,
                    'size_block': (value_texture.get_width(),
                                   value_texture.get_height())
                }

            if 'left_pointer' == key_texture:
                self.objects[key_texture] = {
                    'name': f'Указатель налево',
                    'type': 'object',
                    'block_name': key_texture,
                    'texture': value_texture,
                    'size_block': (value_texture.get_width(),
                                   value_texture.get_height())
                }

            if 'right_pointer' == key_texture:
                self.objects[key_texture] = {
                    'name': f'Указатель налево',
                    'type': 'object',
                    'block_name': key_texture,
                    'texture': value_texture,
                    'size_block': (value_texture.get_width(),
                                   value_texture.get_height())
                }

            if 'scarecrow' == key_texture:
                self.objects[key_texture] = {
                    'name': f'Пугало',
                    'type': 'object',
                    'block_name': key_texture,
                    'texture': value_texture,
                    'size_block': (value_texture.get_width(),
                                   value_texture.get_height())
                }

            if 'totem' == key_texture:
                self.objects[key_texture] = {
                    'name': f'Тотем',
                    'type': 'object',
                    'block_name': key_texture,
                    'texture': value_texture,
                    'size_block': (value_texture.get_width(),
                                   value_texture.get_height())
                }

        self.cultivated = dict()
        self.cultivated['greens'] = {
            'name': 'Зелень',
            'type': 'cultivated',
            'block_name': 'greens',
            'texture_start': self.textures['cultivated']['greens_start'],
            'texture_end': self.textures['cultivated']['greens_end'],
            'rate_growth': self.fps * 60 * 5,
            'size_block': (self.textures['cultivated']['greens_start'].get_width(),
                           self.textures['cultivated']['greens_start'].get_height()),
            'food': 5
        }

        self.cultivated['pumpkin'] = {
            'name': 'Тыква',
            'type': 'cultivated',
            'block_name': 'pumpkin',
            'texture_start': self.textures['cultivated']['pumpkin_start'],
            'texture_end': self.textures['cultivated']['pumpkin_end'],
            'rate_growth': self.fps * 60 * 8,
            'size_block': (self.textures['cultivated']['pumpkin_start'].get_width(),
                           self.textures['cultivated']['pumpkin_start'].get_height()),
            'food': 10
        }

        self.effects = dict()
        for key, value in self.textures['effects'].items():
            if key == 'dead':
                self.effects[key] = []
                for key_texture, value_texture in value.items():
                    self.effects[key].append(value_texture)

            if key == 'explosion':
                for key_texture, value_texture in value.items():
                    self.effects[key_texture] = {
                        'name': f'Взрыв_{key_texture.replace("explosion_", "")}',
                        'type': 'effects',
                        'block_name': key_texture,
                        'texture': value_texture,
                        'is_solid': False,
                        'size_block': (value_texture.get_width(),
                                       value_texture.get_height())
                    }

            if key == 'fire':
                for key_texture, value_texture in value.items():
                    self.effects[key_texture] = {
                        'name': f'Огонь_{key_texture.replace("fire_", "")}',
                        'type': 'effects',
                        'block_name': key_texture,
                        'texture': value_texture,
                        'is_solid': False,
                        'size_block': (value_texture.get_width(),
                                       value_texture.get_height())
                    }

        self.characters = dict()
        for key, value in self.textures['characters'].items():
            if key == 'peasant':
                row = 0
                col = 0

                self.characters['peasant'] = {
                    'name': 'Крестьянин',
                    'block_name': 'peasant',
                    'type': 'character',
                    'group': 0,
                    'attack': (4, 7),
                    'time_attack': self.fps // 3,
                    'health': 100,
                    'speed_regeneration': 0.01,
                    'speed': 1.2,
                    'range_visibility': 5,
                    'anim': dict(),
                    'dead_anim': self.effects['dead']
                }
                anim = dict()
                for key_texture, value_texture in value.items():
                    right = {
                        'texture': value_texture,
                        'size_block': (value_texture.get_width(),
                                       value_texture.get_height())
                    }

                    left = {
                        'texture': pygame.transform.flip(value_texture, True, False),
                        'size_block': (value_texture.get_width(),
                                       value_texture.get_height())
                    }

                    if row == 0:
                        if col == 0:
                            anim['idle_right'] = []
                            anim['idle_left'] = []
                        anim['idle_right'].append(right)
                        anim['idle_left'].append(left)
                    if row == 1:
                        if col == 0:
                            anim['move_right'] = []
                            anim['move_left'] = []
                        anim['move_right'].append(right)
                        anim['move_left'].append(left)
                    if row == 2:
                        if col == 0:
                            anim['build_right'] = []
                            anim['build_left'] = []
                        anim['build_right'].append(right)
                        anim['build_left'].append(left)
                    if row == 3:
                        if col == 0:
                            anim['attack_right'] = []
                            anim['attack_left'] = []
                        anim['attack_right'].append(right)
                        anim['attack_left'].append(left)
                    if row == 4:
                        if col == 0:
                            anim['idle_keep_right'] = []
                            anim['idle_keep_left'] = []
                        anim['idle_keep_right'].append(right)
                        anim['idle_keep_left'].append(left)
                    if row == 5:
                        if col == 0:
                            anim['move_keep_right'] = []
                            anim['move_keep_left'] = []
                        anim['move_keep_right'].append(right)
                        anim['move_keep_left'].append(left)

                    col += 1
                    if col == 6:
                        row += 1
                        col = 0
                self.characters['peasant']['anim'] = anim.copy()

            if key == 'warrior':
                row = 0
                col = 0

                self.characters['warrior'] = {
                    'name': 'Воин',
                    'block_name': 'warrior',
                    'type': 'character',
                    'group': 0,
                    'health': 300,
                    'speed_regeneration': 0.025,
                    'attack': (8, 12),
                    'type_attack': 'melee',
                    'time_attack': self.fps // 3,
                    'speed': 1.2,
                    'range_visibility': 5,
                    'anim': dict(),
                    'dead_anim': self.effects['dead']
                }
                anim = dict()
                for key_texture, value_texture in value.items():
                    right = {
                        'texture': value_texture,
                        'size_block': (value_texture.get_width(),
                                       value_texture.get_height())
                    }

                    left = {
                        'texture': pygame.transform.flip(value_texture, True, False),
                        'size_block': (value_texture.get_width(),
                                       value_texture.get_height())
                    }

                    if row == 0:
                        if col == 0:
                            anim['idle_right'] = []
                            anim['idle_left'] = []
                        anim['idle_right'].append(right)
                        anim['idle_left'].append(left)
                    if row == 1:
                        if col == 0:
                            anim['move_right'] = []
                            anim['move_left'] = []
                        anim['move_right'].append(right)
                        anim['move_left'].append(left)
                    if row == 2:
                        if col == 0:
                            anim['attack_right'] = []
                            anim['attack_left'] = []
                        anim['attack_right'].append(right)
                        anim['attack_left'].append(left)
                    if row == 3:
                        if col == 0:
                            anim['attack_right_1'] = []
                            anim['attack_left_1'] = []
                        anim['attack_right_1'].append(right)
                        anim['attack_left_1'].append(left)

                    col += 1
                    if col == 6:
                        row += 1
                        col = 0
                self.characters['warrior']['anim'] = anim.copy()

            if key == 'archer':
                row = 0
                col = 0

                self.characters['archer'] = {
                    'name': 'Лучник',
                    'block_name': 'archer',
                    'type': 'character',
                    'group': 0,
                    'health': 100,
                    'speed_regeneration': 0.015,
                    'attack': (4, 12),
                    'time_attack': self.fps // 3,
                    'type_attack': 'melee',
                    'speed': 1.2,
                    'range_visibility': 5,
                    'anim': dict(),
                    'dead_anim': self.effects['dead']
                }
                anim = dict()
                for key_texture, value_texture in value.items():
                    right = {
                        'texture': value_texture,
                        'size_block': (value_texture.get_width(),
                                       value_texture.get_height())
                    }

                    left = {
                        'texture': pygame.transform.flip(value_texture, True, False),
                        'size_block': (value_texture.get_width(),
                                       value_texture.get_height())
                    }

                    if row == 0:
                        if col == 0 and col < 6:
                            anim['idle_right'] = []
                            anim['idle_left'] = []
                        anim['idle_right'].append(right)
                        anim['idle_left'].append(left)
                    if row == 1 and col < 6:
                        if col == 0:
                            anim['move_right'] = []
                            anim['move_left'] = []
                        anim['move_right'].append(right)
                        anim['move_left'].append(left)
                    if row == 4:
                        if col == 0:
                            anim['attack_right'] = []
                            anim['attack_left'] = []
                        anim['attack_right'].append(right)
                        anim['attack_left'].append(left)

                    col += 1
                    if col == 6:
                        row += 1
                        col = 0
                self.characters['archer']['anim'] = anim.copy()

            if key == 'goblin':
                row = 0
                col = 0

                self.characters['goblin'] = {
                    'name': 'Гоблин',
                    'block_name': 'goblin',
                    'type': 'character',
                    'group': 2,
                    'health': 120,
                    'speed_regeneration': 0.035,
                    'attack': (3, 7),
                    'time_attack': self.fps // 2.5,
                    'type_attack': 'melee',
                    'speed': 1.2,
                    'range_visibility': 5,
                    'anim': dict(),
                    'dead_anim': self.effects['dead']
                }
                anim = dict()
                for key_texture, value_texture in value.items():
                    right = {
                        'texture': value_texture,
                        'size_block': (value_texture.get_width(),
                                       value_texture.get_height())
                    }

                    left = {
                        'texture': pygame.transform.flip(value_texture, True, False),
                        'size_block': (value_texture.get_width(),
                                       value_texture.get_height())
                    }

                    if row == 0:
                        if col == 0:
                            anim['idle_right'] = []
                            anim['idle_left'] = []
                        anim['idle_right'].append(right)
                        anim['idle_left'].append(left)
                    if row == 1 and col < 6:
                        if col == 0:
                            anim['move_right'] = []
                            anim['move_left'] = []
                        anim['move_right'].append(right)
                        anim['move_left'].append(left)
                    if row == 2 and col < 6:
                        if col == 0:
                            anim['attack_right'] = []
                            anim['attack_left'] = []
                        anim['attack_right'].append(right)
                        anim['attack_left'].append(left)

                    col += 1
                    if col == 6:
                        row += 1
                        col = 0
                self.characters['goblin']['anim'] = anim.copy()

            if key == 'sheep':
                row = 0
                col = 0

                self.characters['sheep'] = {
                    'name': 'Овца',
                    'block_name': 'sheep',
                    'type': 'character',
                    'group': 1,
                    'health': 1,
                    'speed_regeneration': 0,
                    'type_attack': '',
                    'speed': 1.2,
                    'range_visibility': 5,
                    'anim': dict(),
                    'dead_anim': self.effects['dead']
                }
                anim = dict()
                for key_texture, value_texture in value.items():
                    right = {
                        'texture': value_texture,
                        'size_block': (value_texture.get_width(),
                                       value_texture.get_height())
                    }

                    left = {
                        'texture': pygame.transform.flip(value_texture, True, False),
                        'size_block': (value_texture.get_width(),
                                       value_texture.get_height())
                    }

                    if row == 0:
                        if col == 0:
                            anim['idle_right'] = []
                            anim['idle_left'] = []
                        anim['idle_right'].append(right)
                        anim['idle_left'].append(left)
                    if row == 1 and col < 6:
                        if col == 0:
                            anim['move_right'] = []
                            anim['move_left'] = []
                        anim['move_right'].append(right)
                        anim['move_left'].append(left)

                    col += 1
                    if col == 6:
                        row += 1
                        col = 0
                self.characters['sheep']['anim'] = anim.copy()

    # Получение файлов по определённому пути
    def get_files(self, directory, format=None):
        files = []
        for filename in os.listdir(directory):
            if format is not None:
                if filename.endswith(format):
                    files.append({
                        'name': filename,
                        'path': os.path.join(directory, filename)
                    })
            else:
                files.append({
                    'name': filename,
                    'path': os.path.join(directory, filename)
                })
        return files
