# Realiza, utilizando Python 3, el ejercicio 3 de la página 35 del libro “Introducción a
# Python” de Jon Vadillo e inclúyelo en un fichero llamado lista.py. Las funciones que
# debes usar en el ejercicio 3 deben utilizar OBLIGATORIAMENTE las siguientes
# cabeceras:
# def estaEnRango(valor, minimo, maximo)
# # Devuelve True o False determinando que valor se encuentra entre el mínimo y el
# máximo.
# def estaEnLista(valor, lista)
# # Devuelve True o False determinando si el valor está en la lista.
# Guarda este código en un archivo llamado lista.py

def estaEnRango(valor, minimo, maximo):
    return minimo <= valor <= maximo

def estaEnLista(valor, lista):
    return valor in lista

def main():
    try:
        numero_usuario = int(input("Introduce un número del 1 al 20: "))

        if estaEnRango(numero_usuario, 1, 20):
            lista_numeros = [6, 14, 11, 3, 2, 1, 15, 19]

            if estaEnLista(numero_usuario, lista_numeros):
                print(f"El número {numero_usuario} está en la lista.")
            else:
                print(f"El número {numero_usuario} no está en la lista.")
        else:
            print("El número introducido no está en el rango especificado.")
    
    except ValueError:
        print("Error: Introduce un número válido.")

main()
