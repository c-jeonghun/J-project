def list_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def main():
    numbers = []
    print("숫자를 입력하세요. 종료하시려면 'done'을 입력하세요.")

    while True:
        user_input = input("숫자 : ")

        if user_input.lower() == 'done':
            break

        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("유효한 숫자를 입력하세요.")

    if len(numbers) == 0:
        print("입력된 숫자가 없습니다.")
    else:
        average = list_average(numbers)
        print(f"입력된 숫자들의 평균 : {average}")

if  __name__ == "__main__":
    main()