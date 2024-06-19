import time
import random
# ********************** ESTRUCTURAS ****** INICIO ************************************
class estructLibro:
    def __init__(self, titulo: str, pagina: int, genero: str, retraso: bool, autor: str):
        
        self.titulo: str = titulo
        self.pagina: int = pagina
        self.genero: str = genero
        self.retraso: bool = retraso
        self.autor: str = autor

    def imprimirLibro(self):
        print(f"{self.titulo}" + ", " + f"{self.genero}" + ", " + f"{self.pagina}" + " págs, " + f"{self.autor}" + ".")
    
    def getGenero(self):
        return f"{self.genero}"
    
    def getRetraso(self):
        if(self.retraso == True):
            return True
        else:
            return False

class Nodo:
    def __init__(self, id, libro: estructLibro, derecha: 'Nodo' = None, izquierda: 'Nodo' = None):
        self.id: int = id
        self.libro: estructLibro = libro
        self.derecha: 'Nodo' = derecha
        self.izquierda: 'Nodo' = izquierda
      
class Arbol:
    def __init__(self, nodoArbol: Nodo):
        self.nodoArbol: Nodo = nodoArbol
    
    def insertNodo(self, nodo: Nodo):
        nodoAux = self.nodoArbol
        if self.nodoArbol is None:
            self.nodoArbol = nodo
            return
        while True:
            if nodo.id < nodoAux.id:
                if nodoAux.izquierda is None:
                    nodoAux.izquierda = nodo 
                    return
                else:
                    nodoAux = nodoAux.izquierda
            elif nodo.id > nodoAux.id:
                if nodoAux.derecha is None:
                    nodoAux.derecha = nodo
                    return
                else:
                    nodoAux = nodoAux.derecha
            else:
                return
            
# ********************** ESTRUCTURAS ****** FIN ************************************    

# ********************** GENERACIÓN DE LIBRO ****** INICIO ************************************
def genTit():
    
    # Genera un título de libro en español siguiendo la estructura:
    # # El [animal] [acciones] con [estado]
    
    titulo = ["El"]

    animales = [
        "gorila", "chimpancé", "caballo", "perro", "gato",
        "león", "tigre", "elefante", "delfín", "camello",
        "león marino", "hipopótamo", "oso polar", "ornitorrinco",
        "zorro", "rinoceronte", "guepardo", "ratón", "topo", "jaguar"
    ]
    titulo.append(animales[random.randint(0, 19)])

    accion = [
        "trepa", "lanza", "galopea", "ladra", "afila",
        "ruge", "acecha", "destroza", "salta", "camina",
        "baila", "chapotea", "nada", "pone", "escarba",
        "carga", "corre", "roe", "excava", "vuela"
    ]
    titulo.append(accion[random.randint(0, 19)])

    titulo.append("con")
    estado = [
        "tristeza", "felicidad", "exaltación", "entusiasmo", "frialdad",
        "fuerza", "locura", "agresividad", "imparcialidad", "ira",
        "sorpresa", "desesperación", "esperanza", "euforia", "melancolía",
        "apernsión", "serenidad", "euforia", "desasosiego", "desgracia"
    ]
    titulo.append(estado[random.randint(0, 19)])

    
    return " ".join(titulo) 

def genGen():
    accion = [
        "Terror", "Fantasia", "Miedo"
    ]
    
    return accion[random.randint(0,2)]

def genRetra():
    if(random.randint(0,1) == 1):
        return True
    else:
        return False

