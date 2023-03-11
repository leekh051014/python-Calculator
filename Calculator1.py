def calc(v1, op, v2):
    result = 0
    if op == "+":
        result = v1 + v2
    elif op == "-":
        result = v1 - v2
    elif op == "*":
        result = v1 * v2
    elif op == "/":
        if v2 == 0:
            print("0으로 나눌 수 없습니다.")
            quit()
        else:
            result = v1 / v2
    elif op == "**":
        result = v1 ** v2

    return result


res = 0

var1, var2, oper = 0, 0, ""
var1 = int(input("첫 번째 수를 입력하세요 : "))
oper = input("계산을 입력하세요(+,-,*,/,**) : ")
var2 = int(input("두 번째 수를 입력하세요 : "))

res = calc(var1, oper, var2)
print("##계산기 : %d %s %d = %d" % (var1, oper, var2, res))