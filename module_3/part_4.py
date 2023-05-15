import json

password=input("Введите пароль для регистрации: ")
login=input("Введите логин для регистрации: ")

data=[login, password]

def register(login, password):
    with open("2.json", "w") as f:
        json.dump(data, f)

register(login,password)