user = str(input("가위 바위 보?"))

import random

com = random.choice(["가위", "바위", "보"])

if com == "가위" :                                                                            # if com == "가위" and user == "바위" 로 작성해도 됨
        if user == "바위" :                                       
             print(f"내가 {user}를 내고 컴퓨터가 {com}를 내서 승리하였습니다.")                        
        elif user == "보" :
            print(f"내가 {user}를 내고 컴퓨터가 {com}를 내서 패배하였습니다.")
        elif user == "가위" :
            print(f"내가 {user}를 내고 컴퓨터가 {com}를 내서 비겼습니다.")
elif com == "바위" :
    if user == "가위" :
        print(f"내가 {user}를 내고 컴퓨터가 {com}를 내서 패배하였습니다.")
    elif user == "보" :
        print(f"내가 {user}를 내고 컴퓨터가 {com}를 내서 승리하였습니다.")
    elif user == "바위" :
        print(f"내가 {user}를 내고 컴퓨터가 {com}를 내서 비겼습니다.")
elif com == "보" :
    if user == "바위" :
        print(f"내가 {user}를 내고 컴퓨터가 {com}를 내서 패배하였습니다.")
    elif user == "가위" :
        print(f"내가 {user}를 내고 컴퓨터가 {com}를 내서 승리하였습니다.")
    elif user == "보" :
        print(f"내가 {user}를 내고 컴퓨터가 {com}를 내서 비겼습니다.")
