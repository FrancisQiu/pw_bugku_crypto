str1=input("The string is:")
str2=''
temp=0
ch=[]
for i in str1:
    if(i==' '):
        ch.append(str2)
        str2=''
    else:
        str2+=i
for i in range(len(ch)):
    if ch[i][0]=='d':
        for j in range(len(ch[i])-1):
            temp=temp*10+(ord(ch[i][j+1])-48)
    elif ch[i][0]=='b':
        for j in range(len(ch[i])-1):
            temp=temp*2+(ord(ch[i][j+1])-48)
    elif ch[i][0]=='o':
        for j in range(len(ch[i])-1):
            temp=temp*8+(ord(ch[i][j+1])-48)
    elif ch[i][0]=='x':
        for j in range(len(ch[i])-1):
            if ord(ch[i][j+1])>=97:
                temp=temp*16+(ord(ch[i][j+1])-87)
            else:
                temp=temp*16+(ord(ch[i][j+1])-48)
    ch[i]=chr(temp)
    temp=0
for i in ch:
    print(i,end='')