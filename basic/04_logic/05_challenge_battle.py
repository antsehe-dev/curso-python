"""
Tienes dos listas de números, lista_a y lista_b, ambas de la misma longitud. 

Cada número en lista_a se "enfrenta" al número en la misma posición en lista_b.

- Si el número en lista_a es mayor, su valor se suma al siguiente número en lista_a.
- Si el número en lista_b es mayor, su valor se suma al siguiente número en lista_b.
- Si los dos números son iguales, ambos se eliminan y no afectan al siguiente par.

Debes simular estos enfrentamientos y devolver el resultado final:
- Si al final queda un número en lista_a, devuelve ese número seguido de la letra "a" (por ejemplo, "3a").
- Si al final queda un número en lista_b, devuelve ese número seguido de la letra "b" (por ejemplo, "2b").
- En caso de empate, devuelve la letra "x".

lista_a = [2, 4, 2]
lista_b = [3, 3, 4]

resultado = battle(lista_a, lista_b)  # -> "2b"

# Explicación:
# - 2 vs 3: gana 3 (+1)
# - 4 vs 3+1: empate
# - 2 vs 4: gana 4 (+2)
# Resultado: "2b"

lista_a = [4, 4, 4]
lista_b = [2, 8, 2]

resultado = battle(lista_a, lista_b)  # -> "x"

# Explicación:
# - 4 vs 2: gana 4 (+2)
# - 4+2 vs 8: gana 8 (+2)
# - 4 vs 2+2: empate
# Resultado: "x"
"""


def battle (list_a, list_b):
    turn=''
    difference = 0
    for i in range(len(list_a)):            
        num_a = list_a[i]
        num_b = list_b[i]
        
        if turn == 'a':
            num_a=num_a + difference
        elif turn == 'b': 
            num_b=num_b + difference
        
        if num_a > num_b:
            difference = num_a-num_b
            turn = 'a'
        elif num_b > num_a:
            difference = num_b-num_a
            turn = 'b'
        else:
            difference = 0
            turn = ' '
    if difference == 0:
        print("x")
    else:
        print(f"{difference}{turn}")

lista_a = [2, 4, 2]
lista_b = [3, 3, 4]

battle(lista_a,lista_b)