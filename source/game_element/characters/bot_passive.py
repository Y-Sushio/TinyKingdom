import random

from source.game_element.characters.base_character import BaseCharacter


# Класс безобидных ботов (просто ходят по карте)
class BotPassive(BaseCharacter):
    # Инициализация параметров
    def __init__(self, setting_game, params, x=0, y=0):
        super().__init__(setting_game, params, x, y)
        self.time_ai = 0
        self.time_ai_max = 0

    # Функция логики ботов
    def ai_controller(self):
        if self.path_target:
            pass
        elif self.time_ai > 0:
            self.time_ai += 1

            if self.time_ai_max < self.time_ai:
                self.time_ai = 0
        elif self.ai_map:
            if random.randint(0, 1):
                temp = self.ai_map[self.row_current][self.column_current]
                temp = random.choice(temp)
                temp = random.choice(temp)
                if temp is not None:
                    temp = temp.copy()
                self.path_target = temp
            else:
                self.time_ai_max = random.randint(self.setting_game.fps * 3, self.setting_game.fps * 3)
                self.time_ai = 1
                self.new_status('idle')
