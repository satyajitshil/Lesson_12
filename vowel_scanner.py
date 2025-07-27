
def count_vowels():
    name = input("Type a word:")

    vowels = ['a','e','i','o','u']
    count = 0
    for c in name:
        if c in vowels:
            count += 1

    return count   


def variable_oddity(count):
    print("There are",count,"vowel(s)")
    if count%2 == 0:
        print("The number of vowels in the name is even")
    else:
        print("The number of vowels in the name is odd")

#variable_oddity(count_vowels())
def count_vowels_recursion(name, index):
    # base condition
    if index == len(name):
        return 0
    c = name[index]
    vowels = ['a','e','i','o','u']
    count = 0
    if c in vowels:
        count = 1
    r = count_vowels_recursion(name, index + 1)
    return count + r

name = "satyajit"
print(count_vowels_recursion(name, 0))