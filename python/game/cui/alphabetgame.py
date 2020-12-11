import random
import datetime
import string

ALP = list(string.ascii_uppercase)
r = random.choice(ALP)
alp = ""
for i in ALP:
    if i != r:
        alp += i
print(alp)

start_time = datetime.datetime.now()
ans = input("빠진 알파벳은? ").upper()

if ans == r:
    print("정답입니다")
    end_time = datetime.datetime.now()
    print(str((end_time - start_time).seconds) + "초 걸렸습니다")
else:
    print("틀렸습니다")
