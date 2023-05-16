listadetuplas = [("termo", 600, 4, "bigstar"), ("vaso", 300, 8, "bigstar"), ("mate", 1200, 10, "posadas"), ("mate", 100, 20, "posadas"), ("termo", 30000, 2, "apple")]

while (1):
    listaresultado = [ ]
    precio = int(input("ingrese un precio: "))
    marca = (input("ingrese una marca: "))
    for i in range(0, len(listadetuplas)):
        if (listadetuplas[i][1] <= precio) and (listadetuplas [i][3] == marca):
            listaresultado.append(listadetuplas [i])

    print(listaresultado)




tuplameses = ( "" , "enero" , "febrero" ,"marzo", "abril", "mayo" , "junio" , "julio" , "agosto" , "septiembre" , "octubre" , "noviembre" , "diciembre" )

while 1:

    num=int(input("ingrese un numero correspondiente a un mes:   "))

    if num == 0:
        os.system("cls")
        op = input("\nprograma terminado. Precione cualquier tecla para continuar:  ")
    elif (num < 13) and (num > 0):
        for i in range(0,len(tuplameses)):
            if i == num:
                print (f"\n{tuplameses[i]}\n")
    else:
        print ("\nvalor ingresado no es correcto\n")




tuplanumeros = (1,1,4,4,4,2,3,3,3,3,5,5,6,7,7,7,7,8,8,9,9,9,9,9,10,11,12,12,12,12,12)

while 1:
    con = 0
    try:
        num = int(input("Ingrese un numero mayor a 0 y menor a 13: "))
        if (num < 1) or (num > 12):
            print("numero fuera de tupla")
        else:
            print(f"El numero aparece {tuplanumeros.count(num)} vez en la tupla")
    except ValueError:
        print ("Lo que ingresaste no era un numero: ") 