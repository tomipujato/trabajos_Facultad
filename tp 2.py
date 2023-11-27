import os
from getpass import getpass

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def DefinirUsuarios():
    arrayUsuarios = [['' for j in range(4)] for i in range(100)]
    arrayUsuarios[0][0] = "1"
    arrayUsuarios[3][0] = "4"
    arrayUsuarios[5][0] = "6"
    arrayUsuarios[8][0] = "9"
    arrayUsuarios[0][1] = "admin@shopping.com"
    arrayUsuarios[3][1] = "localA@shopping.com"
    arrayUsuarios[5][1] = "localB@shopping.com"
    arrayUsuarios[8][1] = "unCliente@shopping.com"
    arrayUsuarios[0][2] = "12345"
    arrayUsuarios[3][2] = "AAAA1111"
    arrayUsuarios[5][2] = "BBBB2222"
    arrayUsuarios[8][2] = "33xx33"
    arrayUsuarios[0][3] = "administrador"
    arrayUsuarios[3][3] = "dueñoLocal"
    arrayUsuarios[5][3] = "dueñoLocal"
    arrayUsuarios[8][3] = "cliente"

    i = 0
    j = 0
    arrayLocales = [['' for j in range(4)] for i in range(50)]

    return arrayUsuarios, arrayLocales

def MostrarArray(arrayUsuarios):
    for i in range(len(arrayUsuarios)):
        for j in range(len(arrayUsuarios[i])):
            print(arrayUsuarios[i][j])

def MenuAdmin(arrayLocales):
    opc = ""
    while opc != "0":
        print("a. Gestión de locales")
        print("b. Crear cuentas de dueños de locales")
        print("c. Aprobar / Denegar solicitud de descuento")
        print("d. Gestión de Novedades")
        print("e. Reporte de utilización de descuentos")
        print("0. Salir\n")

        opc = input("Seleccione una opción: ")

        def case_a():
            OpcAdmin1(arrayLocales)

        def case_b():
            print("En construcción...")

        def case_c():
            print("En construcción...")

        def case_d():
            print("En construcción...")

        def case_e():
            print("En construcción...")

        def switch_case(case):
            switcher = {
                "a": case_a,
                "b": case_b,
                "c": case_c,
                "d": case_d,
                "e": case_e
            }
            func = switcher.get(case)
            func()

        switch_case(opc)

        input("Presione Enter para continuar...")
        clear()

def OpcAdmin1(arrayLocales):
    def case_a(arrayLocales):
        OpcAdmin1a(arrayLocales)

    def case_b(arrayLocales):
        print("Opción 'Modificar local'")

    def case_c(arrayLocales):
        print("Opción 'Eliminar local'")

    def case_d(arrayLocales):
        print_map(arrayLocales)

    switcher = {
        "a": case_a,
        "b": case_b,
        "c": case_c,
        "d": case_d,
    }

    opc1 = ""
    while opc1 != "e":
        print("a) Crear novedades")
        print("b) Modificar novedad")
        print("c) Eliminar novedad")
        print("d) Ver reporte de novedades")
        print("e) Volver")
        opc1 = input("Seleccione una opción: ")

        func = switcher.get(opc1)
        if func:
            func(arrayLocales)

def OpcAdmin1a(arrayLocales):
    repeated_name = True
    i = 0
    while repeated_name:
        repeated_name = False
        shop_new_name = input("Ingrese el nombre del local: ")
        while not repeated_name and i < 50:
            if shop_new_name == arrayLocales[i][0]:
                repeated_name = True
                print("Nombre ya existente")
            else:
                i += 1

        shop_new_location = input("Ingrese la ubicación del nuevo local: ")

        allowed_type = False
        while not allowed_type:
            shop_new_kind = input("Ingrese el rubro del nuevo local (indumentaria / perfumería / comida): ")
            if shop_new_kind in ["indumentaria", "perfumería", "comida"]:
                allowed_type = True
            else:
                print("Rubro inválido")

        i = 0
        while arrayLocales[i][0] != '' and i < 50:
            i += 1

        if i >= 50:
            print("No hay más espacio para locales")
        else:
            arrayLocales[i][0] = shop_new_name
            arrayLocales[i][1] = shop_new_location
            arrayLocales[i][2] = shop_new_kind
            arrayLocales[i][3] = str(i + 1)

def OpcAdmin2():
    clear()
    print("En construcción...")
    input()

def OpcAdmin3():
    clear()
    print("En construcción...")
    input()

def OpcAdmin4():
    def case_a():
        print("Opción 'Crear novedades'")

    def case_b():
        print("Opción 'Modificar novedad'")

    def case_c():
        print("Opción 'Eliminar novedad'")

    def case_d():
        print("Opción 'Ver reporte de novedades'")

    switcher = {
        "a": case_a,
        "b": case_b,
        "c": case_c,
        "d": case_d,
    }

    opc1 = ""
    while opc1 != "e":
        print("a) Crear novedades")
        print("b) Modificar novedad")
        print("c) Eliminar novedad")
        print("d) Ver reporte de novedades")
        print("e) Volver")
        opc1 = input("Seleccione una opción: ")

        func = switcher.get(opc1)
        if func:
            func()

