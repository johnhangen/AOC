#!/usr/bin/python3
# -*- coding: utf-8 -*-

from file_reader import read_file


def part_one():
    contents = read_file('Day_1/day_1.txt')

    total = 0
    line_nums = []

    for line in contents.split('\n'):
        line_nums = [c for c in line if c in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']]
        total += int(line_nums[0] + line_nums[-1])
        line_nums = []

    print(f'Total: {total}')


def part_two():
    total = 0
    line_nums = []
    line_text = []

    numbers_mapping = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    contents = read_file('Day_1/day_1.txt')

    for line in contents.split('\n'):
        for char in line:
            if char in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                line_nums.append(char)
           
            line_text.append(char)

            for key, value in numbers_mapping.items():
                if key in ''.join(line_text):
                    line_nums.append(value)
                    line_text = list(''.join(line_text).replace(key[0], ''))

        total += int(str(line_nums[0]) + str(line_nums[-1]))
        line_nums = []
        line_text = []

    print(f'Total: {total}')


def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()
