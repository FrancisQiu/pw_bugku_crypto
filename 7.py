str=input("The string is:")
flag=['','','','','','']
count=0;
for i in str:
    count=count%6
    if count==0:
        flag[1]+=i
    elif count==1:
        flag[0]+=i
    elif count == 2:
        flag[5] += i
    elif count == 3:
        flag[4] += i
    elif count == 4:
        flag[2] += i;
    elif count == 5:
        flag[3] += i;
    count+=1
for i in range(0,6):
    print(flag[i],end='')