def get_map_coordinates(code):
    row = (code - 1) // 5
    col = (code - 1) % 5
    return row, col

def print_map(arrayLocales):
    map_grid = [['0' for _ in range(5)] for _ in range(10)]

    for local in arrayLocales:
        if local[0] != '' and local[3] == 'A':
            row, col = get_map_coordinates(int(local[0]))
            map_grid[row][col] = local[0]

    print("Mapa de locales:")
    print("+----+----+----+----+----+")
    for row in map_grid:
        print("| {} | {} | {} | {} | {} |".format(*row))
        print("+----+----+----+----+----+")

def OpcAdmin5():
    clear()
    print("En construcción...")
    input()

def MenuLocal():
    def case_1():
        print("Opción 'Gestión de Descuentos'")

    def case_2():
        print("Opción 'Aceptar / Rechazar pedido de descuento'")

    def case_3():
        print("Opción 'Reporte de uso de descuentos'")

    def default_case():
        print("Opción incorrecta. Intente nuevamente.")

    switcher = {
        "1": case_1,
        "2": case_2,
        "3": case_3,
    }

    opc = ""
    while opc != "0":
        print("1. Gestión de Descuentos")
        print("2. Aceptar / Rechazar pedido de descuento")
        print("3. Reporte de uso de descuentos")
        print("0. Salir")

        opc = input("Seleccione una opción: ")
        clear()

        func = switcher.get(opc, default_case)
        func()

def MenuCliente():
    def case_1():
        print("Opción 'Registrarme'")

    def case_2():
        print("Opción 'Buscar descuentos en locales'")

    def case_3():
        print("Opción 'Solicitar descuento'")

    def case_4():
        print("Opción 'Ver novedades'")

    switcher = {
        "1": case_1,
        "2": case_2,
        "3": case_3,
        "4": case_4,
    }

    opc = ""
    while opc != "0":
        print("1. Registrarme")
        print("2. Buscar descuentos en locales")
        print("3. Solicitar descuento")
        print("4. Ver novedades")
        print("0. Salir")

        opc = input("Seleccione una opción: ")
        clear()

        func = switcher.get(opc)
        if func:
            func()

def Ingreso(arrayUsuarios, arrayLocales):
    def RegisterLogin():
        valid_option = False
        while not valid_option:
            print("1. Ingresar")
            print("2. Registrarme (Usuario)")
            selectedOption = input("Ingrese una opción: ")
            if selectedOption == "1":
                valid_option = True
            elif selectedOption == "2":
                clear()
                valid_option = True
                new_user = input("Ingrese el nombre del nuevo usuario: ")
                new_password = getpass("Ingrese la nueva contraseña: ")
                i = 0
                while arrayUsuarios[i][1] != '' and i < 100:
                    i = i + 1
                if i < 100:
                    arrayUsuarios[i][0] = str(i + 1)
                    arrayUsuarios[i][1] = new_user
                    arrayUsuarios[i][2] = new_password
                    arrayUsuarios[i][3] = "cliente"
                else:
                    print("Ya hay demasiados usuarios registrados")

    clear()
    RegisterLogin()
    intentos = 0
    exit_program = False
    while intentos < 3 and not exit_program:
        def UserSelected(pos):
            tipo = arrayUsuarios[pos][3]
            if tipo == "administrador":
                MenuAdmin(arrayLocales)
            elif tipo == "dueñoLocal":
                MenuLocal()
            elif tipo == "cliente":
                MenuCliente()

        nombre_ingresado = input("Usuario: ")
        pass_ingresada = getpass("Contraseña: ")

        i = 0
        userExist = False
        while not userExist and i < 100:
            if nombre_ingresado == arrayUsuarios[i][1] and pass_ingresada == arrayUsuarios[i][2]:
                userExist = True
                intentos = 0
            else:
                i = i + 1

        if i == 100:
            clear()
            intentos = intentos + 1
            print("USUARIO O CONTRASEÑA INCORRECTO/S")

        if userExist and i < 100:
            clear()
            UserSelected(i)

            re_enter_validOption = False
            while not re_enter_validOption:
                print("1. Ingresar")
                print("0. Salir\n")
                opc_reingreso = input("Ingrese una opción: ")

                if opc_reingreso == "1":
                    exit_program = False
                    re_enter_validOption = True
                elif opc_reingreso == "0":
                    exit_program = True
                    re_enter_validOption = False
                else:
                    print("Ingrese una opción válida")
                    re_enter_validOption = False

arrayUsuarios, arrayLocales = DefinirUsuarios()
Ingreso(arrayUsuarios, arrayLocales)