def genAutor():
    nombre = []
   
    nomb = [
        "Juan", "María", "Carlos", "Ana", "Pedro",
        "Laura", "Diego", "Isabel", "Andrés", "Sofía",
        "Luis", "Elena", "Fernando", "Carmen", "Roberto",
        "Lucía", "Javier", "Marta", "Ricardo", "Valeria"
    ]

    nombre.append(nomb[random.randint(0, 19)])

    primer_apellido = [
        "García", "Martínez", "Rodríguez", "López", "Pérez",
        "Sánchez", "González", "Ramírez", "Torres", "Flores",
        "Hernández", "Fernández", "Gómez", "Díaz", "Muñoz",
        "Álvarez", "Romero", "Herrera", "Medina", "Castro"
    ]
    nombre.append(primer_apellido[random.randint(0, 19)])

    segundo_apellido = [
        "Ruiz", "Morales", "Jiménez", "Moreno", "Ortega",
        "Silva", "Vargas", "Rojas", "Molina", "Soto",
        "Chávez", "Gutiérrez", "Mendoza", "Delgado", "Cruz",
        "Campos", "Castillo", "Vega", "Guerrero", "Ramos"
    ]
    nombre.append(segundo_apellido[random.randint(0, 19)])
    
    return " ".join(nombre)

def genLib(genero):    
    lib = estructLibro(genTit(),random.randint(10,500),genero,genRetra(),genAutor())
    return lib

# ********************** GENERACIÓN DE LIBRO ****** FIN ************************************

# ********************** FUNCIONES GENERALES ************* INICIO ********************************************************

def validarNum(cad):
    try:
        cad = int(cad)
        if cad >= 8 or cad <= 0:
            print("ERROR. El número debe estar entre 1 y 8.\n")
            return None
        else:
            return cad
    except ValueError:
        print("ERROR. No se ha introducido un número.\n")
        return None

def selectArbol():
    print("\nSeleccione el gnénero:")
    print("1. Terror ")
    print("2. Fantasia ")
    print("3. Miedo ")
    num = input("Introduzca el número correspondiente: ")
    
    if not num.isdigit():
        print("ERROR. No se ha introducido un número.\n")
        return -1
    num = int(num)

    if num >= 4 or num <= 0:
        print("ERROR. El número debe estar entre 1 y 3.\n")
        return -1
    return num

def PedirID():
    num = input("Intruzca el ID del libro: ")  
    if not num.isdigit():
        print("ERROR. No se ha introducido un número.\n")
        return -1
    num = int(num)
    if not (num >= 100000 and num <= 999999):
        print("ERROR. El número debe de ser de 6 dígitos.\n")
        return -1
    return num

def Inorden(nodo: Nodo):
    if nodo is not None:
        Inorden(nodo.izquierda)
        print(str(nodo.id) + " ", end='')
        Inorden(nodo.derecha)
    else:
        return None

def guardarNodos(nodo: Nodo, nodos):
    if nodo:
        nodos.append(nodo)
        guardarNodos(nodo.izquierda, nodos)
        guardarNodos(nodo.derecha, nodos)

# ********************** FUNCIONES GENERALES ****** FIN ************************************

# OPCION 1 *****************************************************************************************************    
def insertarNodo(num: int,arbol:Arbol, genero):
    print("\nABB actual: ")
    Inorden(arbol.nodoArbol)
    arbol.insertNodo(Nodo(num,genLib(genero),None,None))
    print("\n\nABB insertado: ")
    Inorden(arbol.nodoArbol)
    print("\n")

def optionUno(Libros_Terror: Arbol,Libros_Miedo: Arbol,Libros_Fantasia: Arbol):

    num = PedirID()
    if num == -1:
        return -1 
    
    genero = selectArbol()
    if genero == -1:
        return -1

    
    if genero == 1:
        insertarNodo(num,Libros_Terror,"Terror")
    if genero == 2:
        insertarNodo(num,Libros_Fantasia,"Fantasia")
    if genero == 3:
        insertarNodo(num, Libros_Miedo,"Miedo")
 

# OPCION 2 *****************************************************************************************************    
def buscarLib(id: int,nod: Nodo):
    if nod is None:
        return None        

    if id > nod.id:
        return buscarLib(id,nod.derecha)
    elif id < nod.id:
        return buscarLib(id,nod.izquierda)
    else:
        return nod
     
