n = int(input().strip())
binary=bin(n)
binary+="0"
lst=[]
ctr=0
for i in binary[2:]:
    if i=="1":
        ctr+=1
    if i=="0":
        lst.append(ctr)
        ctr=0
print(max(lst))
