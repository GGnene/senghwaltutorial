#동전 교환 프로그램

money, c500, c100, c50, c10 = 0, 0, 0, 0, 0
print(money)
money = int(input("교환할 돈은 얼마?"))


c500 = money//500
c100 = (money%500)//100
c50 = (money%100)//50
c10 = (money%50)//10
change = money-(c500*500+c100*100+c50*50+c10*10)

print("오백원자리 ==> %d 개" %c500)
print("백원자리 ==> %d 개" %c100)
print("오십원자리 ==> %d 개" %c50)
print("십원자리 ==> %d 개" %c10)
print("잔돈 ==> %d 원 \n " %change)