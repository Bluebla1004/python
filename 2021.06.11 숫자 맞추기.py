#숫자 맞추기
import random

tries=0
think=0
answer= random.randint(1,100)

print("1부터 100까지 사이의 숫자를 맞추시오")
while think != answer:
    think=int(input("숫자를 입력하시오:"))
    tries+=1
    if think<answer:
        print(think,"보다 높음")
    elif think>answer:
        print(think,"보다 낮음")
if think == answer:
    print("축하합니다. 시도횟수",tries)
else:
    print("정답은",number)
