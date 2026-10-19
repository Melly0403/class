def line():
    print('-'*15)

print('시작')
line()
print('중간')
line()
print('끝')


def profile(name, age, major):
    print('이름:',name)
    print('나이:',age)
    print('전공:',major)
profile(major='경영학',name='서연',age='21')


def total(*nums):
    print('받은값:', nums)
    s = 0
    for n in nums:
        s += n
    print('합계:', s)
total(1, 2)
total(10, 20, 30, 40)