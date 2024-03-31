from threading import Thread


# Волновой алгоритм (взят с уроков pygame)
def has_path(grid, x1, y1, x2, y2):
    rows = grid.rows
    columns = grid.columns
    map_grid = grid.grid

    d = {(x1, y1): 0}
    v = [(x1, y1)]
    parent = {}
    while len(v) > 0:
        x, y = v.pop(0)
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx * dy != 0:
                    continue
                if x + dx < 0 or x + dx >= columns or y + dy < 0 or y + dy >= rows:
                    continue

                if 'block' not in map_grid[y + dy][x + dx].keys():
                    dn = d.get((x + dx, y + dy), -1)
                    if dn == -1:
                        d[(x + dx, y + dy)] = d.get((x, y), -1) + 1
                        v.append((x + dx, y + dy))
                        parent[(x + dx, y + dy)] = (x, y)
                elif map_grid[y + dy][x + dx]['block'].is_solid:
                    continue
                else:
                    dn = d.get((x + dx, y + dy), -1)
                    if dn == -1:
                        d[(x + dx, y + dy)] = d.get((x, y), -1) + 1
                        v.append((x + dx, y + dy))
                        parent[(x + dx, y + dy)] = (x, y)

    if (x2, y2) not in parent:
        return None

    path = [(x2, y2)]
    while path[-1] != (x1, y1):
        path.append(parent[path[-1]])
    path.reverse()
    # Строка, столбец
    return path


# Функция для вызова в потоке
def calculate_path(grid, row, col, row_move, col_move, ai_map):
    if ai_map[row_move][col_move][row][col]:
        ai_map[row][col][row_move][col_move] = ai_map[row_move][col_move][row][col][::-1]
    else:
        ai_map[row][col][row_move][col_move] = has_path(grid, row, col, row_move, col_move)


# Формирование карты маршрутов для персонажей
def get_ai_map(grid):
    if not grid:
        return []

    ai_map = [[dict() for _ in range(grid.columns)] for _ in range(grid.rows)]
    for row in range(grid.rows):
        for col in range(grid.columns):
            for row_move in range(grid.rows):
                ai_map[row][col][row_move] = dict()
                for col_move in range(grid.columns):
                    ai_map[row][col][row_move][col_move] = dict()

    threads = []
    for row in range(grid.rows):
        for col in range(grid.columns):
            for row_move in range(grid.rows):
                for col_move in range(grid.columns):
                    # Создание нового потока для вычисления пути
                    thread = Thread(target=calculate_path, args=(grid, row, col, row_move, col_move, ai_map))
                    threads.append(thread)
                    thread.start()

    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()

    return ai_map
