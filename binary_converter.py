#num = int(input("Enter a whole decimal number:"))
#"10"
#res = ""
#r = (2%2)
#d = (2//2)
#res = str(r)
#r = (d%2)
#d = (d//2)
#res = str(r) + res
#print(res)

#|getting binary without "while" loop|

num = int(input("Enter a whole decimal number:"))


res = " "

while num > 0:
    r = (num%2)
    res = str(r) + res
    num = (num//2)
print(res)   
    