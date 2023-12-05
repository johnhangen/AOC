#!/usr/bin/python3
# -*- coding: utf-8 -*-


def read_file(file_path: str) -> str:
    with open(file_path, 'r') as f:
        contents = f.read()
    
    return contents