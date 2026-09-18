colors = ['빨강', '노랑']
colors.append('초록')
print(colors)               # (        )
colors.pop()
print(colors)               # (        )
colors.insert(1, '파랑')
print(colors)               # (        )
print(colors.index('파랑')) # (        )
print(len(colors))          # (        )

score = [88,92, 75, 100, 63]
print(score[2])  #( )
print(score[:3])    #( )
print(score[-1])    #( )
print(score[2:4])   #( )
print(score[3:])    #( )