def optionDos(Libros_Terror: Arbol,Libros_Miedo: Arbol,Libros_Fantasia: Arbol): # OPTIONNNNNNN
    
    num = selectArbol()

    id = input("Introduzca el ID a buscar: ")
    

    if num == 1:
        Exist = buscarLib(int(id),Libros_Terror.nodoArbol)
    if num == 2:
        Exist = buscarLib(int(id),Libros_Fantasia.nodoArbol)
    if num == 3:
        Exist = buscarLib(int(id),Libros_Miedo.nodoArbol)
    
    if Exist is None:
        print("NO se ha encontrado el libro con el ID establecido")
    else:
        print("\nTítulo, Género, Páginas, Autor.")
        estructLibro.imprimirLibro(Exist.libro)  
       
    
    return

# OPCION 3 *****************************************************************************************************    

def selectTipoBuscar():
    print("\nSeleccione la forma:")
    print("1. Anchura ")
    print("2. Profundidad ")
    num = input("Introduzca el número correspondiente: ")
    
    if not num.isdigit():
        print("ERROR. No se ha introducido un número.\n")
        return -1
    num = int(num)

    if num >= 3 or num <= 0:
        print("ERROR. El número debe estar entre 1 y 2.\n")
        return -1
    return num

def selectTipoBuscarProfund():
    print("\nSeleccione la forma:")
    print("1. Preorden ")
    print("2. Inorden ")
    print("3. Postorden ")
    num = input("Introduzca el número correspondiente: ")
    
    if not num.isdigit():
        print("ERROR. No se ha introducido un número.\n")
        return -1
    num = int(num)

    if num >= 4 or num <= 0:
        print("ERROR. El número debe estar entre 1 y 3.\n")
        return -1
    return num

def Preorden(nodo:Nodo):
    if nodo is not None:
        print(str(nodo.id) + " ", end='')
        Preorden(nodo.izquierda)
        Preorden(nodo.derecha)
    else:
        return None

def Postorden(nodo: Nodo):
    if nodo is not None:
        Postorden(nodo.izquierda)
        Postorden(nodo.derecha)
        print(str(nodo.id) + " ", end='')
    else:
        return None

def printPorTipoProfund(arbol,tipo):
    if arbol is None:
        print("No se han encontrado libros. ")
    elif tipo == 1:
        Preorden(arbol)
    elif tipo == 2:
        Inorden(arbol)
    elif tipo == 3:
        Postorden(arbol)
    else:
        print("ERROR. No se ha introducido correctamente el tipo")

def printArchura(raiz):
    if raiz is None:
        print("No se han encontrado libros. ")
        return ""
    cola = [raiz]
    while cola:
        nodoAux = cola.pop(0)
        print(str(nodoAux.id) + " ", end='')
        if nodoAux.izquierda:
            cola.append(nodoAux.izquierda)
        if nodoAux.derecha:
            cola.append(nodoAux.derecha)

def optionTres(Libros_Terror: Arbol,Libros_Miedo: Arbol,Libros_Fantasia: Arbol): # OPTIONNNNNNN

    arbol = selectArbol()
    if arbol == -1:
        return -1 
    
    tipo = selectTipoBuscar()
    if tipo == -11:
        return -1 
    
    print("")
    if arbol == 1:
        if tipo == 1:
            printArchura(Libros_Terror.nodoArbol)
        else:
            tipoProfund = selectTipoBuscarProfund()  
            printPorTipoProfund(Libros_Terror.nodoArbol,tipoProfund)
    if arbol == 2:
        if tipo == 1:
            printArchura(Libros_Fantasia.nodoArbol)
        else:
            tipoProfund = selectTipoBuscarProfund()   
            printPorTipoProfund(Libros_Fantasia.nodoArbol,tipoProfund)
    if arbol == 3:
        if tipo == 1:
            printArchura(Libros_Fantasia.nodoArbol)
        else:
            tipoProfund = selectTipoBuscarProfund()
            printPorTipoProfund(Libros_Miedo.nodoArbol,tipoProfund)
    
    print("\n")
    
    return ""

