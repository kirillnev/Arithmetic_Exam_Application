import random
import re

operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
}
TASKS_COUNT = 5
lvl_descr = {
    '1': "simple operations with numbers 2-9",
    '2': "integral squares 11-29"
}


def start_level1():
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
    return correct_n


def start_level2():
    n = 0
    correct_n = 0
    while n < TASKS_COUNT:
        x = random.randint(11, 29)
        print(x)
        while True:
            answer = input()
            if answer.isdigit():
                answer = int(answer)
                if answer == x**2:
                    print('Right!')
                    correct_n += 1
                else:
                    print('Wrong!')
                n += 1
                break
            else:
                print('Incorrect format.')
    return correct_n


def save_result(n, lvl_num):
    print("What is your name?")
    name = input()
    res_str = f"{name}: {n}/5 in level {lvl_num} ({lvl_descr[lvl_num]})."
    with open('results.txt', 'a') as f:
        f.write(res_str)
    print('The results are saved in "results.txt".')


def main():
    while True:
        print('Which level do you want? Enter a number:')
        print('1 - simple operations with numbers 2-9')
        print('2 - integral squares 11-29')
        lvl_num = input()
        if lvl_num == '1':
            correct_n = start_level1()
            break
        elif lvl_num == '2':
            correct_n = start_level2()
            break
        else:
            print('Incorrect format.')
    print(f'Your mark is {correct_n}/{TASKS_COUNT}. Would you like to save the result? Enter yes or no.')
    cmd = input()
    if cmd in ['yes', 'YES', 'y', 'Yes']:
        save_result(correct_n, lvl_num)


if __name__ == '__main__':
    main()
