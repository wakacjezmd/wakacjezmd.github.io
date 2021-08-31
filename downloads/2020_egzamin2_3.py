#!/usr/bin/python3

x = [0, 0b1, 0b10, 0b100, 0b1000, 0b10000, 0b100000]
p = [[1, 3, 4, 5, 6], [1, 3, 5, 6], [1, 2, 3, 5], [1, 2, 3, 4, 6], [2, 4, 5, 6], [1, 2, 4, 6]]

expressions = [0]

for par in p:
    new_expressions = [] 
    for j in par:
        for exp in expressions:
            new_expressions.append(exp + x[j])
    expressions = new_expressions

cnt = 0

for exp in expressions:
    if exp == 0b111111:
        cnt += 1

print(cnt)
