import random

# 이 리스트에는 랜덤한 응답이 포함되어 있습니다. (여러분은 자신만의 언어를 추가하거나 자신만의 언어로 번역할 수도 있습니다.)
random_responses = ["꽤 흥미롭네요, 자세히 알려주세요.",
                    "알겠어요. 계속하세요.",
                    "왜 그렇게 말하시나요?",
                    "요즘 날씨가 참 재미있네요, 안 그래요?",
                    "우리 주제를 바꿔 봅시다.",
                    "어젯밤 경기 보셨어요?"]

print("안녕하세요, 저는 간단한 로봇 마빈입니다.")
print("'종료'를 입력하면 언제든지 이 대화를 끝낼 수 있습니다.")
print("대답을 입력한 후에 '엔터'를 누르세요.")
print("오늘 기분 어떠세요?")

while True:
    # 유저가 텍스트를 입력할 때까지 대기
    user_input = input("> ")
    if user_input == "종료":
        # "종료"를 입력하면, 무한 루프 탈출
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("만나서 반가웠어요, 안녕히 계세요!")