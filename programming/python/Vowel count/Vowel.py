
#Jay William Camp Jr.
#4/28/25

#gets the users input of a string
useImp=input("Enter a String: ").lower()
#makes vowels a thing in the eyes of the code
vowels = ["a","e","i","o","u"]
#variables to store how many time each vowel is counted
a = 0
e = 0
i = 0
o = 0
u = 0
#total vowels
vowelCount=0

#check how many vowels in total there are
#loops through use imp
for l in useImp:
    #compares use imp to vowels
    for j in vowels:
        if l == j:
            vowelCount+=1
            break
#prints the number of vowels
#if you have vowels at all tells how many
if vowelCount>0:
    vowel_num=str(vowelCount)
    print("You have " + vowel_num +" vowels")
else:
     print("No vowels ")
     # everytime one appears it increases each variable by one
for letter in useImp:
    if letter =='a':
        a+=1
    elif letter =='e':
        e+=1
    elif letter == 'i':
        i+= 1
    elif letter == 'o':
        o += 1
    elif letter == 'u':
        u += 1
#prints every value for some reason with quotation marks around the number idk thats just what the example wanted
print(f'a = "{a}"')
print(f'e= "{e}"')
print(f'i = "{i}"')
print(f'o = "{o}"')
print(f'u = "{u}"')

