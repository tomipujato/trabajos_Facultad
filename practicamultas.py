import os
import datetime
import pickle

AFM="C://Users//tomas//Desktop//programacion//practica de parciales//elementos//multas.dat"
AFT="C://Users//tomas//Desktop//programacion//practica de parciales//elementos//tipos.dat"
today=datetime.datetime.today()

class multas():
    def __init__(self):
        self.codigo= "".ljust(6)
        self.patende= "".ljust(6)
        self.dni= "".ljust(9)
        self.tipodemulta= 0
        self.lugardeinfraccion= "".ljust(30)
        self.fechadevencimiento= "".ljust(6)
        self.acarreocongrua= "N"
        self.impaga="N"

class tipos ():
    def __init__(self):
        self.tipodemulta=0
        self.valoraabonar=0.00

def printmenu():
    print ("##### MENÚ DE INICIO #####\n")
    print(("{}/{}/{}".format(today.day, today.month, today.year)).ljust(5), ("").ljust(9), ("{}:{}\n".format(today.hour,today.minute)) )
    print ("1_ Consultas")
    print ("2_ Pagos")
    print ("3_ Listado")
    print("4_ Generar multa")
    print("5_ Salir")

def menu():
    while True:
        printmenu()
        opc=int(input("Ingrese una opción\n"))
        while opc<1 and opc > 5:
            print("Ingrese una opción válida\n")
        if opc == 1:
            Consultas()
        elif opc == 2:
            pagos()
        elif opc == 3:
            tipomulta=input("ingrese el tipo de multa a buscar:\n")
            listado(tipomulta)
            
            input()
        elif opc == 4:
            crear_multa()
        elif opc == 5:
            return False

def listado(tipomulta):
    global AFM
    ALM=open(AFM, "r+b")
    multas=pickle.load(ALM)
    tam=os.path.getsize(AFM)
    while ALM.tell() < tam:
        if multas.tipodemulta==tipomulta and multas.impaga=="N":
            printinfo()
   

def printinfo():
    global AFM
    ALM=open(AFM, "r+b")
    mult=pickle.load(ALM)
    print("código: ", mult.codigo)
    print("patente: ", mult.patende)
    print("DNI titular: ", mult.dni)
    print("Tipo de multa: ", mult.tipodemulta)
    print("Lugar de infracción: ", mult.lugardeinfraccion)
    print("Fecha de vencimiento: ", mult.fechadevencimiento)
    print("Acarreo con grúa: ", mult.acarreocongrua)

def printmultas(var, var1):
    global AFM
    ALM=open(AFM, "r+b")
    tam=os.path.getsize(AFM)
    ALM.seek(0,0)
    while ALM.tell() < tam:
        mult=pickle.load(ALM)
        if var1== "DNI":
            if mult.dni==var:
                printinfo()
        if var1=="PATENTE":
            if mult.patente==var:
                printinfo()
    ALM.close()


def Consultas():
    k=True
    while k:
        opc=input("De que forma desea ingresar por DNI (D) o patente (P)\nIngrese D o P: ")
        if opc == "D":
            DNI=input("Ingrese su DNI para comenzar\n")
            var=DNI
            var1="DNI"
            printmultas (var, var1)
            k=False
        elif opc=="P":
            Patent=input("Ingrese su patente para comenzar\n")
            var = Patent
            var1="PATENTE"
            printinfo (var, var1)
        elif opc=="*":
            k=False
        

def pagos():
    global AFM
    ALM=open(AFM,"r+b")
    tam=os.path.getsize(AFM)
    ALM.seek(0,0)
    tamre=ALM.tell()
    if tamre==0:
        print("no hay multas")
    else:
        cantre=int(tam/tamre)
        inicio=0
        final=cantre-1
        medio = cantre/2
        for i in range (cantre-1):
            for j in range (cantre):
                auxi=i*tamre
                auxj=j*tamre

def maxcod():
    global AFM
    ALM=open(AFM,'r+b')
    ALM.seek(2,0)
    multas=pickle.load(ALM)
    codigo=int(multas.codigo)+1
    return codigo

def crear_multa():
    global AFM
    ALM=open(AFM,'r+b')
    while True:
        cod=maxcod()
        print(cod)
        patente=input("Ingrese la patente del infractor:\n")
        DNI=input("Ingrese el DNI del infractor:\n")
        tipomulta=input("Ingrese el tipo de multa que le corresponde:\n")
        lugar=input("Ingrese en donde se cometio la multa:\n")
        fecha= input("Ingrese la fecha de vencimiento:\n")
        acarreo=input("Hubo acarreo con grúa?:\n")
        paga="N"
        ALM.seek(2,0)
        mult=multas()
        mult.codigo=cod
        mult.patende=patente
        mult.dni=DNI
        mult.tipodemulta=tipomulta
        mult.lugardeinfraccion=lugar
        mult.fechadevencimiento=fecha
        mult.acarreocongrua=acarreo
        mult.impaga=paga
        pickle.dump(mult, ALM)
        ALM.flush()
        ALM.close()
        return

def inicializar():
    if os.path.exists(AFM):
        ALM=open(AFM, 'r+b')
    else:
        ALM=open(AFM, "w+b")
    if os.path.exists(AFT):
        ALT=open(AFT, 'r+b')
    else:
        ALT=open(AFT, "w+b")

def precargamulta():
    global AFM
    ALM=open(AFM, "r+b")
    mult=multas()
    mult.codigo=0
    mult.dni="26912394"
    mult.patende="VGE292"
    mult.impaga="N"
    mult.acarreocongrua="N"
    mult.fechadevencimiento="22-10-2023"
    mult.tipodemulta=1
    pickle.dump(mult, ALM)
    ALM.flush()
    ALM.close()


inicializar()
precargamulta()
menu()