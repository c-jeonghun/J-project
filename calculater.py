# 계산기

def calculate(expression):
    operators = ['+', '-', '*', '/']

    for operator in operators:
        if operator in expression:
            x, y = expression.split(operator)
            x = float(x.strip())
            y = float(y.strip())

            if operator == '+':
                return x + y
            elif operator == '-':
                return x - y
            elif operator == '*':
                return x * y
            elif operator == '/':
                if y == 0:
                    raise ValueError("0으로 나눌 수 없습니다.")
                return x / y
            
    raise ValueError("지원하지 않는 형식입니다.")

user_input = input("계산식을 입력하세요 (예. 1+1) : ")

try:
    total = calculate(user_input)
    print(f"결과 : {total}")
except Exception as e:
    print(f"오류발생 : {e}")