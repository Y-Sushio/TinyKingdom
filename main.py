import ctypes
import os.path
import pygame
from source.windows.game import Game
from source.ui.loading import Loading
from source.windows.main_menu import MainMenu
from source.audio_player import AudioPlayer
from source.setting_game import SettingGame
from source.windows.designer_map import DesignerMap
from source.resource_registry import ResourceRegistry
from source.windows.settings_menu import SettingsMenu
from source.windows.statistics_menu import StatisticsMenu
from source.windows.map_new_or_load_menu import MapNewOrLoadMenu


# Главная функция
def main():
    pygame.init()
    ctypes.windll.user32.SetProcessDPIAware()
    pygame.display.set_caption('TinyKingdom')

    setting_game = SettingGame()

    if setting_game.full_screen:
        screen = pygame.display.set_mode(setting_game.resolution, pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(setting_game.resolution)
    reg = ResourceRegistry(setting_game.size_k, setting_game.fps)

    # Экран загрузки
    Loading(resolution=setting_game.resolution,
            font=reg.fonts['Konstanting'],
            size_k=setting_game.size_k).draw(screen)

    audio_player = AudioPlayer(reg.audio_music_path, setting_game.volume_music, setting_game.volume_sound)
    audio_player.play_music('menu')
    pygame.display.set_icon(reg.icon)
    reg.load_registry()
    audio_player.load_sounds(reg.audio_sounds_path)

    # Скрыть системный курсор
    pygame.mouse.set_visible(False)

    window = 'main_menu'
    while window != 'exit' and window != 'restart':
        if window == 'main_menu':
            menu = MainMenu(screen, setting_game, audio_player, reg)
            window = menu.run_window()

        if window == 'map_new_or_load_menu':
            menu = MapNewOrLoadMenu(screen, setting_game, audio_player, reg)
            window = menu.run_window()

        if window == 'designer_map':
            designer = DesignerMap(screen, setting_game, audio_player, reg)
            window = designer.run_window()

        if 'designer_map_' in window:
            Loading(resolution=setting_game.resolution,
                    font=reg.fonts['Konstanting'],
                    size_k=setting_game.size_k).draw(screen)

            designer = DesignerMap(screen, setting_game, audio_player, reg, window.replace('designer_map_', ''))
            window = designer.run_window()

        if window == 'settings_menu':
            menu = SettingsMenu(screen, setting_game, audio_player, reg)
            window = menu.run_window()
            if menu.data_save:
                setting_game.save_settings(menu.data_save)

        if 'game_' in window:
            Loading(resolution=setting_game.resolution,
                    font=reg.fonts['Konstanting'],
                    size_k=setting_game.size_k).draw(screen)

            audio_player.play_music('game')
            game = Game(screen, setting_game, audio_player, reg, window.replace('game_', ''))
            window = game.run_window()
            audio_player.play_music('menu')

        if window == 'statistics_menu' and os.path.exists('statistics.json'):
            menu = StatisticsMenu(screen, setting_game, audio_player, reg)
            window = menu.run_window()

    pygame.quit()
    if window == 'restart':
        return True
    else:
        return False


# Запуск игры, если restart == True игра перезапускается
if __name__ == '__main__':
    restart = True
    while restart:
        restart = main()
