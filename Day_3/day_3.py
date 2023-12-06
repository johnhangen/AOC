#!/usr/bin/python3
# -*- coding: utf-8 -*-

from file_reader import read_file
import numpy as np


def part_one():
    contents = read_file('Day_3/day_3.txt')

    matrix = [[char for char in line] for line in contents.split('\n')]
    height = len(matrix)
    width = len(matrix[0])

    total = 0
    current_number = []

    for i, line in enumerate(matrix):
        for j, char in enumerate(line):
            if char.isdigit():
                current_number.append(char)
            else:
                if current_number:
                    number = int(''.join(current_number))
                    current_number = []

                    surrounding_elements = set()
                    for k in {max(i - 1, 0), i, min(i + 1, height - 1)}:
                        for l in range(max(j - len(str(number)) - 1, 0), min(j + 1, width)):
                            if not matrix[k][l].isdigit() and matrix[k][l] != '.':
                                surrounding_elements.add(matrix[k][l])

                    if not len(surrounding_elements) == 0:
                        total += number

    # 556448
    # 549292
    # 64954
    print(total)

def part_two():
    pass


def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()
