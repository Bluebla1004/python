a = float (input("국어:"))
b = float (input("영어:"))
c = float (input("수학:"))
d = float (input("과학:"))

e = (a+b+c+d)
f = e/4
if e>=90:
    print("합:",e,"평균:",f)
    print("A학점")
elif e>=80:
    print("합:",e,"평균:",f)
    print("B학점")
elif e>=70:
    print("합:",e,"평균:",f)
    print("C학점")
elif e>=60:
    print("합:",e,"평균:",f)
    print("D학점")
else:
    print("합:",e,"평균:",f)
    print("F학점")

#또는 print("합:",a+b+c+d,"평균:"f,"A학점)