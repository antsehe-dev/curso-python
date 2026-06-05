"""
EJERCICIOS: Métodos de listas
Nivel: Básico
"""

# Ejercicio 1: append y extend
# Crea una lista vacía. Añade los números del 1 al 5 con append().
# Luego usa extend() para añadir [6, 7, 8, 9, 10].
nums = []
for i in range(1, 6):
    nums.append(i)
print("After append:", nums)
nums.extend([6, 7, 8, 9, 10])
print("After extend:", nums)

# Ejercicio 2: insert y remove
# Dada la lista letras = ["a", "c", "d", "e", "b", "c"]
# Inserta "z" en la posición 0. Luego elimina la primera ocurrencia de "c".
letras = ["a", "c", "d", "e", "b", "c"]
letras.insert(0, "z")
print("After insert:", letras)
letras.remove("c")
print("After remove:", letras)

# Ejercicio 3: pop y del
# Dada la lista nums = [10, 20, 30, 40, 50]
# Usa pop() para eliminar y obtener el último elemento.
# Usa del para eliminar el elemento en el índice 1.
# Usa pop(0) para eliminar y obtener el primer elemento.
nums = [10, 20, 30, 40, 50]
print("pop:", nums.pop())
print("After pop:", nums)
del nums[1]
print("After del:", nums)
print("pop(0):", nums.pop(0))
print("After pop(0):", nums)

# Ejercicio 4: sort y sorted
# Dada la lista palabras = ["manzana", "pera", "MELÓN", "plátano", "KIWI"]
# Ordena alfabéticamente (sin distinguir mayúsculas) usando sort con key=str.lower.
# Luego usa sorted() para crear una nueva lista ordenada de forma descendente.
palabras = ["manzana", "pera", "MELÓN", "plátano", "KIWI"]
palabras.sort(key=str.lower)
print("Sorted in-place:", palabras)
desc = sorted(palabras, key=str.lower, reverse=True)
print("Descending:", desc)

# Ejercicio 5: count e in
# Dada la lista datos = [1, 2, 3, 2, 4, 2, 5, 2]
# Cuenta cuántas veces aparece el 2. Verifica si el 6 está en la lista.
datos = [1, 2, 3, 2, 4, 2, 5, 2]
print(f"El 2 aparece {datos.count(2)} veces")
print(f"El 6 {'está' if 6 in datos else 'no está'} en la lista")

# Ejercicio 6: Limpiar lista
# Dada una lista con 10 elementos, usa clear() para vaciarla.
# Muestra la lista antes y después.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Antes: {lista}")
lista.clear()
print(f"Después: {lista}")

# Ejercicio 7: Gestión de tareas
# Crea una lista vacía tareas. Implementa un menú interactivo que permita:
# 1. Añadir tarea (append)
# 2. Eliminar tarea por nombre (remove)
# 3. Mostrar todas las tareas
# 4. Salir
# (Usa un bucle while y if/elif/else)
tareas = []
while True:
    print("\n--- Gestión de Tareas ---")
    print("1. Añadir tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas")
    print("4. Salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        tarea = input("Introduce la tarea: ")
        tareas.append(tarea)
        print(f"Tarea '{tarea}' añadida")
    elif opcion == "2":
        tarea = input("Introduce la tarea a eliminar: ")
        if tarea in tareas:
            tareas.remove(tarea)
            print(f"Tarea '{tarea}' eliminada")
        else:
            print(f"La tarea '{tarea}' no existe")
    elif opcion == "3":
        if tareas:
            print("Tareas:")
            for i, t in enumerate(tareas, 1):
                print(f"{i}. {t}")
        else:
            print("No hay tareas")
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida")
