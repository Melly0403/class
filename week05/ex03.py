score = [68,80, 90, 70, 95]
hap =0
for s in score:
    hap+=s
avg=hap/len(score)
print('합계 =>', hap,',평균=>',avg)
print('최댓값=>', max(score),',최솟값 =>', min(score))

import random
flag = True
correct = 0
while flag:
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    answer = int(input(str(x) + ' × ' + str(y) + ' = '))
    if answer == x * y:
        print('정답!')
        correct += 1
    else:print('틀렸어요. 정답은', x * y)
    flag = False
print('맞힌문제수:', correct)

start = int(input('시작단 입력:'))
end = int(input('종료단 입력:'))
for dan in range(start, end +1):
    for num in range(1,10):
        print(dan,'x',num,'=',dan*num,end='\t')
    print('구구단 프로그램 종료')

#도전문제4 친구 연락처 관리 프로그램
fri={}
while True:
    menu = input("1) 친구 등록 2)검색 3)종료 :")
    if menu =='1':
        name = input("name : ")
        phone = input("phone : ")
        fri[name] = phone
    elif menu =='2':
        name = input("name : ")
        if name in fri:
            print(fri[name])
        else:
            print("찾을 수 없음")
    elif menu == '3':
        break
