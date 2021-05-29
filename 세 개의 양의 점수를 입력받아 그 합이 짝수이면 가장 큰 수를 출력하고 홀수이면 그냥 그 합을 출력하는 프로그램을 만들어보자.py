print("세개의 양의 점수를 입력하십시오")
a=int(input())
b=int(input())
c=int(input())



sum= a+b+c
if sum%2==0:
    if a>b:
        Max=a
        if a>c:
            Max=a
            print("세수의 합은",sum,"짝수이고, 가장큰수는",Max,"이다.")
        else:
            Max=c
            print("세수의 합은",sum,"짝수이고, 가장큰수는",Max,"이다.")
    else:
        Max=b
        if b>c:
            Max=b
            print("세수의 합은",sum,"짝수이고, 가장큰수는",Max,"이다.")
        else:
            Max=c
            print("세수의 합은",sum,"짝수이고, 가장큰수는",Max,"이다.")
else:
    print("세수의 합은 홀수이고, 그합은",sum,"이다.")
