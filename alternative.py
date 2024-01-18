# ------------- 1st Task - Alternate Each Character --------------
print("-" * 103)
print("\t\t\t\t\tSTRING HANDLING\n")
print("1st Task - Alternate Each Character")

sentence = "my name is daryll fernandez and i want to become a software engineer"
final = ""          # this is empty string variable to store each letter

for i in range(len(sentence)):  # for loop, to go through each index of the string
    if i % 2 == 0:  # true in index 0,2,4,6,8 and so on, then makes letter in upper case
        final = final + sentence[i].upper()
    else:           # true in index 1,3,5,7,9 and so on, then makes letter in lower case
        final = final + sentence[i].lower()
print("ORIGINAL SENTENCE : \"my name is daryll fernandez and i want to become a software engineer\"" )
print(f"ALTERNATE RESULT  :  {final}")   # var "final" holds each letter 
print()

# -------------- 2nd Task - Alternate Each Word ------------------
print("2nd Task - Alternate Each Word")

sentence_2 = "i can achieve it by learning new coding tricks every single day and keep rocking"
sentence_2 = sentence_2.split(" ") # .split function is used to separate each word in to a list
final_2 = []                       # this is empty list variable to store each word

for j in range(len(sentence_2)):   # for loop, to go through each index of the list
    if j % 2 == 0:                 # true in index 0,2,4,6,8 and so on, then makes letter in upper case
        final_2.append(sentence_2[j].upper()) # append method is used to add each index value into the list variable "final_2"
    else:                          # true in index 1,3,5,7,9 and so on, then makes letter in lower case
        final_2.append(sentence_2[j].lower())
print("ORIGINAL SENTENCE : \"i can achieve it by learning new coding tricks every single day and keep rocking\"" )
print(f"ALTERNATE RESULT  :  {" ".join(final_2)}")       # .join method is used to combine all list value and make as a sentence
print("-" * 103)


