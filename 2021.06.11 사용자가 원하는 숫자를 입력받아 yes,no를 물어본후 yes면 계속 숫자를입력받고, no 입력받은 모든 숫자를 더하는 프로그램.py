total=0
answer="y"
while answer == "y":
    number=float(input("숫자를 입력하시오:"))
    total=total+number
    answer=input("계속? (y/n):")
print("합계:",total)
