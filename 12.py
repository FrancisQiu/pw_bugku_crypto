#奇怪的密码
str=input("The string is:")
flag=''
num=1;
for i in str:
    i=ord(i)-num
    flag+=chr(i)
    num+=1
print(flag)#flag₧lei_ci_jiami,₧这个符号改成'{'，尾部再加个'}'