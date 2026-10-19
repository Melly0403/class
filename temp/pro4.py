club = {'이혜정':'01050957663', '오세훈':'01011111111', '도경수':'01022222222'}
print(list(club.keys()))
name = input('검색할 이름:')
print(club.get(name, '등록안됨'))