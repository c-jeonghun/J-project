def reverse_string(string):
    return string[::-1]

input_string = input("문자를 입력해주세요 : ")
reverse = reverse_string(input_string)

print(f"Original String : {input_string}")
print(f"Rrverse String : {reverse}")