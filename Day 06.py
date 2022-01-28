n=int(input())
lst=[]
for i in range(n):
    str=input()
    lst.append(str)

for i in lst:
    str1=""
    str2=""
    for j in range(len(i)):
        if j%2==0:
            str1+=i[j]
        else:
            str2+=i[j]
    print(str1,str2)
