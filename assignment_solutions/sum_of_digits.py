input_val=int(input("enter the integer: "))

print(input_val)

sum = 0

while input_val>0:
    digit=input_val%10
    sum +=digit
    input_val=int(input_val/10)
    print(input_val)

print("the sum of digits is : ",sum)


