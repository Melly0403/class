def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if b == 0:
        return '0으로 나눌 수 없음'
    return a / b
while True:
    op = input('연산(+ - * /), 종료 q : ')
    if op == 'q':
        print('계산기를 종료합니다.')
        break
    if op in ('+', '-', '*', '/'):
        num1 = int(input('첫 번째 수 : '))
        num2 = int(input('두 번째 수 : '))
        if op == '+':
            result = add(num1, num2)
        elif op == '-':
            result = sub(num1, num2)
        elif op == '*':
            result = mul(num1, num2)
        elif op == '/':
            result = div(num1, num2)
        print(f'결과 : {result}')