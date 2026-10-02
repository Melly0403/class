# #1번 문제
count = 1
while count <= 3:
    print('충전중...', count * 30, '%')
    count += 1

print('충전완료\n')


# #2번 문제
count = 1
while count <= 4:
    error = input("충전 오류가 발생했나요?(y/n):")
    if error == 'y':
        print('충전중단!')
        break
    print('충전 중...', count * 25, '%')
    count += 1
else:
    print('충전 완료!')