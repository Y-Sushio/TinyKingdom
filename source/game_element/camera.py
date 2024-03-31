# Класс камеры
class Camera:
    # Инициализация параметров
    def __init__(self, min_x, min_y, max_x, max_y, setting_game):
        self.setting_game = setting_game
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.set_max_x(max_x)
        self.max_y = max_y
        self.set_max_y(max_y)
        self.pos_camera_x = 0
        self.pos_camera_y = 0
        self.left_move_border = self.setting_game.resolution[0] // 50
        self.right_move_border = self.setting_game.resolution[0] - (self.setting_game.resolution[0] // 50)
        self.top_move_border = self.setting_game.resolution[1] // 50
        self.bottom_move_border = self.setting_game.resolution[1] - (self.setting_game.resolution[1] // 50)
        self.speed_x = self.speed_y = 12 // self.setting_game.fps_k

    # Установка максимального значения камеры по x
    def set_max_x(self, max_x):
        self.max_x = max_x
        if self.setting_game.resolution[0] > self.max_x:
            self.max_x = 0
        else:
            self.max_x -= self.setting_game.resolution[0]

    # Установка максимального значения камеры по y
    def set_max_y(self, max_y):
        self.max_y = max_y
        if self.setting_game.resolution[1] > self.max_y:
            self.max_y = 0
        else:
            self.max_y -= self.setting_game.resolution[1]

    # Обновление камеры по расположению мыши
    def update(self, mouse_pos):
        if mouse_pos[0] < self.left_move_border:
            self.pos_camera_x -= self.speed_x
        elif mouse_pos[0] > self.right_move_border:
            self.pos_camera_x += self.speed_x

        if mouse_pos[1] < self.top_move_border:
            self.pos_camera_y -= self.speed_y
        elif mouse_pos[1] > self.bottom_move_border:
            self.pos_camera_y += self.speed_y

        if self.pos_camera_x < self.min_x:
            self.pos_camera_x = self.min_x
        if self.pos_camera_x > self.max_x:
            self.pos_camera_x = self.max_x
        if self.pos_camera_y < self.min_y:
            self.pos_camera_y = self.min_y
        if self.pos_camera_y > self.max_y:
            self.pos_camera_y = self.max_y

    # Получение смещения объектов по отношению к центрированию камеры
    def get_offset(self, rect):
        new_rect = rect.copy()
        new_rect.x -= self.pos_camera_x
        new_rect.y -= self.pos_camera_y
        return new_rect
