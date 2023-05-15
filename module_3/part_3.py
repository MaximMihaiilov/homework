a=float(input("сторона a: "))
b=float(input("сторона b: "))
c=float(input("сторона c: "))


def area(a, b, c):
    p = (a + b + c) / 2
    s=(p * (p - a) * (p - b) * (p - c)) ** 0.5
    return s

   
print("Площадь равна:", area(a,b,c))





    