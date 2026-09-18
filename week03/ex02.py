"""
s = 'abc늦게출발해도def 천천히걸어가면결국도착한다'
print('원본문장:', s)
# 공백을'-'로변경
print('1 :', s.replace(' ', '-'))
# 공백기준으로단어분리
print('2 :', s.split())
# 대문자로변환
print('3 :', s.upper())
# '천' 문자의개수세기
print('4 :', s.count('천'))
# 숫자로만구성되었는지판별
print('5 :', s.isdigit())
"""

#Quiz
c = input('영어 한문장을 쓰시오: ')
print(len(c))
print(c.lower())
print(c[::-1])