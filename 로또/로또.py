import random

print("로또 번호 생성기")
print("-"*50)
print("몇개 할꺼?")

num = input("게임 수 : ")

print("-"*50)

for i in range(0, int(num)):
    lotto = random.sample(range(1,46),6)
    lotto.sort()
    print(lotto)