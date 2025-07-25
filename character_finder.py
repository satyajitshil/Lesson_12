string = input("PLZ TYPE A STRING:")
char = input("PLZ WRITE A CHARACTER:")

i = 0
count = 0

while i < len(string):
    if string[i] == char:
        count = count + 1
    i += 1
print("The string has the character",char, count, "times")