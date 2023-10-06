number = int(input("몇 단까지 출력할까요?"))
for x in range(1,number+1):
    print("------- [" + str(x) + "단] -------")
    for y in range(1,number+1):
        print(x, "X", y, "=", x*y)
print("--------------------")