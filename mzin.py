#Take
num = int(input("Enter the number:"))

#Sum.
sum = 0

#find
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit **3
    temp //= 10

#display
if num == sum :
    print(num,"Is a armstrong number")
else:
     print(num,"Is not a armstrong number")