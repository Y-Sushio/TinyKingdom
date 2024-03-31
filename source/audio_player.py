import pygame
from pygame.mixer import Sound


# Класс аудио-плеера
class AudioPlayer:
    def __init__(self, music_path, volume_music=1, volume_sound=1):
        pygame.mixer.init()
        self.volume_music = volume_music / 100
        self.volume_sound = volume_sound / 100
        self.sounds = dict()
        self.music_path = music_path

    # Функция проигрывания музыки
    def play_music(self, name_music):
        pygame.mixer.music.load(self.music_path[name_music])
        pygame.mixer.music.set_volume(self.volume_music)
        pygame.mixer.music.play(-1)

    # Функция остановки проигрывания музыки
    def stop_music(self):
        pygame.mixer.music.stop()

    # Функция проигрывания звуков
    def play_sound(self, name_sound):
        self.sounds[name_sound].play()

    def load_sounds(self, path_sounds):
        for key, value in path_sounds.items():
            self.sounds[key] = Sound(value)
            self.sounds[key].set_volume(self.volume_sound)
