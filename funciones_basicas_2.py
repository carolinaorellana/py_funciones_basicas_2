"""
Cuenta regresiva: crea una función que acepte un número como entrada. Devuelve una lista nueva que cuente de uno en uno, desde el número (como elemento 0) hasta 0 (como último elemento). 
Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0]
"""
def cuentaRegresiva (numero):
    listaRegresiva=[]
    for i in range (numero, -1, -1):
        listaRegresiva.append(i)
    return listaRegresiva
x = cuentaRegresiva(5)
print(x)

"""
Imprimir y devolver: crea una función que reciba una lista con dos números. Imprime el primer valor y devuelve el segundo.
Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2
"""
def imprimirDevolver(lista):
    print(lista [0])
    return lista[1]

y = imprimirDevolver([2,3,4])
# print(y) si se quiere ver el retorno

"""
Primero más longitud: crea una función que acepte una lista y devuelva la suma del primer valor de la lista, más la longitud de la lista.
Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 +length: 5)
"""
def primeroLongitud (list):
    primero = list[0]
    longitud = len(list)
    return primero+longitud
z = primeroLongitud ([1,2,3,4,5])
print(z)

"""
Valores mayores que el segundo: escribe una función que acepte una lista y cree una nueva que contenga solo los valores de la lista original que sean mayores que su segundo valor. Imprime cuántos valores son y luego devuelve la lista nueva. Si la lista tiene menos de 2 elementos, has que la función devuelva False
Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]
Ejemplo: valores_mayores_que_el_segundo([3]) debe devolver False
"""
def mayorSegundo (lista):
    if len(lista)>1:
        listaMayor=[]
        for iterador in lista:
            if iterador> lista[1]:
                listaMayor.append(iterador)
        print(len(listaMayor))
        return listaMayor
    else:
        return False

a= mayorSegundo ([5,2,3,2,1,4])
b = mayorSegundo ([9])
print(a)
print(b)

"""
Esta longitud, ese valor: escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean todos el valor dado.
Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]
"""

def longValor(t,v):
    lista= []
    lista.append(v)
    return t*lista

print(longValor(4,7))
print(longValor(6,2))