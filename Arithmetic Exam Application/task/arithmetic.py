import re


def main():
    example = input()
    pattern = r'(\d+) ([\+\-\*]) (\d+)$'
    re_res = re.findall(pattern, example)
    num1, operator, num2 = re_res[0]
    num1 = int(num1)
    num2 = int(num2)
    if operator == '+':
        print(num1 + num2)
    if operator == '-':
        print(num1 - num2)
    if operator == '*':
        print(num1 * num2)

if __name__ == '__main__':
    main()