# OPCION 4 *****************************************************************************************************    

def borrarNodo(id: int, nod: Nodo):
    if nod is None:
        return None        

    if id > nod.id:
        nod.derecha = borrarNodo(id, nod.derecha)
    elif id < nod.id:
        nod.izquierda = borrarNodo(id, nod.izquierda)
    else:
        if nod.izquierda is None:
            nodoAux = nod.derecha
            nod = None
            return nodoAux
        elif nod.derecha is None:
            nodoAux = nod.izquierda
            nod = None
            return nodoAux
        nodoAux = nod.derecha
        while nodoAux and nodoAux.izquierda:
            nodoAux = nodoAux.izquierda
        nod.id = nodoAux.id
        nod.derecha = borrarNodo(nodoAux.id, nod.derecha)     
    return nod

def optionCuatro(Libros_Terror: Arbol,Libros_Miedo: Arbol,Libros_Fantasia: Arbol): # OPTIONNNNNNN
    id = PedirID()
    arbol = selectArbol()

    if id == -1 or arbol == -1:
        return -1
    
    if arbol == 1:
        Libros_Terror.nodoArbol = borrarNodo(int(id), Libros_Terror.nodoArbol)
    if arbol == 2:
        Libros_Fantasia.nodoArbol = borrarNodo(int(id),Libros_Fantasia.nodoArbol)
    if arbol == 3:
        Libros_Miedo.nodoArbol = borrarNodo(int(id),Libros_Miedo.nodoArbol)
        
    return -1  

# OPCION 5 *****************************************************************************************************    
def comprobarID(ID: int,Libros_Terror:Arbol,Libros_Miedo:Arbol,Libros_Fantasia:Arbol): # Comprobamos si existe un ID dado dentro de los 3 arboles que tenemos
    
    Exist1 = buscarLib(int(ID),Libros_Terror.nodoArbol)
    Exist2 = buscarLib(int(ID),Libros_Miedo.nodoArbol)
    Exist3 = buscarLib(int(ID),Libros_Fantasia.nodoArbol)

    if Exist1 is not None:
        return True
    if Exist2 is not  None:
        return True
    if Exist3 is not None:
        return True

    return False

def addLibros(libros: int, arbolGenero: Arbol, genero,Libros_Terror:Arbol,Libros_Miedo:Arbol,Libros_Fantasia:Arbol):
    i = 0
    while i < libros: 
        boolID = True
        while boolID: # Repetimos el bucle hasta que genere un ID valido
            ID = random.randint(100000,999999)
            boolID = comprobarID(ID,Libros_Fantasia,Libros_Miedo,Libros_Terror)
        if not boolID:
            lib = Nodo(ID,genLib(genero),None,None)
            arbolGenero.insertNodo(lib)       
            i += 1
    return lib

def mostrarActuInse(NLibros: int,ABB: Arbol, genero,Libros_Terror:Arbol,Libros_Miedo:Arbol,Libros_Fantasia:Arbol):
    print("\nABB actual: ")
    Inorden(ABB.nodoArbol)
    addLibros(NLibros,ABB, genero,Libros_Terror,Libros_Miedo,Libros_Fantasia)
    print("\n\nABB insertado: ")
    Inorden(ABB.nodoArbol)
    print("\n")

