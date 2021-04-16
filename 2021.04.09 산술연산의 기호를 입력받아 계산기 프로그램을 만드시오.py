a = float(input("수 입력:"))
b = input("연산기호:")#연산 기호 + - * / // % **
c = float(input("수 입력2:"))

#연산기호 판단
if b=="+":
    print("두수의 합:",a+c)
elif b=="-":
    print("두 수의 차:",a-c)
elif b=="*":
    print("두 수의 곱:",a*c)
elif b=="/":
    print("두 수의 나눈값:",a/c)
elif b=="%":
    print("두 수의 뺀 나머지:",a%c)
elif b=="//":
    print("두 수의 몫:",a//c)
elif b=="**":
    print("두 수의 제곱:",a**c)
else:
    print("연산기호를 제대로 적어주세요")