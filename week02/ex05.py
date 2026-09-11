money = 3650

print("3650 원은")
w1000 = money // 1000
money = money % 1000
print("1000원", w1000, "개")

w500 = money // 500
money = money % 500
print("500원", w500, "개")

w100 = money // 100
money = money % 100
print("100원", w100, "개")

w10 = money // 10
money = money % 10
print("10원", w10, "개")

# 남은 잔액
print("남은 잔액(10원 미만):", money, "원")