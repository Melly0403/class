import random
options = ['가위', '바위', '보']
com = random.choice(options)
me = input('가위, 바위, 보 중 하나입력: ')
if me == '가위':
    if com == '가위':
        result = '비김'
    elif com == '바위':
        result = '짐'
    else:
        result = '이김'
elif me == '바위':
    if com == '가위':
        result = '이김'
    elif com == '바위':
        result = '비김'
    else:
        result = '짐'
else :
    if com == '가위':
        result = '짐'
    elif com == '바위':
        result = '이김'
    else:
        result = '비김'
if me in options:
    print('나:', me, ', 컴퓨터:', com, '->', result)
else:
    print('잘못입력하셨습니다. 다시입력하세요.')