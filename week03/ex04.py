point =(10,20,30,40)
print(point[0])
print(point[-1])
print(point[1:])
print(point[:2])

menu = {'김밥': 2500, '라면': 3200}
print(menu['김밥'])
# 값수정
menu['라면'] = 3500
# 새항목추가
menu['떡볶이'] = 3500
print(menu)
print(menu['순대'])

menu = {'김밥': 2500, '라면': 3200, '떡볶이': 3500}
print(list(menu.keys()))
print(list(menu.values()))
print(list(menu.items()))

student = {202601: '민준', 202602: '서연'}
print(student.get(202601))
print(student.get(202699, '등록되지않은학번'))