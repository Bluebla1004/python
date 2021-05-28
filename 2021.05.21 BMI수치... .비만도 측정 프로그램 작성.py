#BMI = 몸무게 / (키*키)
#BMI지수 20 미만이면 저체중
#BMI지수 20 이상24이하면 정상
#BMI지수 25 이상30이하면 경도비만
#BMI지수 31 이상이면 비만
#입력 예시) 176cm 86kg

kg = float(input("몸무게:"))
cm = float(input("키:"))
bmi = (cm*cm)/kg

if bmi<20:
    print ("저체중")
elif 20 <= bmi <= 24:
    print("정상체중")
elif 25 <= bmi <= 30:
    print("경도비만")
else:
    print("비만")
