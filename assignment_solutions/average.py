count = 0
english_marks =int(input("enter the mark of english: "))
print(english_marks)
count+= 1
marathi_marks = int(input("enter the mark of marathi: "))
print(marathi_marks)
count+= 1
hindi_marks = int(input("enter the mark of hindi: "))
print(hindi_marks)
count+= 1
history_marks = int(input("enter the mark of history: "))
print(history_marks)
count+= 1
kannad_marks = int(input("enter the mark of kannad: "))
print(kannad_marks)
count+= 1
sum_of_marks= (english_marks+marathi_marks+hindi_marks+history_marks+kannad_marks)
print("the sum is: ",sum_of_marks)
calculate_avg = sum_of_marks/count
print("the average of marks is: ",calculate_avg)
