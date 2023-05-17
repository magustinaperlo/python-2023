def divisibles(valor):
    if (int(valor) % 2 == 0 and int(valor) % 3 == 0):
        print(str(valor) + " Es divisible por 2 y 3")
    else:
        divisibles(valor= int(input("No es divisible por 2 y 3, ingrese nuevo valor: ")))
divisibles(valor = int(input("Ingresa un numero para dividir por 2 y 3:  ")))
#########
#Profe
def divisibles(valor):
    if (valor % 2 == 0 and valor % 3 == 0):
        print(str(valor) + " es divisible por 2 y 3")
    else:
        nuevo_valor = int(input("No es divisible por 2 y 3, ingrese un nuevo valor: "))
        divisibles(valor=nuevo_valor)

valor_inicial = int(input("Ingresa un número para verificar si es divisible por 2 y 3: "))
divisibles(valor=valor_inicial)

"""Correcciones realizadas:
Al parecer indagaste sobre funciones recursivas , que son aquellas que se llaman a sí mismas dentro de la función hasta que el valor ingresado corresponda a la condición.
Eliminé la conversión innecesaria a int dentro de la función. Como ya estás pasando un entero a la función divisibles(), no es necesario convertirlo nuevamente.
Cambié el mensaje de salida para que sea coherente con la lógica de la función.
Guardé el nuevo valor ingresado en una variable nuevo_valor dentro del bloque else y luego llamé a la función divisibles() con el nuevo valor."""
#########


def multiplicacion (num1,num2):
    
    suma = num1 * num2
    print ("El resultado de " + str(num1) + " * " + str(num2) + " = "+ str(suma))


multiplicacion(num1 = int(input("Ingrese se primer numero:  ")),num2 = int(input("Ingrese su 2° numero:  ")))
##########
#Profe
def multiplicacion(num1, num2):
    resultado = num1 * num2
    print(f"El resultado de {num1} * {num2} = {resultado}")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
multiplicacion(num1, num2)
"""
esta bien escrita y realiza la multiplicación de dos números correctamente. Sin embargo, hay algunas mejoras que puedes realizar para que sea más flexible y reutilizable:
"""
def multiplicacion(num1, num2):
    resultado = num1 * num2
    print(f"El resultado de {num1} * {num2} = {resultado}")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
multiplicacion(num1, num2)

"""Mejoras realizadas:
Usé una f-string para formatear la salida y hacerla más legible.
Eliminé el uso de str() en las llamadas a print() ya que las variables num1 y num2 ya son enteros.
Separé la lectura de los números de la llamada a la función multiplicacion() para que puedas reutilizar la función con otros valores si así lo deseas.
"""


##########
  

def regla3 (num1, num2, num3):
    calculo = (num1 * num2)/num3
    print ("El resultado de "+ str("(") + str(num1) + " * " + str(num2) +str(")") + str(" \ ") + str(num3) + " = "+ str(calculo))

regla3(num1 = int(input("Ingrese se primer numero para la regla de 3 simple:  ")),num2 = int(input("Ingrese su segundo numero:  ")),num3 = int(input("Ingrese su tercer numero:  ")))
"""
Profe:
"""
def regla3(num1, num2, num3):
    resultado = (num1 * num2) / num3
    print(f"El resultado de ({num1} * {num2}) / {num3} = {resultado}")

num1 = float(input("Ingrese el primer número para la regla de tres simple: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
regla3(num1, num2, num3)
"""
La mejora para tu función de regla de 3 simple fue permitirle decimales para calcular: 
Al cambiar los tipos de datos a float, podrás ingresar números decimales y realizar cálculos precisos con ellos. 
Ahora podrás utilizar decimales en lugar de enteros al ejecutar la función regla3
"""

###########


def cargarLista(lista):
    estado = 1
    while (estado==1):
        nombre = input("ingrese un nombre: ")
        estado = int(input("Desea continuar? 1-Si Otro-No:  "))
        lista.append(nombre)
    print (lista)

a = []
cargarLista(a)

"""
Profe:
"""
def cargarLista(lista):
    continuar = True
    while continuar:
        nombre = input("Ingrese un nombre: ")
        lista.append(nombre)
        respuesta = input("¿Desea continuar? (Sí/No): ")
        if respuesta.lower() != "si":
            continuar = False
    print(lista)

a = []
cargarLista(a)
"""
Mejoras realizadas:

Reemplacé la variable estado por continuar para hacer más evidente su propósito.
Utilicé un bucle while continuar en lugar de while estado == 1 que en el rubro llamamos  BANDERA, lo que nos permite utilizar directamente el valor booleano.
Modifiqué la forma en que se verifica la respuesta del usuario. Ahora se compara en minúsculas y se verifica si es diferente de "si" para terminar el bucle.
Agregué un mensaje más claro en la solicitud de confirmación de continuación.
"""

###########


def diferenciaParesImpares(lista):
    listapar=[]
    listaimpar=[]
    for i in lista:
        if (i % 2 ==0):
            listapar.append(i)
        else:
            listaimpar.append(i)
    print (listapar)
    print (listaimpar)
lista=[2,42,1,45,76,85,8]
diferenciaParesImpares(lista)

"""
Profe:
"""
def diferenciaParesImpares(lista):
    listapar = []
    listaimpar = []

    for num in lista:
        if isinstance(num, int) and not isinstance(num, bool):
            if num % 2 == 0:
                listapar.append(num)
            else:
                listaimpar.append(num)

    print("Lista de números pares:", listapar)
    print("Lista de números impares:", listaimpar)

lista = [2, 42, 1, 45, 76, 85, 8, 3.14, "abc", True]
diferenciaParesImpares(lista)

"""
para asegurarme de que la función diferenciaParesImpares no reciba números decimales:
isinstance() es una función incorporada de Python que se utiliza para verificar si un objeto pertenece a una clase
o tipo de dato específico. Acepta dos argumentos: el objeto que se va a verificar y la clase o tipo que se desea verificar.
devuelve True si el objeto es una instancia de la clase o tipo especificado, o una instancia de una subclase de dicho tipo.
 para asegurarme de que los elementos de la lista sean de tipo int y no sean de tipo bool. Esto excluye tanto los números
 decimales como otros tipos de datos que no sean enteros. Además, agregue algunos elementos adicionales a la lista de entrada lista
 para mostrar cómo se manejarían diferentes tipos de datos en la función.

la función ahora ignorará los elementos que NOsean enteros y solo procesará los números enteros
para separar los pares e impares en las listas correspondientes.
"""

    
