#Integrantes: Boveri Rafaela, Neffen Jeremias, Neri Milagros, Lopez Pujato Tomas.
import os
import os.path 
from getpass import getpass
import io 
import datetime

arcusuarios="C:\\usuarios.dat"

aux=0
#Definimos los archivos y sus registros
class Usuario:
    def init(self):
        self.nombreUsuario=""
        self.codUsuario=0 
        self.claveUsuario="" 
        self.tipoUsuario=""

class Local:
    def init(self):
        self.nombreLocal="" 
        self.ubicacionLocal="" 
        self.rubroLocal="" 
        self.codUsuario=0 
        self.codLocal=0 
        self.estado="A" #ya lo asignamos como Activo de manera predeterminada/automatica para que se genere cuando crea un local.

class Promociones:
    def init(self):
        self.textoPromo="" 
        self.fechaDesdePromo="" 
        self.fechaHastaPromo="" 
        self.estado="" 
        self.codLocal=0 
        self.diaSemana=[0]*6

class UsoPromocion: 
    def init(self):
        self.codCliente=0 
        self.codPromo=0 
        self.fechaUso=""

class Novedad: #Desarrollado en Chapin
    def init(self):
        self.codNovedad=0 
        self.textoNovedad="" 
        self.fechaDesdeNovedad="" 
        self.fechaHastaNovedad="" 
        self.tipoUsuario="" 
        self.estado="A"




# PRECARGA DEL ARREGLO DE USUARIOS
us = [["", "", "", ""] for f in range(100)]

def precargauser():
    datos = [
        ["1", "admin@shopping.com", "12345", "administrador"],
        # Add more user data here if needed
    ]
    for i, data in enumerate(datos):
        us[i] = data



def buscar_usuario(usuario, contraseña):
    for infous in us:
        if infous[1] == usuario and infous[2] == contraseña:
            return infous
    return None

# Funcion para que borremos la pantalla
def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Inicio del programa
print("Bienvenido al sistema de Shopping Mall")

def primermenu():
    print("1- Ingresar con usuario registrado")
    print("2-Registrarse como cliente")
    print("3-Salir")
    opc = 0 



    while opc < 1 or opc > 3:
        opc= int(input("Ingrese la opcion que desea: "))

        while opc != 3:
            if opc == 1:
                print("Ingreso de Usuario")
                procedimiento_login()
            elif opc == 2:
                print("Registro como cliente")
                # registrocliente()
    Clear()

    

# Procedimiento de inicio de sesión
def procedimiento_login():
    for _ in range(3):
        usuario = input("Usuario: ")
        contraseña = getpass("Contraseña: ")

        usuario_correcto = buscar_usuario(usuario, contraseña)
        if usuario_correcto is not None:
            return usuario_correcto

        print("Credenciales incorrectas. Inténtelo de nuevo.")

    print("Ha alcanzado el límite máximo de intentos.")
    Clear()  # Clear the screen

# desarrollamos el menu del administrador 

def menuadmin():
    print("1. Gestión de locales")
    print("2. Crear cuentas de dueños de locales")
    print("3. Aprobar / Denegar solicitud de descuento")
    print("4. Gestión de Novedades")
    print("5. Reporte de utilización de descuentos")
    print("0. Salir")
    opcadmin=0
    opcadmin=int(input("Ingrese una opción"))
    while opcadmin==0 or opcadmin>1 or opcadmin <5:
        if opcadmin ==1:
            gestiondelocales()
        if opcadmin ==2:
            crearcuentasdueños()
        # if opcadmin ==3:
        #     solicituddedescuento()
        if opcadmin ==4:
            gestiondenovedades()
        else:
            reportedescuentos()
        Clear()

# desarrollamos las funciones del menu

def crearcuentasdueños (kk):
    kk.nombreUsuario=input("ingrese el nombre de usuario")
    cod=aux
    kk.codUsuario=cod
    cod=aux+1
    kk.claveUsuario=input("ingrese la nueva clave del usuario")
    kk.tipoUsuario="dueño"


def gestiondelocales():
    print("a) Crear locales")
    print("b) Modificar local")
    print("c) Eliminar local")
    print("d) Mapa de locales")
    print("e) Volver")    
    # opcgestion="x"
    # opcgestion=str(input("ingrese su opción"))
    # while opcgestion!="e":
    #     if opcgestion=="a":    
    #         crearlocal()
    #     if opcgestion=="b":
    #         modificarlocal()
    #     if opcgestion=="c":
    #         eliminarlocal()
    #     else:
    #         mapalocales()
    # Clear()

def gestiondenovedades():
    print("a) Crear novedades")
    print("b) Modificar novedad")
    print("c) Eliminar novedad")
    print("d) Volver")
    Clear()            

def reportedescuentos():
    Clear()




   
        
# Inicio de sesión
primermenu()
