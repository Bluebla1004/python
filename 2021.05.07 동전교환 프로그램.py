#500원 100원 50원 10원 단위로 변환
#사용자가 임의의 돈을 입력함.

c500, c100, c50, c10=0,0,0,0
money = int(input("교환할돈은 얼마인가요:"))
c500 = money//500
money %=500

c100 = money//100
money %=100

c50 = money//50
money %=50

c10 = money//10
money %=10


print("\n 500원자리 ==>%d개"%c500)
print("\n 100원자리 ==>%d개"%c100)
print("\n 50원자리 ==>%d개"%c50)
print("\n 10원자리 ==>%d개"%c10)
print("바꾸지못한 잔돈 ==>%d원\n"%money)
