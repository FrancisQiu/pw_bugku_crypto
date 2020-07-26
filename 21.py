def aff(num):
    for j in range(0,26):
        if (17*j-8)%26==num:
            print(chr(j+97),end='')
str1=input("The string is:")

for i in str1:
    aff(ord(i)-97)