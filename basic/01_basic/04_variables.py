###
#04 - Variables
###

# Tipado dinamico: el tipo de dato se determina en tiempo de ejecución
my_variable = "Hola"
print(type(my_variable)) #str
my_variable = 123
print(type(my_variable)) #int

# Tipado fuerte: no se pueden realizar operaciones entre tipos de datos incompatibles
#print (10 + "20") #TypeError
print (10 + int("20")) #30

# No recomendada forma de asignar variables
name, age, city = "Antonio", 30, "Madrid"

# Convenviones de nombres de variables
snake_case = "Variable en snake_case"

MI_CONSTANTE = 3.14 #UPPERCASE para constante (aunque en Python no existen constantes verdaderas)

# 12421_variable = "ko"

mark_final: float = 4 # Anotación de tipos: se puede indicar el tipo de dato que se espera, pero no es obligatorio

print (type(mark_final)) # <class 'int'>

