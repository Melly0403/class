dance = {'민준', '서연', '하윤'}
band = {'서연', '지우', '예준'}

club_all = dance | band
print("1", club_all)
print("2", dance & band)
print("3", dance - band)
dance.add('지우')
print("4", dance)
band.remove('예준')
print("5", band)