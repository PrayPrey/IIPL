## 사칙연산 함수 정의
def plus(a,b):
    return a + b

def minus(a,b)
    return a-b

def mul(a,b):
    return a*b

def divide(a,b):
    return a/b

def custom(a,b):
    return a//b

def custom2(a,b):
    return a%b


def custom3(a,b):
    return a**b


if __name__ == '__main__':

    ## 사용자 입력
    print('\n첫 번째 숫자를 입력하세요.')
    input1 = input('입력 :')


    print('\n원하는 사칙연산 기호 중 하나를 선택하세요. (+, -, *, /, //, %)')
    act = input('기호 : ')

    print('\n두 번째 숫자를 입력하세요.')
    input2 = input('입력 :')


    ## 연산 수행
    if act == "+":
        result = plus(input1, input2)
    elif act == "-":
        result = minus(input1, input2)
    elif act == "*":
        result = mul(input1, input2)
    elif act == '/':
        result = divide(input1, input2)
    elif act == '//':
        result = custom(input1, input2)
    elif act == "%":
        result = custom2(input1, input2)
    elif act == "**":
        result = custom3(input1, input2)


    print(f"사칙연산 결과는 {result}입니다.")
