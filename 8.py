str=input("The string is:")
flag=''
for i in range(0,26):
    for item in str:
        num1=ord(item)
        num2 = ord(item)+int(i)
        if num1<65 or (num1>=90 and num1<=96) or num1>122:
            print(chr(num1),end='')
        elif (num2>90 and num1<=90 and num1>=65) or (num2>122 and num1<=122 and num1):
            num2-=26
            print(chr(num2),end='')
        else:
            print(chr(num2),end='')
    print()