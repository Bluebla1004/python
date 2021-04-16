price=7000
age=int(input("나이:"))
if age<8:
    print("무료입장")
elif age<60:
    print("입장료",price)
else:
    print("입장료:",price*0.5)
