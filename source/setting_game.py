import pygame
from source.database import db_session
from source.database.settings import SettingModel


# Класс настроек
class SettingGame:
    # Инициализация параметров
    def __init__(self):
        db_session.global_init("game.db")
        self.db = db_session.create_session()
        self.full_screen = False
        self.resolution = (1600, 900)
        if self.resolution not in pygame.display.list_modes():
            self.resolution = pygame.display.list_modes()[0]
        self.volume_sound = 1
        self.volume_music = 1
        self.fps = 60
        self.show_fps = True

        self.load_settings()
        self.fps_k = self.fps // 30
        self.size_k = (self.resolution[0] / 1920, self.resolution[1] / 1080)
        self.size_block = (round(64 * self.size_k[0]), round(64 * self.size_k[1]))

    # Загрузка настроек
    def load_settings(self):
        data = self.db.query(SettingModel).filter(SettingModel.name == 'full_screen').first()
        if data:
            if int(data.value):
                self.full_screen = True
            else:
                self.full_screen = False

        data = self.db.query(SettingModel).filter(SettingModel.name == 'resolution').first()
        if data:
            self.resolution = tuple(map(int, data.value.split('x')))

        data = self.db.query(SettingModel).filter(SettingModel.name == 'volume_sound').first()
        if data:
            self.volume_sound = int(data.value)

        data = self.db.query(SettingModel).filter(SettingModel.name == 'volume_music').first()
        if data:
            self.volume_music = int(data.value)

        data = self.db.query(SettingModel).filter(SettingModel.name == 'fps').first()
        if data:
            self.fps = int(data.value)

        data = self.db.query(SettingModel).filter(SettingModel.name == 'show_fps').first()
        if data:
            if int(data.value):
                self.show_fps = True
            else:
                self.show_fps = False

    # Сохранение настроек
    def save_settings(self, settings):
        for key, value in settings.items():
            row = self.db.query(SettingModel).filter(SettingModel.name == key).first()
            if row:
                row.value = value
            else:
                new_row = SettingModel()
                new_row.name = key
                new_row.value = value
                self.db.add(new_row)

        self.db.commit()
