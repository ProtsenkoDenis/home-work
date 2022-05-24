def homework1():
    print("Hello World")
def homework2():
    fullname = input("Enter yuor name and surname")
    age = input("Enter yuor age")
    gender = input("Enter yuor gender")
    print("Hello, my name is" + fullname + ". " "I`m"" " + age + " yers old, and I`m" + gender + ".")
def homework3():
    a = input("Enter any number from 1 to 15")
    b = input("Enter any number from 1 to 20")
    c = input("Enter any number from 1 to 25")
    if a > b:
        print("сумне повідомлення")
    elif b > a:
        if b > c:
            print("безмежно радісне")
        else:
            print("не дуже сумне повідомлення")
    elif a == b:
        print("щось про рівенство")
def homework4():
    a = int(input("будь-яке число а"))
    b = int(input("будь-яке число б"))
    c = int(input("будь-яке число с"))
    історія = ""
    while a < b:
        print("погана новина")
        a = a + c
        історія = історія + " " + str(a)
    else:
        print("хороша новина")
        print("інкримент історії =" + історія)
homework1()
homework2()
homework3()
homework4()









