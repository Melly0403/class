name = input('이름입력: ')
print('안녕하세요', name, '님')
name = input('이름입력: ')
print('입력하신이름은%s '%name)

a= int(input('첫번째숫자입력: '))
b= int(input('두번째숫자입력: '))
print('%d/%d=%f' % (a, b, a/b))

a= int(input('첫번째숫자입력: '))
b= int(input('두번째숫자입력: '))
print('{0} X {1} = {2}'.format(a, b, a*b))
print('{1} X {0} = {2}'.format(a, b, a*b))

print('{1}{1} 빛나는작은{0}'.format('별','반짝'))