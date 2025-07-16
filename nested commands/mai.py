string=input("Enter your word:")
char=input("Enter your character:")
i=0
count=0

while (i<len(string)):
    if (string[i]==char):
        count= count+1
    i=i+1

print("The character", char, "occurs", count, "times in the word", string)