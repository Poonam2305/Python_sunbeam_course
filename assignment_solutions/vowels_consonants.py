input_string = input("enter the string: ")
print("the entered string is:",input_string)
vowels = "aeiouAEIOU"

def number_of_vowels(input_string):
     count =0
     for ch in input_string:
         if ch in vowels:
             count+=1
     return count

def number_of_consonants(input_string):
    count =0
    for ch in input_string:
        if ch not in vowels:
            count+=1
    return count

def ratio_of_vowels_consonants(input_string):
    vowels=number_of_vowels(input_string)
    consonants=number_of_consonants(input_string)
    return vowels / consonants

print(f"the number of vowels in {input_string} is:",{number_of_vowels(input_string)})

print(f"the number of consonants in {input_string} is:",{number_of_consonants(input_string)})
print(f"the ratio in {input_string} is:",{ratio_of_vowels_consonants(input_string)})






