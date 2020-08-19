string  = input()
# Write your code here
l1=list(string)
flag=0
lenth=len(l1)
for i in range(0,lenth-1,2):
    if(l1[i]==")" or l1[i]=="]" or l1[i]=="}" or len(l1)%2):
        flag=0
        break
    elif(l1[i]=="(" or l1[i]=="[" or l1[i]=="{"):
        if(l1[i]=="(" and l1[i+1]==")"):
            flag=1
        elif(l1[i]=="[" and l1[i+1]=="]"):
            flag=1
        elif(l1[i]=="{" and l1[i+1]=="}"):
            flag=1
        else:
            flag=0
if(flag!=0):
    print("Success")
else:
    print(len(l1))