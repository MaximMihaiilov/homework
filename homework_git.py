#Модуль 1 Часть 1
#1
value = (5 + 7*5/8) / 3**5
print("Значение выражения:", value) 

#2
v = int (input())
t = int (input())
print((v * t) % 109) 

#3
a = float(input())
b = float(input())
max1 = (a>b)*a + (b>=a)*b
print("Наибольшее число:", max1)

#Модуль 1 Часть 2
#1
a = int(input("Число1:"))
b = int(input("Число2:"))
c = int(input("Число3:"))
if (a==b) & (b==c):
	print("3")
elif (a==b) or (b==c) or (a==c):
	print("2")
else:
	print("0")

#2
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
if (x1==x2) or (y1==y2):
	print("YES")
else:
	print("NO")

#3 
password = str(input("Придумайте пароль:"))
while len(password) <9:
	print("Пароль должен состоять более чем из 8 символов")
	password = str(input("Придумайте пароль еще раз:"))
else: 
	print("Пароль успешно создан") 
