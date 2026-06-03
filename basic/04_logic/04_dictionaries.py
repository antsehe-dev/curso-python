###
# 04 - Dictionaries
# Los diccionarios son colecciones de pares clave-valor.
# Sirven para almacenar datos relacionados.
###

#Diccionario:
persona = {
    "nombre":"Antonio",
    "apellidos":"Serrano Herruzo",
    "edad":20,
    "genero":"Masculino",
    "es_estudiante": True,
    "calificaciones":[8,1,2,5,9,7,8,10],
    "familiares":{
        "padre":"Antonio José Serrano",
        "madre":"Inmaculada Herruzo",
        "hermano":"Miguel Serrano"
    }
}

# Acceder a valores
print(persona["nombre"])
print(persona["calificaciones"][4])
print(persona["familiares"]["padre"])


# cambiar valores al acceder
persona["nombre"] = "madeval"
persona["calificaciones"][2] = 10

# eliminar completamente una propiedad
del persona["edad"]


es_estudiante = persona.pop("es_estudiante") 
print(f"es_estudiante: {es_estudiante}")
print(persona)


# sobreescribir un diccionario con otro diccionario
a = { "name": "miduev", "age": 25 }
b = { "name": "madeval", "es_estudiante": True }

a.update(b)
print(a)

# comprobar si existe una propiedad
print("name" in persona) # False
print("nombre" in persona) # True

# obtener todas las claves
print("\nkeys:")
print(persona.keys())

# obtener todas los valores
print("\nvalues:")
print(persona.values())

# obtener tanto clave como valor
print("\nitems:")
print(persona.items())

# imprimir de manera clave valor
print("\nImprimir de manera clave valor:")
for key, value in persona.items():
  print(f"{key}: {value}")