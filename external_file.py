num = input("Enter a binary number: ")

int_result = 0

reversed_str = ""
for i in range(len(num)-1, -1, -1):
    reversed_str += num[i]

for i in range(len(reversed_str)):
    int_char = int(reversed_str[i])
    temp_val = pow(2, i) * int_char
    int_result += temp_val
print(int_result)