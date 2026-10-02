import random
answer = random.randint(1,100)
guess = 0 #이건 초기화 안해도 됨
tries = 0
print('1~100사이의 숫자를 맞혀 보세요')

while guess!= answer:
    guess = int(input('숫자 입력:'))
    tries += 1
    if guess < answer:
        print('up!')
    elif guess > answer:
        print('down!')
print("정답입니다! 시도횟수:",tries)

for ch in '파이썬':
    print(ch)

fruits =['사과','바나나','딸기']
for fruit in fruits:
    print(f'{fruit}를 좋아합니다.')

menu = {'김밥':2500, '라면':3200, '떡볶이':3500}
for m in menu:
    print(m,':',menu[m])

n = int(input('n입력:'))
total = 0
for i in range(1, n+1):
    total +=i
print('1부터', n, '까지의 합:', total)

num = int(input('단입력: '))
for a in range(1, 10):
    print(f'{num}x{i} = {num*i:2d}', end='\t')
#여기서 2d는 최소 2자리 공간에 맞추어 오른쪽 정렬로 출력하라는 뜻

#구구단 while버전
num = int(input('단입력: '))
a = 1
while a <= 9:
    print(num, '×', a, '=', num * a)
    a += 1

#!팩토리얼 계산하기
num = int(input('정수 입력:'))
fact = 1
for i in range(1,n+1):
    fact = fact*i
print(n,'!=', fact)

