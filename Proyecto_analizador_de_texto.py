print("\U0001f525          Bienvenido al analizador de texto 3000          \U0001f525")
print("--------------------------------------------------------------")
texto_ingresado = input("Ingresa un texto: ")
texto_ingresado_minusculas = texto_ingresado.lower()
print("--------------------------------------------------------------")
##Parte 1 - recibir 3 letras del usuario y buscar su frecuencia en el texto ingresado
print("Ahora ingresa 3 letras para analizar su frecuencia en el texto.")
letra_1 = input("Letra 1: ")
letra_2 = input("Letra 2: ")
letra_3 = input("Letra 3: ")

letra_1_minusculas = letra_1.lower()
letra_2_minusculas = letra_2.lower()
letra_3_minusculas = letra_3.lower()

#lista_de_letras = [letra_1_minusculas, letra_2_minusculas, letra_3_minusculas] #Esta parte la veo inecesaria

letra_1_contador = texto_ingresado_minusculas.count(letra_1_minusculas)
letra_2_contador = texto_ingresado_minusculas.count(letra_2_minusculas)
letra_3_contador = texto_ingresado_minusculas.count(letra_3_minusculas)

print(f"La letra 1 ({letra_1}) aparece {letra_1_contador} veces")
print(f"La letra 2 ({letra_2}) aparece {letra_2_contador} veces")
print(f"La letra 3 ({letra_3}) aparece {letra_3_contador} veces")
print("--------------------------------------------------------------")

##Parte 2 - decirle al usuario cuantas palabras tiene su texto
texto_separado = texto_ingresado_minusculas.split()
print(f"\nEl texto ingresado contiene {len(texto_separado)} palabras.\n")

print("--------------------------------------------------------------")
##Parte 3 - imprimir la pirmera y ultima letra del texto ingresado
primera_letra = texto_ingresado[0]
ultima_letra = len(texto_ingresado) - 1

print(f"\nLa primer letra del texto es: {primera_letra}")
print(f"La ultima letra del texto es: {texto_ingresado[ultima_letra]}")
print("\n--------------------------------------------------------------")

##Parte 4 - Invertir el orden de las palabras
texto_ingresado_invertido = texto_ingresado.split()
texto_ingresado_invertido.reverse()
print(f"\nEl texto ingresado invertido quedaria asi: \n{" ".join(texto_ingresado_invertido)}")
print("\n--------------------------------------------------------------")

##Parte 5 - Analisar si la palabra Python se encuentra en el texto ingresado
print("\nAnalizando si la palabra Python se encuentra en el texto ingresado...")
analizando_texto = "python" in texto_ingresado_minusculas ##El resultado sera un booleano
texto_analizado = {True: "La palabra Python si se encuentra en el texto ingresado.",
                   False: "La palabra Python no se encuentra en el texto ingresado."}
print(texto_analizado[analizando_texto])
print("\n--------------------------------------------------------------\n")
print("Elaborado por: Anton Mtz \U0001f60e")
