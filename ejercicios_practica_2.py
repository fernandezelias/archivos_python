# CODE:37
# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con diccionarios

import csv


def desafio():
    print('Ejercicio con diccionarios como base de datos')
    # Utilizaremos el diccionario como una base de datos. 
    # Comenzaremos con un diccionario de stock
    # de nuestros productos en cero:
    
    stock = {'tornillos': 0, 'tuercas': 0, 'arandelas': 0}

    # Paso 1:
    # Crear un bucle utilizando while que se ejecute de forma infinita
    # while True.....
    
    # Paso 2:
    # Dentro de ese bucle consultar al usuario por consola
    # que producto desea agregar al stock
    #   - Si el usuario ingresa "FIN" como producto se debe 
    #   finalizar el bucle
    #   - No debe agregar stock de productos que no estén
    #   definidos inicialmente en el diccionario stock.
    #   Para verificar si un producto existe dentro del
    #   diccionario stock utilice el operador "in" visto en clase

    # Paso 3:
    # Luego de haber ingresado el producto valido, se debe
    # ingresar por consola cuanto stock de ese producto se desea agregar.
    # Si teniamos 20 tornillos y el usuario desea agregar 10 tornillos más,
    # en nuestro diccionario deben quedar 30 tornillos (debe acumular)

    # Paso 4:
    # Cuando el usuario ingrese "FIN" y se termine el bucle, debe
    # imprimir en pantalla con print el diccionario con el stock final
    # Al final de esta función retornar (return) la variable stock

    # Comenzar aquí, recuerde el identado dentro de esta funcion

    
    while True:

        print(''' 
        PRODUCTOS DISPONIBLES:
        1- Tornillos
        2- Tuercas
        3- Arandelas
        4- FIN: salir del programa
        ''')
        
        producto = str(input('Ingrese el producto que desea agregar al stock:\n'))
        
        if producto == "1" and "tornillos" in stock:
            stock['tornillos'] += int(input('¿Cuántos tornillos desea ingresar al stock?\n'))
                                    
        elif producto == "2" and "tuercas" in stock:
            stock['tuercas'] += int(input('¿Cuántas tuercas desea ingresar al stock?\n'))
            
        elif producto == "3" and "arandelas" in stock:
            stock['arandelas'] += int(input('¿Cuántas arandelas desea ingresar al stock?\n'))

        elif producto == "4":
            break
    
    print(f"El stock actualizado de productos es:", stock)
    return stock
    

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    desafio()