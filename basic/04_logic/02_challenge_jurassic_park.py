"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""

def count_carnivore_dinasour_eggs (egg_list):
    total_carnivore_eggs = 0
    
    for eggs in egg_list:
        if eggs % 2 == 0:
            total_carnivore_eggs += eggs
    return total_carnivore_eggs

egg_list=[3,4,7,8,10,22,2]

print(count_carnivore_dinasour_eggs(egg_list=egg_list))
