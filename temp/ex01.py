id = input('아이디: ')
print(id)
print(len(id))

print(len(id.encode('utf-8')))

#2바이트로 셈
print(len(id.encode('cp949'))) 

#문자열 자료형 - 슬라이싱 활용
words = 'good luck'
print(words[5:9])
print(words[5:])
print(words[:4])
print(words[::2])
print(words[::-1])

