# El usuario tiene 5 vidas
# Se le pregunta al usuario si quiere seguir jugando luego de perder
# Se le da pistas al usuario de si su número está más arriba o más abajo
from random import randint
print("****** Adivina el Número *******");
def aksForNumber(text):
  while True:
    try:
      return int(input(text))
    except:
      print("La entrada es incorrecta. Esto no contará como un intento")

def askForDiffuculty():
  try:
    difficulty = int(input("Tienes 3 niveles de dificultad: 1- Fácil, 2-Media, 3-Difícil. Escoge: "))
    if (difficulty == 1):
      return 10;
    if (difficulty == 2):
      return 20;
    else:
      return 30
  except:
    return 20

while True:
  maxInt = askForDiffuculty()
  tinkedNumber = randint(1,maxInt)
  lifes = 5
  number = aksForNumber("Estoy pensando un número entre 1 y {}. Adivina cuál es? ".format(maxInt))
  while lifes > 0:
    if (number == tinkedNumber):
      print("Ganaste el juego!!! {} era el número correcto".format(number))
      break
    else:
      lifes -= 1
      if (number < tinkedNumber):
        message = "Piensa más alto: ";
      else:
        message = "Piensa más bajo: ";
      if (lifes != 0):
        number = aksForNumber("Incorrecto. Tienes {} intentos. {}".format(lifes, message))
      else:
        print("Fin del juego. Ya no te quedan intentos. El número correcto era el {}".format(tinkedNumber))
  response = input("Deseas volver a jugar? (s/n): ")
  if (response == "n"):
    print("Gracias por jugar")
    break