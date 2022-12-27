# CODE:39
# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv

# Objetivo:
# Leer y trabajar con un archivo CSV complejo y el
# manejo de excepciones

def desafio(ambientes):
    print('Ejercicios con archivos CSV complejos')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.
    
    # Según el valor ingresado en "ambientes" está función deberá
    # retornar (return):
    # 1) si ambientes == "2_ambientes"
    #  ---> retornar la cantidad encontrada de ddepartamentos de 2 ambientes
    # 2) si ambientes == "3_ambientes"
    #  ---> retornar la cantidad encontrada de ddepartamentos de 3 ambientes

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # Puede evitar que el programa explote utilizando "try except".

    # Comenzar aquí, recuerde el identado dentro de esta funcion

    csvfile = open('propiedades.csv')

    propiedades = list(csv.DictReader(csvfile))

    propiedades_dos_ambientes = 0
    propiedades_tres_ambientes = 0

    for k in propiedades:
        try:
            ambientes = int(k['ambientes'])
            if ambientes == 2:
                propiedades_dos_ambientes += 1
            elif ambientes == 3:
                propiedades_tres_ambientes += 1
        except:
            print('dato faltante') 
    
    print(f'Propiedades con dos ambientes: {propiedades_dos_ambientes} | Propiedades con tres ambientes: {propiedades_tres_ambientes}')
    
    return propiedades_dos_ambientes, propiedades_tres_ambientes

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    desafio("2_ambientes")
