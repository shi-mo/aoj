#!/usr/bin/env python3
import sys
from collections import deque

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    stack = deque()
    for token in iterate_tokens():
        if not token in '+-*':
            stack.append(int(token))
            continue

        right = stack.pop()
        left  = stack.pop()
        result = None
        if '+' == token:
            result = left + right
        if '-' == token:
            result = left - right
        if '*' == token:
            result = left * right
        stack.append(result)
    print(stack.pop())

main()
