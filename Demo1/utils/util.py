#!/usr/bin/python
# -*- coding: UTF-8 -*-
#给文件加最后一行
def lines(file):
    for line in file: yield line
    yield '\n'

#划分block
def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():  # 不为空行
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []


if __name__ == '__main__':
    file = "./test_input.txt"
    with open(file, 'r',encoding='UTF-8') as f:
        for block in blocks(f):
            print(block)
            print('-------------------------------')

