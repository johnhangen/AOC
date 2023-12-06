#!/usr/bin/python3
# -*- coding: utf-8 -*-

from file_reader import read_file
import numpy as np


def part_one():
    contents = read_file('Day_4/day_4.txt')

    cards = contents.split('\n')

    total = 0
    
    for card in cards:
        target, test = card.split(':')[-1].split('|')

        target = filter(lambda x: x != '', target.split(' '))
        test = filter(lambda x: x != '', test.split(' '))

        matches = set(target) & set(test)

        if len(matches) > 0:
            total += (2**len(matches))/2

    print(total)

def part_two():
    pass

def main():
    part_one()
    part_two()

if __name__ == '__main__':
    main()