def optionCinco(Libros_Terror: Arbol,Libros_Miedo: Arbol,Libros_Fantasia: Arbol): # OPTIONNNNNNN
    NLibros = input("Introduzca el número de libros que desea crear: ")
    if not NLibros.isdigit():
        print("ERROR. Se debe de introducir un número positivo.\n")
        return -1
    
    list_1 = []
    list_2 = []
    list_3 = []
    guardarNodos(Libros_Terror.nodoArbol,list_1)
    guardarNodos(Libros_Miedo.nodoArbol,list_2)
    guardarNodos(Libros_Fantasia.nodoArbol,list_3)
    LibrosExistentes = len(list_1) + len(list_2) + len(list_3)

    if int(NLibros) >= 900000 - LibrosExistentes: # 900000 es el Nº de combinaciones máxima
        NLibros = 900000 - LibrosExistentes


    
    arbol = selectArbol()
    if arbol == -1:
        return ""

    if arbol == 1:        
        mostrarActuInse(int(NLibros),Libros_Terror, "Terror",Libros_Terror,Libros_Miedo,Libros_Fantasia)
    if arbol == 2:
        mostrarActuInse(int(NLibros),Libros_Miedo,"Fantasia",Libros_Terror,Libros_Miedo,Libros_Fantasia)
    if arbol == 3:
        mostrarActuInse(int(NLibros),Libros_Fantasia, "Miedo",Libros_Terror,Libros_Miedo,Libros_Fantasia)
    
    return ""

# OPCION 6 *****************************************************************************************************

def genIDs(cantidad):
    IDs = []
    
    while len(IDs) < cantidad:
        num = random.randint(100000, 999999)
        
        if num not in IDs:
            IDs.append(num)
    
    return IDs

def optionSeis(Libros_Terror: Arbol,Libros_Miedo: Arbol,Libros_Fantasia: Arbol): # OPTIONNNNNNN
    NLibros = input("Introduzca el número de libros que desea eliminar: ")
    if not NLibros.isdigit():
        print("ERROR. Se debe de introducir un número positivo.\n")
        return -1


    ListIDs = genIDs(int(NLibros)) # Creamos una lista con números que no se repitan

    rangIDs = len(ListIDs)
    i = 0
    while i < rangIDs:
        print(ListIDs[i])
        borrarNodo(ListIDs[i],Libros_Terror.nodoArbol)
        borrarNodo(ListIDs[i],Libros_Miedo.nodoArbol)
        borrarNodo(ListIDs[i],Libros_Fantasia.nodoArbol)
        i += 1

    return ""

# OPCION 7 *****************************************************************************************************

def RandomNodoSelect(raiz: Nodo):
    NODOs = []
    guardarNodos(raiz, NODOs)
    if NODOs:
        return random.choice(NODOs)
    else:
        return None

