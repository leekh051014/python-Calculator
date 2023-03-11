operator = input('연산자를 입력해 주세요 : ');
Num01 = int(input('피 연산자1 : '));
Num02 = int(input('피 연산자2 : '));

if operator == "+" and(Num01>10 and Num02>10):
    Re01 = Num01 + Num02;

print(Re01);