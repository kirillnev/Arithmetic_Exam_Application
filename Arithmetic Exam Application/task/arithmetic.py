import random
import re

operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
}
TASKS_COUNT = 5


def main():
    n = 0
    correct_n = 0
    while n < TASKS_COUNT:
        x = random.randint(2, 9)
        y = random.randint(2, 9)
        operator = random.choice(list(operators.keys()))
        print(x, operator, y)
        while True:
            answer = input()
            if re.match(r'^-?\d+$', answer):
                answer = int(answer)
                if answer == operators[operator](x, y):
                    print('Right!')
                    correct_n += 1
                else:
                    print('Wrong!')
                n += 1
                break
            else:
                print('Incorrect format.')
    print(f'Your mark is {correct_n}/{TASKS_COUNT}.')


if __name__ == '__main__':
    main()
