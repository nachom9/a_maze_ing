import random

class MazeGenerator:

    def __init__(self, limits):
        self.limits = limits
        self.entry: (config["ENTRY"])
        self.exit: config["EXIT"]
        self.output_file: config["OUTPUT_FILE"]
        self.perfect: False
        self.center: (0,0)
        self.cells = {}
    
    def add_cell(self, cell, coord):
        self.cells[coord] = cell

    def get_hex(self, coord: tuple):
        
        hex_sequence = '0123456789ABCDEF'
        hex_number = (self.cells[coord].walls['north'] +
                      (self.cells[coord].walls['east'] * 2) +
                      (self.cells[coord].walls['south'] * 4) +
                      (self.cells[coord].walls['west'] * 8))
        hex = hex_sequence[hex_number]
        self.cells[coord].hex = hex

        return(hex)
    
    def open_walls(self, coord, limits):
        if coord == (0,0) and self.cells[coord].check:
            MazeGenerator.open_walls(self, (coord[0], coord[1] + 1), limits)
        directions = ['west', 'south', 'east', 'north']
        random.shuffle(directions)
        row = coord[0]
        col = coord[1]
        self.cells[coord].check = True

        for direction in directions:
            if direction == 'north' and row != 0:
                if not self.cells[(row - 1, col)].check:
                    self.cells[coord].walls[direction] = 0
                    self.cells[(row - 1, col)].walls['south'] = 0
                    MazeGenerator.open_walls(self, (row - 1, col), limits)
            elif direction == 'east' and col < limits[1] - 1:
                if not self.cells[(row, col + 1)].check:
                    self.cells[coord].walls[direction] = 0
                    self.cells[(row, col + 1)].walls['west'] = 0
                    MazeGenerator.open_walls(self, (row, col + 1), limits)
            elif direction == 'south' and row < limits[0] - 1:
                if not self.cells[(row + 1, col)].check:
                    self.cells[coord].walls[direction] = 0
                    self.cells[(row + 1, col)].walls['north'] = 0
                    MazeGenerator.open_walls(self, (row + 1, col), limits)
            elif direction == 'west' and col != 0:
                if not self.cells[(row, col - 1)].check:
                    self.cells[coord].walls[direction] = 0
                    self.cells[(row, col - 1)].walls['east'] = 0
                    MazeGenerator.open_walls(self, (row, col - 1), limits)
        
        self.cells[coord].hex = MazeGenerator.get_hex(self, coord)

    def clean_mazecheck(self):
        for coord in self.cells:
            if self.cells[coord].hex != 'F':
                self.cells[coord].check = False

    def maze_solution(self):
        

    def draw_fortytwo(self, limits):
        if limits[0] % 2 == 0:
            mid_row = int((limits[0] / 2) - 1)
        else:
            mid_row = int(limits[0] / 2)
        if limits[1] % 2 == 0:
            mid_col = int((limits[1] / 2) - 1)
        else:
            mid_col = int(limits[1] / 2)
        self.center = (mid_row, mid_col)

        blocked = ((mid_row, mid_col - 1), (mid_row, mid_col - 2),
                   (mid_row, mid_col - 3), (mid_row - 1, mid_col - 3),
                   (mid_row - 2, mid_col - 3), (mid_row + 1, mid_col - 1),
                   (mid_row + 2, mid_col - 1), (mid_row, mid_col + 1),
                   (mid_row, mid_col + 2), (mid_row, mid_col + 3),
                   (mid_row - 1, mid_col + 3), (mid_row - 2, mid_col + 3),
                   (mid_row - 2, mid_col + 2), (mid_row - 2, mid_col + 1),
                   (mid_row + 1, mid_col + 1), (mid_row + 2, mid_col + 1),
                   (mid_row + 2, mid_col + 2), (mid_row + 2, mid_col + 3))
        print(self.center)
        if limits[0] >= 5 and limits[1] >= 7:
            for cell in blocked:
                self.cells[cell].check = True


class Cell:

    def __init__(self, coord):
        self.coord = coord
        self.hex = 'F'
        self.walls = {'west': 1,
                 'south': 1,
                 'east': 1,
                 'north': 1}
        self.check = False

def main():

    row_count = 0
    col_count = 0
    limits = (5, 7)

    maze = MazeGenerator(limits)
    while row_count < maze.limits[0]:
        while col_count < maze.limits[1]:
            cell = Cell((row_count, col_count))
            maze.add_cell(cell, (row_count, col_count))
            col_count += 1
        row_count += 1
        col_count = 0
    MazeGenerator.draw_fortytwo(maze, limits)

    MazeGenerator.open_walls(maze, (0,0), limits)
    if maze.cells[(maze.center[0] + 1, maze.center[1] + 2)].check == False:
            MazeGenerator.open_walls(maze, (maze.center[0] + 1, maze.center[1] + 2), limits)
    if maze.cells[(maze.center[0] + 1, maze.center[1] - 2)].check == False:
            MazeGenerator.open_walls(maze, (maze.center[0] + 1, maze.center[1] - 2), limits)

    MazeGenerator.clean_mazecheck(maze)

    for key in maze.cells.keys():
        print(maze.cells[key].hex, end='')

if __name__ == "__main__":
    main()
