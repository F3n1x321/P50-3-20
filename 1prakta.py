print("Выберите действие:\n1)Сложение(Введите +)\n2)Вычитание(Введите -)\n3)Умножение(Введите *)\n4)Деление(Введите /)\n")
deistv = input()
if (deistv == "+"):
    schet = int(input("Введите колличество чисел:" ))
    x = 0
    while x < schet:
        chislo = int(input())
        if x == 0:
            otvet = chislo +0
        else:
            otvet = otvet + chislo
        x+=1
    print (otvet)
if (deistv == "-"):
    schet = int(input("Введите колличество чисел:" ))
    x = 0
    while x < schet:
        chislo = int(input())
        if x == 0:
            otvet = chislo - 0
        else:
            otvet = otvet-chislo
        x+=1
    print (otvet)
if (deistv == "*"):
    schet = int(input("Введите колличество чисел:" ))
    x = 0
    otvet = 0
    while x < schet:
        chislo = int(input())
        if x == 0:
            otvet = chislo*1
        else:
            otvet = otvet*chislo
        x+=1
    print (otvet)
if (deistv == "/"):
    schet = int(input("Введите колличество чисел:" ))
    x = 0
    while x < schet:
        chislo = int(input())
        if x == 0:
            otvet = chislo/1
            x+=1
        else:
            if chislo == 0:
                print("Нельзя делить на ноль")
            else:
                otvet= otvet/chislo
                x+=1
    print (otvet)    