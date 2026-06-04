###
# 04 - Funciones
# Bloques de código reutilizables y parametrizables para hacer tareas especificas
###

""" Definicion de una funcion 

    def nombre_de_la_funcion(parametro1,parametro2, ...):
        docstring
        cuerpo de la funcion
        return valor

"""

print("\nFunciones: ")
# Funcion con parametro
def saludar(nombre):
    print(f"Hola {nombre}!")
saludar("Antonio")

# Funcion con mas de un parametro
def suma(a,b):
    return a+b
print(suma(2,4))

# Parámetros por defecto
def multiplicar(a, b = 2):
    return a * b
print(multiplicar(2))
print(multiplicar(2, 3))

# Argumentos por posición
def describir_persona(nombre: str, edad: int, sexo: str):
  print(f"Soy {nombre}, tengo {edad} años y me identifico como {sexo}")
  
describir_persona("hombre", "madeval", 39)

# Argumentos de longitud de variable (*args):
def sumar_numeros(*args):
    suma = 0
    for num in args:
        suma += num
    return suma
print(sumar_numeros(2,2,2,2,2,2))

# Argumentos de clave-valor variable (**kwargs):
def mostrar_informacion_de(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_informacion_de(nombre="midudev", edad=25, sexo="gato")
