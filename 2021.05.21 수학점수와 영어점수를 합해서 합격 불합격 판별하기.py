#영어점수와 수학점수를 합해서 110점 넘으면 합벽이라고 합니다
#각 과목의 점수가 40점 미만이면 110점이 넘어도 불합격입니다.
while True:
    eng = float(input("영어점수:"))
    math = float(input("수학점수:"))
    hap = eng+math

    if hap<110:
        print("불합격:총점이 부족합니다.")
    elif eng>=40:
        if math>=40:
            print("합격")
        else:
            print("불합격:수학점수 미달")
    else:
        print("불합격:영어점수 미달")
