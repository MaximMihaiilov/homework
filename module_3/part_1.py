#L1
x = float(input("Введите сумму вклада: "))
p = float(input("Введите процент вклада: "))
y = float(input("Введите желаемую сумму : "))
i = 0
while x <= y:
    x = x/100*p+x
    round(x)
    i += 1
print("Понадобится ", i)


#L2
n=int(input("Введите количество раз: "))
i=0
while i<n:
	print("for - частный случай цикла while")
	i+=1


#L3
n = int(input())
c = 0

while n > 0:
    d = n % 10
    c = c + d
    n = n // 10
 
print("Сумма всех цифр:", c)



	