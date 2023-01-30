otvetN = 0
otvetF = 0
otvet  = 0
otvetC = 0
day = 0
x = 0
i = 0
year = int(input('Введите год: '))
while i<10:
        otvetC += i
        otvetN += i
        otvetF += i
        i+=1
i=0
while i < 10:
        day = 1 + i
        i+=1    
        otvetF+= day
        otvetC += day
        otvetN+= day
i = 0
day = 0
while i <10:
    day = 2+i
    i+=1
    otvetC+=day
    otvetN += day
if year % 4 != 0:
    while x<9:
        day= 2 + x
        x+=1
        otvetF+=day
elif year % 100==0:
    if year  % 400==0:
        while x<10:
            day = 2+ x
            x+=1
            otvetF+=day
        day = 0
        x = 0
    else:
        while x<9:
            day= 2 + x
            x+=1
            otvetF+=day
        day = 0
        x = 0
else:
    while x<10:
        day= 2 + x
        x+=1
        otvetF+=day
    day = 0
    x=0
x = 0
i = 0
day = 0
otvetN +=3
while i < 2:
        day = 3 + i
        i+= 1
        otvetC += day
otvetC*=7
otvetN*=4
otvet = otvetC+otvetF+otvetN
print(otvet)