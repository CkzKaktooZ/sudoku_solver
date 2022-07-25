from math import floor
from typing import List


def is_number_possible(grid: List[list], num: int, row: int, col: int) -> bool:
    # Check if doesn't exist in row
    for i in range(0, len(grid[row])):
        if grid[row][i] == num:
            return False
    # Check if doesn't exist in column
    for i in range(0, len(grid)):
        if grid[i][col] == num:
            return False
    return check_mini_cube(grid=grid, row=row, column=col, num=num)


def insert_num(current_grid: List[list], num: int, row: int, col: int) -> List[list]:
    new_grid = current_grid.copy()
    new_grid[row][col] = num
    return new_grid


def solve(grid: List[list], empty_slots_to_fill: List[tuple]) -> bool:
    if not empty_slots_to_fill:
        print_grid(grid_to_print=grid)
        return True

    for row_index, col_index in empty_slots_to_fill:
        for num in range(1, len(grid)+1):
            if is_number_possible(grid=grid, num=num, row=row_index, col=col_index):
                updated_grid = insert_num(current_grid=grid, num=num, row=row_index, col=col_index)
                if solve(grid=updated_grid, empty_slots_to_fill=empty_slots_to_fill[1:]):
                    return True
                else:
                    updated_grid = insert_num(current_grid=grid, num=0, row=row_index, col=col_index)
        return False


def print_grid(grid_to_print: List[list]):
    for row in range(0, len(grid_to_print)):
        for column in range(0, len(grid_to_print[row])):
            print(grid_to_print[row][column], end=" ")
        print("")
    else:
        print("-"*17)


def detect_empty_slots(grid_with_empty_slots: List[list], empty_token=0) -> List[tuple]:
    slots_to_fill = []
    for row_index, row in enumerate(grid_with_empty_slots):
        for column_index, value in enumerate(row):
            if value == empty_token:
                slots_to_fill.append((row_index, column_index))
    return slots_to_fill


def check_mini_cube(grid: List[list], row: int, column: int, num: int) -> bool:
    row_multiplier = floor(row/3)
    column_multiplier = floor(column/3)
    
    for row_index in range(0, 3):
        for column_index in range(0, 3):
            if grid[row_index+row_multiplier*3][column_index+column_multiplier*3] == num:
                return False
    return True


if __name__ == '__main__':
    grid_1 = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
              [0, 1, 0, 0, 0, 4, 0, 0, 0],
              [4, 0, 7, 0, 0, 0, 2, 0, 8],
              [0, 0, 5, 2, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 9, 8, 1, 0, 0],
              [0, 4, 0, 0, 0, 3, 0, 0, 0],
              [0, 0, 0, 3, 6, 0, 0, 7, 2],
              [0, 7, 0, 0, 0, 0, 0, 0, 3],
              [9, 0, 3, 0, 0, 0, 6, 0, 4]]

    grid_2 = [[0, 0, 0, 0, 0, 4, 0, 9, 0],
              [8, 0, 2, 9, 7, 0, 0, 0, 0],
              [9, 0, 1, 2, 0, 0, 3, 0, 0],
              [0, 0, 0, 0, 4, 9, 1, 5, 7],
              [0, 1, 3, 0, 5, 0, 9, 2, 0],
              [5, 7, 9, 1, 2, 0, 0, 0, 0],
              [0, 0, 7, 0, 0, 2, 6, 0, 3],
              [0, 0, 0, 0, 3, 8, 2, 0, 5],
              [0, 2, 0, 5, 0, 0, 0, 0, 0]]

    solution_2 = """
                7 3 5 | 6 1 4 | 8 9 2 
                8 4 2 | 9 7 3 | 5 6 1 
                9 6 1 | 2 8 5 | 3 7 4
                --------------------- 
                2 8 6 | 3 4 9 | 1 5 7 
                4 1 3 | 8 5 7 | 9 2 6 
                5 7 9 | 1 2 6 | 4 3 8 
                ---------------------
                1 5 7 | 4 9 2 | 6 8 3 
                6 9 4 | 7 3 8 | 2 1 5 
                3 2 8 | 5 6 1 | 7 4 9 """
    empty_slots = detect_empty_slots(grid_with_empty_slots=grid_2)
    solution = solve(grid=grid_2, empty_slots_to_fill=empty_slots)

    print(solution_2)