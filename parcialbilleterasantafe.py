import os
import pickle
import datetime
from datetime import datetime

AFG="C://Users//tomas//Desktop//programacion//practica de parciales//gobierno.dat"
AFC="C://Users//tomas//Desktop//programacion//practica de parciales//comercios.dat"
AFCL="C://Users//tomas//Desktop//programacion//practica de parciales//clientes.dat"

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class gobierno ():
    def __init__ (self):
        self.aportes=[0]*12

class comercios ():
    def __init__ (self):
        self.qr=" ".ljust(15)
        self.lepagaron= 0.00

class clientes ():
    def __init__ (self):
        self.dni=" ".ljust(8)
        self.saldo=0.00
        self.pago=0.00
        self.recupero=0.00
        self.mes=0
        self.estado="S"

def printmenu():
    print("##### bienvenidos al menú #####\n")
    print(" ".ljust(5),"1_ Alta Comercios", " ".ljust(10))
    print(" ".ljust(5),"2_ Alta Clientes", " ".ljust(10))
    print(" ".ljust(5),"3_ Actualizar - Billetera", " ".ljust(10))
    print(" ".ljust(5),"4_ Comprar ", " ".ljust(10))
    print(" ".ljust(5),"5_ Informe Gobierno", " ".ljust(10))
    print(" ".ljust(5),"6_ Fin", " ".ljust(10))

def menuprincipal():
    opc=""
    while True:
        printmenu()
        opc=int(input())
        if opc <= 6 and opc >= 1:
            if opc==1:
                altacomercios()
            if opc==2:
                altaclientes()
            if opc==3:
                actualizarbilletera()
            if opc==4:
                comprar()
            if opc==5:
                informegobierno()
            if opc ==6:
                return    
        else :
            print("ingrese un número correcto...")
        
        Clear()

def inicializar():
    if os.path.exists(AFG):
        ALG=open(AFG, "r+b")
        ALG.close()
    else:
        ALG=open(AFG, "w+b")
        ALG.close()

    if os.path.exists(AFC):
        ALC=open(AFC, "r+b")
        ALC.close()
    else: 
        ALC=open(AFC, "w+b")
        ALC.close()

    if os.path.exists(AFCL):
        ALCL=open(AFCL, "r+b")
        ALCL.close()
    else: 
        ALCL=open(AFCL, "w+b")
        ALCL.close()


def ver_comercios(QR):
    global AFC
    ALC=open(AFC, "r+b")
    tam = os.path.getsize(AFC)
    ALC.seek(0,0)
    while ALC.tell()<tam:
        comercio=pickle.load(ALC)
        if comercio.qr == QR:
            print ("comercio ya inscripto")
            ALC.close()
            return False
        if comercio.qr != QR:
            ALC.close()
            return True 
    return True   



def altacomercios():
    global AFC
    while True:
        QR=str(input("ingrese el qr del nuevo comercio a crear o ingrese * si desea terminar:\n")).ljust(15)
        veri=ver_comercios(QR)
        if QR!="*".ljust(15):
            if veri == True or None:
                AlC=open(AFC, "r+b")
                comercio=comercios()
                comercio.qr=QR
                comercio.lepagaron=0.00
                pickle.dump(comercio, AlC)
                AlC.flush()
                AlC.close()
        if QR=="*".ljust(15):
            return 

def ver_cliente(DNI):
    global AFCL
    ALCL = open(AFCL, "r+b")
    tam = os.path.getsize(AFCL)
    while ALCL.tell()<tam:
        client = pickle.load(ALCL)
        if client.dni == DNI:
            print("cliente ya inscripto")
            ALCL.close()
            return False
    ALCL.close()
    return True


def altaclientes():
    global AFCL
    today = datetime.today()
    while True:
        DNI=str(input("ingrese el DNI del nuevo comercio a crear o ingrese * si desea terminar:\n")).ljust(8)
        veri=ver_cliente(DNI)
        if DNI!="*".ljust(8):
            if veri == True:
                ALCL=open(AFCL, "r+b")
                cliente=clientes()
                cliente.dni=DNI
                cliente.saldo=float(input("ingrese su saldo"))
                cliente.pago=0.00
                cliente.recupero=0.00
                cliente.mes=today.month
                pickle.dump(cliente, ALCL)
                ALCL.flush()
                ALCL.close()
        if DNI=="*".ljust(8):
            return 

def buscaruserandmonth(DNI):
    global AFCL 
    today = datetime.today()
    ALCL=open(AFCL, "r+b")
    tam=os.path.getsize(AFCL)
    ALCL.seek(0,0)
    while ALCL.tell()<tam:
        client=pickle.load(ALCL)
        if client.dni == DNI:
            if client.mes>=today.month:
                pos=ALCL.tell()
                if client.recupero >= 5000:
                    client.estado=="N"
                    pickle.dump(client, AFCL)
                    ALCL.flush()
                    ALCL.close()                
                return pos
            elif client.mes<today.month:
                client.recupero=0.00
                client.estado="S"
                client.mes=today.month
                pickle.dump(client, AFCL)
                ALCL.flush()
                ALCL.close()
                return pos
            else:
                ALCL.close()
                return -2
        else:
            ALCL.close()
            return -1



def actualizarbilletera():
    DNI=input("ingrese su dni:\n")
    opt=buscaruserandmonth(DNI)
    if opt == -2:
        print("Error in month")
        Clear ()
        return
    elif opt == -1:
        print("user dont exist")
        Clear ()
        return

def verdni(DNI, valor):
    global AFCL 
    global AFC
    ALC=open(AFC, "r+b")
    ALCL=open(AFCL, "r+b")
    tam=os.path.getsize(AFCL)
    ALCL.seek(0,0)
    while ALCL.tell() > 0 and ALCL.tell() < tam:
        client=pickle.load(ALCL)
        if client.dni== DNI:
            pos=ALCL.tell()
            ALCL.seek(pos,0)
            if client.saldo >= valor:
                if client.estado=="N":
                    lep=valor*0.15
                    cliente=clientes()
                    cliente.pago=valor
                    comer=comercios()
                    comer.lepagaron=lep
                    pickle.dump(ALCL, cliente)
                if client.estado=="S":
                    reembolso=valor*0.30
                    lep=valor*0.15
                    client.pago=valor
                    client.recupero=reembolso
                    comer=comercios()
                    comer.lepagaron=lep
                    pickle.dump(ALC, comer )
                    ALCL.close()
                    ALC.close()
            elif client.saldo<=valor:
                print("No posee el monto a pagar")



def comprar():
    while True:
        actualizarbilletera()
        QR=input("ingrese el qr del negocio o * para salir\n")
        corro = ver_comercios(QR)
        if corro ==True:
            valor = float(input("ingrese el valor del producto:\n "))
            DNI=input("ingrese el DNI suyo\n")
            verdni(DNI, valor)
        if corro ==False or QR=="*":
            print("comercio no habilitado\n aprete enter para continuar\n")
            kk=input()
            return False
        

        


##################### INICIALIZAR PROGRAM #####################
inicializar()
menuprincipal()