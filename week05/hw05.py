#1번 문제
score = [100, 70, 60, 80, 90]
print("수강 과목 수 :", len(score))
for s in score:
    print("score :", s)
passscore = 0
failscore = 0
for s in score:
    if s >= 80:
        passscore+= 1
    else:
        failscore+= 1
print()
print("pass :", passscore)
print("fail :", failscore)


#2번 문제
heart = input("정수 입력 : ")
for n in heart:
    number = int(n)
    print("❤️" * number)


#3번문제
alpha = {'A':'1!','B':'2@','C':'3#','D':'4$','E':'5%'}

while True:
    count = input("대문자 A~E 단어 입력(종료:0)")
    if count == '0':
        break  
    code = ""
    for ch in count:
        code += alpha[ch]
    print("암호 :", code)