#5만원 1만원 5천원 천원 단위로 변환하는 프로그램 작성
c50000, c10000, c5000, c1000=0,0,0,0
money = int(input("가격입력:"))
c50000 = money//50000
money %=50000

c10000 = money//10000
money %=10000

c5000 = money//5000
money %=5000

c1000 = money//1000
money %=1000


print("\n 5만원 ==>%d장"%c50000)
print("\n 1만원 ==>%d장"%c10000)
print("\n 5천원 ==>%d장"%c5000)
print("\n 1천원 ==>%d장"%c1000)
print("\n 잔돈 ==>%d원\n"%money)
