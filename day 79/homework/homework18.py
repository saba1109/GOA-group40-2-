 #სახელის ასოების რაოდენობის შედარება
user_name = input("შეიყვანე შენი სახელი: ")
my_name = "გიორგი"

user_name_length = 0
for _ in user_name:
    user_name_length += 1

my_name_length = 0
for _ in my_name:
    my_name_length += 1

if user_name_length == my_name_length:
    print("ჩვენ სახელებში ერთნაირი რაოდენობის ასოებია!")
else:
    print("კარგი სახელია!")