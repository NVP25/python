from errno import EDEADLK


conjunto = {1, 5, 9}

# conjunto = set(lista)
# print (type(conjunto))

# conjunto.remove(9)

# for elem in conjunto: 
#     print (elem)

# print (5 in conjunto)

# print (conjunto)

# conjunto2 = {1, 5, 10}

# print (conjunto.intersection(conjunto2))



d = {
    "nombre": ["Hola Mundo", 19],
    "edad": {
        "edad de papa": 20, 
        "nombre2": "alonso"
    }
}
print ( d["nombre"][1] )

# d["apellido"] = "Perez"
# del d["edad"]
# d["edad"] += 20
# print ( d  )
# print ( d["edad"] )

# for k, v in list(d.items()):
#     print (k,v)