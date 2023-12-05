#!/usr/bin/python3
# -*- coding: utf-8 -*-

from file_reader import read_file

def part_one():
    contents = read_file('Day_2/day_2.txt')

    RED = 12
    GREEN = 13
    BLUE = 14

    running_total = 0
    
    for line in contents.split('\n'):
        curr_red = 0
        curr_green = 0
        curr_blue = 0

        id = int(line.split(':')[0].split(' ')[1])
        line = line.split(':')[1]

        for sets in line.split(';'):
            for set in sets.split(','):
                color = set.strip().split(' ')[1]
                value = int(set.strip().split(' ')[0])

                #print(f'Color: {color}, Value: {value}')
                
                if color == 'red' and value >= curr_red:
                    curr_red = value
                elif color == 'green' and value >= curr_green:
                    curr_green = value
                elif color == 'blue' and value >= curr_blue:
                    curr_blue = value

        if curr_red <= RED and curr_green <= GREEN and curr_blue <= BLUE:
            print(f'ID: {id} is valid')
            running_total += id

    print(f'Running total: {running_total}')


def part_two():
    contents = read_file('Day_2/day_2.txt')

    running_total = 0
    
    for line in contents.split('\n'):
        curr_red = 0
        curr_green = 0
        curr_blue = 0

        id = int(line.split(':')[0].split(' ')[1])
        line = line.split(':')[1]

        for sets in line.split(';'):
            for set in sets.split(','):
                color = set.strip().split(' ')[1]
                value = int(set.strip().split(' ')[0])

                #print(f'Color: {color}, Value: {value}')
                
                if color == 'red' and value >= curr_red:
                    curr_red = value
                elif color == 'green' and value >= curr_green:
                    curr_green = value
                elif color == 'blue' and value >= curr_blue:
                    curr_blue = value

        running_total += curr_red * curr_green * curr_blue

    print(f'Running total: {running_total}')


def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()
