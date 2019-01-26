#杰裴逊加密器
def paixu(str,num):#旋转处理
    str2=''
    for i in range(len(str)):
        str2+=str[(i+num)%len(str)]
    print(str2)
sum=int(input("the sum is:"))#转轮位数
num=[2,5,1,3,6,4,9,7,8,14,10,13,11,12]#转轮顺序
flag=[]
temp=[]
for i in range(0,sum):
    print("the No. %d String is:"%(i+1))#加密器的每一轮,懒得老输入就自己写个字典呗0w0
    str=input()
    temp.append(str)
for i in num:
    flag.append(temp[i-1])
password=input("The key is:")#密文内容

for i in range(0,sum):
    for k in range(0,26):
        if flag[i][k]==password[i]:
            paixu(flag[i],k)