# 1. Traer datos desde archivo: guardará el contenido del archivo DBZ.csv en una colección. Tener en
# cuenta que tanto razas y habilidades deben estar guardadas en algún tipo de colección debido a que
# un personaje puede tener más de una raza y más de una habilidad.

import csv
import re

ruta = "C:\\Users\\Magalí\\programacion_I\\primer_parcial\\__pycache__\\DBZ.csv"
def leer_lista(ruta:str)->list:
    lista_personajes = []
    with open(ruta, 'r', encoding ='utf-8') as archivo:#as archivo (declaro ya mi variable y guardo el contenido de open)
        for personaje in archivo:
            personaje = personaje.replace("\n", "")
            lista_auxiliar = personaje.split(',')
            
            diccionario_personajes = {}
            diccionario_personajes["Id"] = lista_auxiliar[0]
            diccionario_personajes["Nombre"]= lista_auxiliar[1]
            diccionario_personajes["Raza"] = lista_auxiliar[2]
            diccionario_personajes["Poder de pelea"] = lista_auxiliar[3]
            diccionario_personajes["Poder de ataque"] = lista_auxiliar[4]
            diccionario_personajes["Habilidades"] = lista_auxiliar[5].split('|$%')
            if  "-Humano" in diccionario_personajes["Raza"]:
                diccionario_personajes["Raza"] = lista_auxiliar[2].split('-')
            lista_personajes.append(diccionario_personajes)
            
        return lista_personajes
    
lista_final = leer_lista('DBZ.csv')
print(lista_final)


# 2. Listar cantidad por raza: mostrará todas las razas indicando la cantidad de personajes que corresponden a esa raza.
def cantidad_por_raza(lista_personajes:str):
    diccionario_raza = {}
    for personaje in lista_personajes:
        if type(personaje["Raza"]) == str:
            if personaje["Raza"] in diccionario_raza:
                diccionario_raza[personaje["Raza"]] += 1
            else:
                diccionario_raza[personaje["Raza"]] = 1
        else:
            for personaje in personaje["Raza"]:
                if personaje in diccionario_raza:
                    diccionario_raza[personaje] +=1
                else:
                    diccionario_raza[personaje] = 1
                
    return diccionario_raza
raza = cantidad_por_raza(lista_final)
print(raza)

# 3. Listar personajes por raza: mostrará cada raza indicando el nombre y poder de ataque de cada
# personaje que corresponde a esa raza. Dado que hay personajes que son cruza, los mismos podrán
# repetirse en los distintos listados.

def personajes_por_raza(lista:list):
    diccionario_raza = {}
    for personaje in lista:
        if type(personaje["Raza"]) == str:
            if personaje["Raza"] in diccionario_raza:# esta en diccionario_raza
                diccionario_raza[personaje["Raza"]] += "" #sumale 1
            else:
                diccionario_raza[personaje["Raza"]] = personaje["Nombre"] # si no agregale
        else:
            for personaje in personaje["Raza"]:
                if personaje in diccionario_raza:
                    diccionario_raza[personaje] += ""
                else:
                    diccionario_raza[personaje] = ""
                
    return diccionario_raza    
        
raza = personajes_por_raza(lista_final)
print(raza)














# ef parser_csv(path:str)-> list:
#     lista = []

#     archivo = open(path, "r", encoding="utf-8")
#     for line in archivo:
#         lectura = re.split (",\n", line)
#         tema = {}
#         tema["title"] = lectura[0]
#         tema["views"] = int (lectura[1])
#         tema["lenght"] = int (lectura[2])
#         tema["img_url"] = lectura[3]
#         tema ["url"] = lectura [4]
#         tema["date"] = lectura[5]
#         lista.append(tema)

#         archivo = re.split(

#         )
#     archivo.close()
#     return lista



# archivo.close()
        # CANTIDAD_PERSONAJES = 2
        # lista_personajes = []
    # for ruta in range(CANTIDAD_PERSONAJES):
    #     id = int(input("Ingrese el id: "))
    #     nombre = input("Ingrese nombre Personaje: ")
    #     raza = input("Ingrese la raza: ")
    #     poder_pelea = input("Ingrese podel de pelea: ")
    #     poder_ataque = input("Ingrese poder de pelea: ")
    #     habilidad = input("Ingrese la habilidad de personaje: ")
    #     personajes = {}
    #     personajes["ID"] = id
    #     personajes["Nombre"] = nombre
    #     personajes["Raza"] = raza
    #     personajes["Poder_Pelea"] = poder_pelea
    #     personajes["Poder Ataque"] = poder_ataque
    #     personajes["Habilidades"] = habilidad
    #     lista_personajes.append(personajes)

    #     print(f"{nombre}--{raza}{poder_ataque}")





    












# import csv
# import json

# #binarios
# #texto
# #csv -> coma separated value
# #json -> java script objetc notation

# # leer -> r/r+
# # escribir -> w/w+ ()
# # añadir info -> a

# # archivo = open(ruta, 'r')
# # print(archivo)
# # archivo.close()


# def leer_csv(ruta:str):
#     lista_retorno = []
#     with open(ruta, 'r') as archivo:
#         # segunda_lista_aux = archivo.readlines() esto es una etapa intermedia en lugar de iterar el objeto file de forma directa
#         for usuario in archivo:
#             usuario = usuario.replace("\n", "")
#             lista_aux = usuario.split(',')
#             lista_retorno.append(lista_aux)
#     return lista_retorno

# def guardar_csv(ruta:str, lista_usuarios:list):
#     with open(ruta, 'w') as archivo:
#         for usuario in lista_usuarios:
#             archivo.write(",".join(usuario)+'\n')

# def leer_json(ruta:str)->list:
#     with open(ruta, 'r') as archivo:
#         diccionario_usuarios = json.load(archivo)
#     return diccionario_usuarios["usuarios"]
    
# def guardar_json(ruta:str, lista_usuarios:list)->None:
#     with open(ruta, 'w') as archivo:
#         json.dump(lista_usuarios, archivo, indent=4)


# rutaCSV = "Archivos\\usuarios.csv"
# rutaJSON = "Archivos\\usuarios.json"


# Leer y Escribir en JSON
# lista_usuarios = leer_json(rutaJSON)
# guardar_json('prueba.json', lista_usuarios)

# Leer y Escribir en CSV
# lista_usuarios = leer_csv(rutaCSV)
# guardar_csv("prueba.csv", lista_usuarios)
# print(lista_usuarios)