###
# 01 - Clases
# Introducción a la Programación Orientada a Objetos (POO) en Python
###

# 1. Definir una clase
class Persona:
    # Constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    # Método de la clase
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

# 2. Crear una instancia de la clase
persona1 = Persona("Juan", 30)
# 3. Acceder a los atributos y métodos de la instancia
print(persona1.nombre)  # Juan

# 4. Llamar al método de la clase
print(persona1.saludar())  # Hola, mi nombre es Juan y tengo 30 años.

# 5. Herencia: Crear una clase que herede de otra
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llamar al constructor de la clase padre
        self.carrera = carrera

    def estudiar(self):
        return f"{self.nombre} está estudiando {self.carrera}."
    

estudiante1 = Estudiante("Ana", 22, "Ingeniería")
print(estudiante1.saludar())  # Hola, mi nombre es Ana y tengo 22 años.

#5. Polimorfismo: Sobrescribir un método de la clase padre
class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def saludar(self):
        return f"Hola, soy el profesor {self.nombre} y enseño {self.materia}."

profesor1 = Profesor("Carlos", 45, "Matemáticas")
print(profesor1.saludar())  # Hola, soy el profesor Carlos y enseño Matemáticas.

# 6. Encapsulamiento: Atributos privados
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado se indica con __
    def depositar(self, cantidad):
        self.__saldo += cantidad

        
# 7. Métodos para acceder a atributos privados
    def obtener_saldo(self):
        return self.__saldo
cuenta1 = CuentaBancaria("Laura", 1000)
cuenta1.depositar(500)
print(cuenta1.obtener_saldo())  # 1500

# 8. Métodos estáticos y de clase
class Matematica:
    @staticmethod
    def sumar(a, b):
        return a + b

    @classmethod # El método de clase recibe la clase como primer argumento, se suele nombrar cls por convención
    def multiplicar(cls, a, b):
        return a * b

print(Matematica.sumar(5, 3))  # 8
print(Matematica.multiplicar(5, 3))  # 15
