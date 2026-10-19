def c_to_f(c):
    f = c*9/5+32
    return f
for c in [0,25, 100]:
    print(c, '도->', c_to_f(c),'도(F)')

count = int(input("몇개의 수를 입력할까요? (1이상):"))
numbers=[]
for i in range(count):
    num = int(input(f"{i+1}번째 수 입력:"))
    numbers.append(num)

print(f"받은 값:{numbers}")
print(f"입력한 수 중 최댓값:{max(numbers)}")