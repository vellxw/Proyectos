import random                                          # El programa importa random para generar la aleatoriedad necesaria

def resultado():                                       # Crea función
    intrigante = input("Escriba TIRAR para proceder:") # Imprime un mensaje para proceder a darle al usuario la posibilidad de elegir con input
    a, b = random.choice([1, 2, 3, 4, 5, 6]), random.choice([1, 2, 3, 4, 5, 6]) # se les otorga valor aleatorio del 1 al 6 a las variables "a" y "b"
    if intrigante == "TIRAR" or intrigante == "tirar": # Si la variable intrigante es igual a TIRAR o tirar
        print("=====================")                 # Imprime adorno visual
        print("El dado nº1 ha dado:", a)               # Imprime el resultado del primer dado
        print("El dado nº2 ha dado:", b)               # imprime el resultado del segundo dado
        print("=====================")                 # Imprime adorno visual
        print("La suma de los dados es:", a + b)       # y por último suma los dados y otorga el resultado de esta.
    else:                                              # Sino
        print("El valor indicado no es TIRAR, ingrese un valor correcto. Puede indicarlo tambien en minusculas")

resultado()                                            # Llama a la función "resultado"

while True:                                            # Crea bucle while
    intrigante2 = input("¿Querés tirar nuevamente? (Y/N):") # Imprime mensaje input para darle valor a la variable "intrigante2"
    if intrigante2 == "N" or intrigante2 == "n" or intrigante2 == "no": # Si "intrigante2" es igual a "N" o "n" o "no"
        break                                          # para el ciclo
    elif intrigante2 == "Y" or intrigante2 == "y" or intrigante2 == "s" or intrigante2 == "S": # Si "intrigante2" es igual a las distintas formas de poner si                       
        resultado()                                    # Llama a la función "resultado"
    else:                                              # Sino
        print("El valor indicado no es Y ni tampoco N, ni S. Ingrese un valor correcto. No olvide indicarlo en mayusculas")