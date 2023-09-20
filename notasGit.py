#Test Git
import random

nombre = input("escribe tu nombre")
print("Hola",nombre,"Lindo día")

num1 = random.random()
print("Resultado de la función Random: ", round(num1, 4))

num2 = random.randint(4,84)
print("Resultado de la función randint: ", num2)

lista = ["Robert", "Pablo", "Carlos", "Emiliano", "Mathias", "Jesús", "Yael", "Juan Pablo", "JC"]
nombre = random.choice(lista)
print("El elegido es:",nombre)

num3 = random.randrange(4,27,2)
print("El elemento random fue:", num3)
