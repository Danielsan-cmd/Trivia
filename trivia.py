
nombre_usuario = input('Ingrese su nombre por favor: ')
print(f"SBienvenido {nombre_usuario} a esta trivia. Estas listo?")
contador = 0
def cuestionario():
    respuesta1= input("Quien hizo el papel de Jack (Titanic)?: ").lower()
    respuesta2= int(input("Cuantas patas tiene una aranha?: ").lower())
    respuesta3= int(input("Cuanto es 2 + 2? : ").lower())
    respuesta4= input("Cual es el pokemon legendario que lleva el numero uno?:  ").lower()
    contador = 0
    if respuesta1 == "Leo Dicaprio":
        contador +=1
    else:
        contador -=1
    if respuesta2 == 8:
        contador += 1
    else:
        contador -=1
    if respuesta3 == 4:
        contador += 1
    else:
        contador -=1
    if respuesta4 == "articuno":
        contador += 1
    else:
        contador -=1
    
cuestionario()
print(f"Eres {nombre_usuario} y lograste hacer {contador} puntos")



