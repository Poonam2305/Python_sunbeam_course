num = int(input("enter the number: "))
print("num")
for i in range(2,num):
     if num%i == 0:
         flag=0
     else:
         flag=1
print("Number is prime") if flag ==1 else print("Number is not prinme")

