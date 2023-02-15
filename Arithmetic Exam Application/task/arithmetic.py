import random
import re

operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
}

def main():
    x = random.randint(2, 9)
    y = random.randint(2, 9)
    operator = random.choice(list(operators.keys()))
    print(x, operator, y)
    a = int(input())
    print('Right!' if a == operators[operator](x, y) else 'Wrong!')


if __name__ == '__main__':
    main()
