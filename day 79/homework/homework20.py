operation = input("აირჩიე მოქმედება (+, -, *, /): ")
num1 = float(input("შეიყვანე პირველი რიცხვი: "))
num2 = float(input("შეიყვანე მეორე რიცხვი: "))

if operation == "+":
    print("შედეგი:", num1 + num2)
elif operation == "-":
    print("შედეგი:", num1 - num2)
elif operation == "*":
    print("შედეგი:", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("შედეგი:", num1 / num2)
    else:
        print("ნულზე გაყოფა შეუძლებელია!")
else:
    print("არასწორი ოპერაცია!")