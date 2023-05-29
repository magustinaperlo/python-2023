def validarOpcion12(opcion):
    try:
        opcion = int(opcion)
        if opcion == 1 or opcion == 2:
            return opcion
        else:
            print("Valor fuera de rango")
            opcion = 0
            return opcion
    except ValueError:
        print("Valor invalido")
        opcion = 0
        return opcion
    
def validarOpcion12345(opcion):
    try:
        opcion = int(opcion)
        if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5:
            return opcion
        else:
            print("Valor fuera de rango")
            opcion = 0
            return opcion
    except ValueError:
        print("Valor invalido")
        opcion = 0
        return opcion

agenda = {}
nombre = ""
telefono = ""
op = ""
flag = 0
buscar = ""
while True:
    op = input("""
    Bienvenido al gestor de contactos
    1. Agregar contacto
    2. Buscar contacto
    3. Eliminar contacto
    4. Mostrar todos los contactos
    5. Salir
    """)
    op = validarOpcion12345(op)
    if op == 1:
        while(True):
            nombre = input("Ingrese nombre del contacto: ")
            telefono = input("Ingrese el numero de telefono: ")
            flag = 0
            for name, cel in agenda.items():
                if nombre == name:
                    while True:
                        op = input(f"""
                        Nombre de contacto encontrado en la agenda
                        nombre: {name}
                        telefono: {cel}                   
                        ¿Desea editarlo?
                        1. Si
                        2. No
                        """)
                        op = validarOpcion12(op)
                        if op == 1:
                            nombre = input("Ingrese nuevo nombre de contacto: ")
                            telefono = input("Ingrese el nuevo numero de telefono: ")
                            agenda[nombre]=telefono
                            flag = 1
                            break
                        if op == 2:
                            break
                if telefono == cel:
                    while True:
                        op = input(f"""
                        Numero de contacto encontrado en la agenda
                        nombre: {name}
                        telefono: {cel}                   
                        ¿Desea editarlo?
                        1. Si
                        2. No
                        """)
                        op = validarOpcion12(op)
                        if op == 0:
                            continue
                        if op == 1:
                            nombre = input("Ingrese nuevo nombre de contacto: ")
                            telefono = input("Ingrese nuevo numero de telefono: ")
                            agenda[nombre]=telefono
                            flag = 1
                            break   
                        if op == 2:
                            break

            if flag == 0:
                agenda[nombre]=telefono

            while True:    
                op = input("""¿Desea agregar mas contactos?
                1. Si
                2. No
                """)
                op = validarOpcion12(op)
                if op == 0:
                    continue
                if op == 1:
                    b = 1
                    break
                if op == 2:
                    b = 0
                    break
            if b == 0:
                op = 0
                break
            
                       
    if op == 2:
        while(True):
            buscar = input("Ingrese nombre o telefono a buscar: ")
            b = 0
            for name, cel in agenda.items():
                if buscar == name or buscar == cel:
                    print(f"""
                    Nombre: {name}
                    Telefono: {cel}
                    """)
                    b = 1
            if b == 0:
                print("Contacto no encontrado")
            while True:
                op = input("""
                ¿Desea buscar algun contacto mas?
                1. Si
                2. No
                """)
                op = validarOpcion12(op)
                if op == 0:
                    continue
                if op == 1:
                    b = 1
                    break
                if op == 2:
                    b = 0
                    break
            if b == 0:
                op = 0
                break
        
    if op == 3:
        while(True):
            delet = input("Ingrese el nombre o numero del contacto que desea eliminar: ")
            b = 0
            for name, cel in agenda.items():
                if delet == name or delet == cel:
                    op = input(f"Desea eliminar este contacto?\nNombre: {name} Telefono: {cel} 1. Si\n2. No\n:")
                    validarOpcion12(op)
                    b = 1
                else:
                    b = 0
            if b == 0:
                print("Contacto no encontrado")
            if b == 1:     
                if (op == 1):
                    agenda.pop(delet)
                elif(op == 2):
                    print("El contacto no sera borrado. Nuevamente...")
                
            while True:
                op = input("""
                ¿Desea eliminar algun contacto mas?
                1. Si
                2. No
                """)
                op = validarOpcion12(op)
                if op == 0:
                    continue
                if op == 1:
                    b=1
                    break
                if op == 2:
                    b=0
                    break
            if b == 0:
                op = 0
                break

    if op == 4:
        while(True):
            for i, k in(agenda.items()):
                print(f"{i} : {k}")
            break

    if op == 5:
        break
        
 '''salvedades:
En la opción 1 , 2 y 3 , del menú principal, dentro del bucle while, se repite la pregunta "¿Desea agregar más contactos?"
incluso después de que se haya ingresado una opción válida. Puedes mover la pregunta fuera del bucle while para que solo
se pregunte una vez al final.
En la opción 4 del menú principal, en lugar de usar un bucle for i, k in(agenda.items()):,
deberías usar for i, k in agenda.items(): para obtener las claves y valores de forma corretca.
En la opción 3 del menú principal, al solicitar al usuario que confirme la eliminación de un contacto, el valor ingresado se almacena en la variable op, pero no se realiza ninguna validación en ese momento.
Debes asignar el resultado de validarOpcion12(op) a la variable op para asegurar
de que sea un valor válido antes de usarlo en la condición if.
El nombre de las funciones no condice con la nomenclatura que hemos visto a comienzo de año con las buenas prácticas ! Revisar eso para las p`róxiimas entregas !! 
