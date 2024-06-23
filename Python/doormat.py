str1 = "-"
str2 = ".|."

n=int(input())
m= n*3

for i in range(n//2):
    str2formula = (i*2)+1
    count = len(str2*str2formula)
    str1formula = (m- count)//2
    print(str1*str1formula + str2*str2formula + str1*str1formula)

str3 = "WELCOME"
formula = (m - len(str3)) //2
print(str1*formula + str3 + str1*formula)

for i in range(n//2, 0, -1):
    str2formula = (i*2)-1
    count = len(str2*str2formula)
    str1formula = (m- count)//2
    print(str1*str1formula + str2*str2formula + str1*str1formula)