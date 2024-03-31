from source.game_element.characters.base_character import BaseCharacter


# Класс ботов ближнего боя
class BotMelee(BaseCharacter):
    # Инициализация параметров
    def __init__(self, setting_game, params, x=0, y=0):
        super().__init__(setting_game, params, x, y)

    # Функция логики ботов
    def ai_controller(self):
        pass
