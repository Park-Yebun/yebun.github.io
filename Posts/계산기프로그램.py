# 계산기 프로그램

# 사용할 수 있는 연산자
# + - * /
# 나머지
# 몫

# 계산기는 먼저 두 숫자를 입력받는다
# 그 뒤에 연산자를 입력받는다 > 나누기 연산자를 입력받았다면 계산하지 않고 메세지를 출력
# 결과를 출력

# 나눗셈은 0으로 나누기 불가능

# 한번 계산이 끝나도 계속 계산할 수 있게 반복문 이용

# 두 숫자 모두 0을 입력하면 종료

from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText('calcaulator'))

while True :
    a = int(input())
    b = int(input())


    cal = input("연산자: ")

    if b == 0 and cal == "/" :
        print("계산할 수 없습니다")
    elif cal == "+" :
        print("결과: ", a + b)
    elif cal == "-" :
        print("결과: ", a - b)
    elif cal == "*" :
        print("결과: ", a * b)
    elif cal == "/" :
        if b == 0 :
            print("계산할 수 없습니다")
        else :
            print("결과: ", a / b)
    elif cal == "%" :
        print("결과: ", a % b)
    elif cal == "//" :
        print("결과: ", a // b)     
    elif a == b and a == 0 :
        print("종료")
        break