def optionSiete(Libros_Terror: Arbol,Libros_Miedo: Arbol,Libros_Fantasia: Arbol): # OPTIONNNNNNN
    
    # 30 segundos 
    tiempo = 1
    while (tiempo <= 60):
        time.sleep(5)
        tiempo = tiempo + 5

        # Primera parte -----------------------------
        nodo = None
        genero = genGen()
        if genero == "Terror":        
            nodo = addLibros(1,Libros_Terror, genero,Libros_Terror,Libros_Miedo,Libros_Fantasia)
        if genero == "Fantasia":
            nodo = addLibros(1,Libros_Fantasia, genero,Libros_Terror,Libros_Miedo,Libros_Fantasia)
        if genero == "Miedo":
            nodo = addLibros(1,Libros_Miedo, genero,Libros_Terror,Libros_Miedo,Libros_Fantasia)
        
        print("*******************************************************")
        print("ABB Terror:   ", end='')
        Inorden(Libros_Terror.nodoArbol)
        print("")

        print("ABB Fantasía: ", end='')
        Inorden(Libros_Fantasia.nodoArbol)
        print("")

        print("ABB Miedo:    ", end='')
        Inorden(Libros_Miedo.nodoArbol) 
        print("")


        print("EVENTO: Se devuelve el libro con id " +  str(nodo.id) + " al ABB de " + genero + ".")
        print("\n")

        # Segunda parte -----------------------------
        nodo_2 = None
        genero_2 = genGen()
        if genero_2 == "Terror":        
            nodo_2:Nodo = RandomNodoSelect(Libros_Terror.nodoArbol)
            if nodo_2:
                if nodo_2.libro.getRetraso:
                    Libros_Terror.nodoArbol = borrarNodo(nodo_2.id,Libros_Terror.nodoArbol)
        if genero_2 == "Fantasia":
            nodo_2: Nodo = RandomNodoSelect(Libros_Fantasia.nodoArbol)
            if nodo_2:
                if nodo_2.libro.getRetraso:
                    Libros_Fantasia.nodoArbol = borrarNodo(nodo_2.id,Libros_Fantasia.nodoArbol)
        if genero_2 == "Miedo":
            nodo_2:Nodo = RandomNodoSelect(Libros_Miedo.nodoArbol)
            if nodo_2:
                if nodo_2.libro.getRetraso:
                    Libros_Miedo.nodoArbol = borrarNodo(nodo_2.id,Libros_Miedo.nodoArbol)
        

        if nodo_2:
                if nodo_2.libro.getRetraso:
                    print("*******************************************************")
                    print("ABB Terror:   ", end='')
                    Inorden(Libros_Terror.nodoArbol)
                    print("")

                    print("ABB Fantasía: ", end='')
                    Inorden(Libros_Fantasia.nodoArbol)
                    print("")

                    print("ABB Miedo:    ", end='')
                    Inorden(Libros_Miedo.nodoArbol) 
                    print("") 
                    print("EVENTO:  Se detecta retraso en la devolución del libro " +  str(nodo.id) + " del ABB de " + genero_2 + ".")
                    print("\n")



# ********************** MAIN ********************************** INICIO ************************************************

Libros_Terror = Arbol(None)
Libros_Fantasia = Arbol(None)
Libros_Miedo = Arbol(None)

while(True):
    num = 0

    print("\n|************************************************************************|")
    print("| Seleccione una opción:                                                 |")
    print("| 1. Insertar un libro en un género                                      |")
    print("| 3. Imprimir lista de libros del género correspondiente                 |")
    print("| 2. Buscar libro en un género                                           |")
    print("| 3. Imprimir lista de libros del género correspondiente                 |")
    print("| 4. Borrar un libro del género correspondiente                          |")
    print("| 5. Generar libros aleatorios y guardar segun su género                 |")
    print("| 6. Generar libros aleatorios y busqueda y eliminación de duplicados    |")
    print("| 7. Iniciar la simulación                                               |")
    print("| 8. Salir de la aplicación                                              |")
    print("|************************************************************************|\n")

   
    num = input("Introduzca el número correspondiente: ")
    
    if not num.isdigit():
        print("ERROR. No se ha introducido un número.\n")
        continue
    num = int(num)
    if num >= 9 or num <= 0:
        print("ERROR. El número debe estar entre 1 y 8.\n")
        continue

    if num == 1:
        optionUno(Libros_Terror,Libros_Miedo,Libros_Fantasia)
    elif num == 2:
        optionDos(Libros_Terror,Libros_Miedo,Libros_Fantasia)
    elif num == 3:
        optionTres(Libros_Terror,Libros_Miedo,Libros_Fantasia)
    elif num == 4:
        optionCuatro(Libros_Terror,Libros_Miedo,Libros_Fantasia)
    elif num == 5:
        optionCinco(Libros_Terror,Libros_Miedo,Libros_Fantasia)
    elif num == 6:
        optionSeis(Libros_Terror,Libros_Miedo,Libros_Fantasia) 
    elif num == 7:
        Libros_Terror = Arbol(None)
        Libros_Fantasia = Arbol(None)
        Libros_Miedo = Arbol(None)
        optionSiete(Libros_Terror,Libros_Miedo,Libros_Fantasia) 
    elif num == 8:
        exit (0) 
    
# ********************** MAIN ****** FIN ********************************************