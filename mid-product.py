num = int(input())
t =num
num_len = 0

while t > 0:
    num_len = num_len + 1
    t = int(t/10)

if num_len >= 4:
    num_len = int(num_len/2)
    chk = 0
    while num > 0:
        rem = num%10
        if chk == num_len:
            midone = rem
        elif chk == num_len - 1:
            midtwo = rem
        num = int(num/10)
        chk += 1
    prod = midone * midtwo
    print(prod)
else:
    print("Type a 4 or more digit number.")    
