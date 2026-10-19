#1번 문제 (온도 단위 변환)
dg = float(input("현재 온도는?: "))
unit = input("입력하신 온도의 단위는? (C 또는 F): ")
if unit.upper() == 'C':
    converted = (dg * 9/5) + 32
    print(f"변환된 화씨 온도: {converted:.2f}°F")
elif unit.upper() == 'F':
    converted = (5/9) * (dg - 32)
    print(f"변환된 섭씨 온도: {converted:.2f}°C")
else:
    print("MISS 'C' 또는 'F'를 입력")

#2번 문제
month = int(input("월(month)은? (1~12): "))
if 3 <= month <= 5:
    print(f"{month}월은 **봄**")
elif 6 <= month <= 8:
    print(f"{month}월은 **여름**")
elif 9 <= month <= 11:
    print(f"{month}월은 **가을**")
elif month == 12 or month == 1 or month == 2:
    print(f"{month}월은 **겨울**입니다.")
else:
    print("MISS 1부터 12 사이의 숫자를 입력")


#4번 문제
total_price = int(input("주문 금액을 입력하세요 (원): "))
if total_price >= 50000:
    discount_rate = 0.20 
elif total_price >= 30000:
    discount_rate = 0.10 
elif total_price >= 10000:
    discount_rate = 0.05  
else:
    discount_rate = 0.0  
discount_amount = total_price * discount_rate
final_price = total_price - discount_amount
print("주문 금액:", total_price, "원")
print("할인 금액:", int(discount_amount), "원")
print("최종 결제 금액:", int(final_price), "원")
