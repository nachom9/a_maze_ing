import random

class MazeGenerator:

    def __init__(self, limits):
        self.limits = limits
        self.squares = {}
        self.walls = {}
    
    @classmethod
    def get_hex(cls, maze, coord: tuple, limits: tuple):
        
        walls = cls.get_walls(maze, coord, limits)
        hex_sequence = '0123456789ABCDEF'
        hex_number = (walls['north'] + (walls['east'] * 2) + (walls['south'] * 4)
                      + (walls['west'] * 8))
        hex = hex_sequence[hex_number]
        maze.squares[coord] = hex
        maze.walls[coord] = walls

        return(hex)

    @classmethod
    def get_walls(cls, maze, coord: tuple, limits: tuple):

        walls = {'west': 0,
                 'south': 0,
                 'east': 0,
                 'north': 0}
        row = coord[0]
        col = coord[1]
        close_count = 0

        if col == 0 or maze.walls[(row, col - 1)]['east'] == 1:
            walls['west'] = 1
            close_count += 1
        if row == 0 or maze.walls[(row - 1, col)]['south'] == 1:
            walls['north'] = 1
            close_count += 1
        if row == (limits[0] - 1):
            walls['south'] = 1
            close_count += 1
        if col == (limits[1] - 1):
            walls['east'] = 1
            close_count += 1
        
        for key, value in walls.items():
            if ((col != 0 and key == 'west' and maze.walls[(row, col - 1)]['east'] == 0)
                or
                (row != 0 and key == 'north' and maze.walls[(row - 1, col)]['south'] == 0)
                ):
                if value == 1:
                    value = 0
                    close_count -= 1
            else:
                if value == 0 and close_count < 4:
                    walls[key] = random.choice(range(0, 2))
                if walls[key] == 1:
                    close_count += 1
        
        return(walls)


def main():

    row_count = 0
    col_count = 0
    limits = (5, 5)

    maze = MazeGenerator((5, 5))
    while row_count < maze.limits[0]:
        while col_count < maze.limits[1]:
            MazeGenerator.get_hex(maze, (row_count, col_count), maze.limits)
            col_count += 1
        maze.squares[(row_count, col_count)] = '\n'
        row_count += 1
        col_count = 0
    print()
    for value in maze.squares.values():
        print(value, end='')
    for value in maze.walls.values():
        print(value)


if __name__ == "__main__":
    main()
