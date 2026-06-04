###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición
###

contador = 0
while contador <=5:
    print(contador)
    contador +=1

contador = 0

# BREAK
while True:
    print(contador)
    contador +=1
    if contador == 5:
        break
    

# CONTINUE
contador = 0
while contador < 10:
    contador +=1
    if contador == 5:
        continue
    
    print(contador)

# ELSE
contador = 0
while contador < 5:
  print(contador)
  contador += 1
else:
  print("El bucle ha terminado")