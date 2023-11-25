# Realiza, utilizando Python 3, un programa llamado binario.py que pida al usuario que
# introduzca un número binario e imprima por pantalla el número en formato decimal.
# Para desarrollar el programa, es necesario que desarrolles una función con la
# siguiente cabecera:
# def esBinario(strbinario)
# # Devuelve True o False si la cadena de caracteres (strbinario) que se ha pasado
# como parámetro contiene una cadena binaria.
# # Ejemplo de esBinario:
# print(esBinario(“1001”))
# True
# print(esBinario(“Hola”))
# False

def esBinario(strbinario):
    for caracter in strbinario:
        if caracter != '0' and caracter != '1':
            return False
    return strbinario != ""

def binarioADecimal(strbinario):
    if esBinario(strbinario):
        decimal = int(strbinario, 2)
        return decimal
    else:
        return None

def main():
    numero_binario = input("Introduce un número binario: ")

    resultado = binarioADecimal(numero_binario)

    if resultado is not None:
        print(f"El número decimal correspondiente es: {resultado}")
    else:
        print("Por favor, introduce un número binario válido.")

main()