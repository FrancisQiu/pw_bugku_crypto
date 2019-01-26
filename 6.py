import base64
str=input("The string is:")
str2=''
for item in str:
    num1=ord(item)-4
    str2+=chr(num1)
print(base64.b64decode(str2))