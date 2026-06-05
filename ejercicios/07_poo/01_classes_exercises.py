"""
EJERCICIOS: Programación Orientada a Objetos
Nivel: Intermedio
"""

# --- PARTE 1: Clases básicas ---

# Ejercicio 1: Clase Libro
# Crea una clase Libro con atributos: titulo, autor, anio, prestado=False.
# Métodos: prestar() (cambia prestado a True si está disponible),
# devolver() (cambia prestado a False), y __str__() que muestre la info del libro.
class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.prestado = False
    def prestar(self):
        if not self.prestado:
            self.prestado = True
            return True
        return False
    def devolver(self):
        self.prestado = False
    def __str__(self):
        estado = "prestado" if self.prestado else "disponible"
        return f"{self.titulo} ({self.anio}) - {self.autor} [{estado}]"
lib = Libro("1984", "Orwell", 1949)
print(lib)
lib.prestar()
print(lib)

# Ejercicio 2: Clase Banco
# Crea una clase CuentaBancaria con:
# - Atributo privado __saldo
# - Método depositar(cantidad) que aumente el saldo
# - Método retirar(cantidad) que disminuya el saldo si hay suficiente
# - Método obtener_saldo() getter
# - Método transferir(destino, cantidad) que transfiera entre cuentas
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo
    def depositar(self, cantidad):
        self.__saldo += cantidad
    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return True
        return False
    def obtener_saldo(self):
        return self.__saldo
    def transferir(self, destino, cantidad):
        if self.retirar(cantidad):
            destino.depositar(cantidad)
            return True
        return False
c1 = CuentaBancaria("Ana", 1000)
c2 = CuentaBancaria("Luis", 500)
c1.transferir(c2, 200)
print(f"{c1.titular}: {c1.obtener_saldo()}€")
print(f"{c2.titular}: {c2.obtener_saldo()}€")

# --- PARTE 2: Herencia ---

# Ejercicio 3: Herencia Vehículos
# Crea una clase base Vehiculo con atributos: marca, modelo, year.
# Método: info() que muestre los datos.
# Crea clases derivadas:
# - Coche(Vehiculo): añade num_puertas, sobreescribe info()
# - Moto(Vehiculo): añade tipo (deportiva, cruiser, etc.), sobreescribe info()
# - Camion(Vehiculo): añade capacidad_carga, sobreescribe info()
# Tu código aquí:

# --- PARTE 3: Polimorfismo ---

# Ejercicio 4: Polimorfismo Animales
# Crea una clase Animal con método hacer_sonido() que lance NotImplementedError.
# Crea clases Perro, Gato, Vaca que hereden de Animal e implementen hacer_sonido().
# Crea una función hacer_sonidos(lista_animales) que recorra la lista y llame a hacer_sonido().
# Tu código aquí:

# --- PARTE 4: Métodos estáticos y de clase ---

# Ejercicio 5: Static y class methods
# Crea una clase Calculadora con:
# - @staticmethod sumar(a, b)
# - @staticmethod multiplicar(a, b)
# - @classmethod desde_string(cls, expresion) que reciba "2+3" y devuelva el resultado
# Tu código aquí:

# --- PARTE 5: Sistema completo ---

# Ejercicio 6: Sistema de Biblioteca
# Combina todo lo anterior:
# - Clase Biblioteca con lista de libros
# - Método agregar_libro(libro)
# - Método buscar_por_titulo(titulo)
# - Método listar_disponibles()
# - Método listar_prestados()
# Tu código aquí:
