####################### 3-1 함수 연습문제 #######################

# def yebun(a, b):
#     if a > b:
#         print(f"{a} > {b}")
#     elif a < b:
#         print(f"{a} < {b}")
#     elif a == b:
#         print(f"{a} == {b}")


# yebun(6, 6)



######################## 3-1-1 연습문제 #######################

# def numOfDigits(num):
#     result = len(str(num))
#     print(result)


# numOfDigits(12345)

# numOfDigits(1234567890)

######### 3-1-2 연습문제 #########

# for multiple in range(2, 10):
#     print(f"{multiple}단")
#     for i in range(1, 10):
#         print(f"{multiple} * {i} = {multiple * i}")




###################### 3-2 반환문 연습문제 #######################

# def triangle(b, h):
#     y = 0.5 * b * h
#     return (y)


# result1 = triangle(4, 5)
# result2 = triangle(8, 12)

# print(result1)
# print(result2)


####################### 3-2-1 연습문제 ######################

# def korean_number(n):
#     if n == 1:
#         print("일")
#     elif n == 2:
#         print("이")
#     elif n == 3:
#         print("삼")
#     elif n == 4:
#         print("사")
#     elif n == 5:
#         print("오")
#     elif n == 6:
#         print("육")
#     elif n == 7:
#         print("칠")
#     elif n == 8:
#         print("팔")
#     elif n == 9:
#         print("구")
#     elif n == 10:
#         print("십")


# korean_number(1)
# korean_number(3)



####################### 3-2-2 연습문제 ######################

# def triple(x):
#     result = 3 * x
#     print(result)


# triple(2)
# triple('x')

"""
from datetime import datetime
today = datetime.now()
year = today.year


def korean_age():
    birth = input("태어난 년도를 입력하세요: ")
    return today - birth + 1


korean_age()

"""




####################### 3-2- 연습문제 ######################


# def simple_interest(p, r, t):
#     return p * r * t
#     



# def simple_interest_amount(p, r, t):
#     return p * (1 + r * t)
 

# simple_interest_amount(10000000, 0.03875, 5)

# print(simple_interest_amount)

