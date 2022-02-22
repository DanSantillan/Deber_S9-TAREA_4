class Lista:    
    # def __init__(self,datos=[]):
    #     self.lista=datos
    def __init__(self):
        self.lista=[]
        self.ind=0
    
    def push(self,datos):
        self.lista.append(datos)
        self.ind=self.ind+1
        
    def empty(self):
        if self.ind == 0:
            True
        else:
            False
            
    def pop(self):
        if self.empty():
            return "Lista Vacia"
        else:
            self.lista.pop()
            self.ind -=1
    
    def show(self):                   
        for i in self.lista:
            print("[{}]".format(i)) 
        
    def insertar(self,dato):
        self.lista.append(dato)
        
    def obtener(self):
        ultimo = self.lista.pop()
        return ultimo
    
    def eliminarElemento(self,pos):
       if pos in range(0,len(self.lista)):
            ele = self.lista[pos-1]     
            self.lista = self.lista[0:pos-1] + self.lista[pos:]
            self.ind -= 1
            # listaAux = []
            # for ind in range(0,len(self.lista)):
            #     if ind != pos:
            #         listaAux += [self.lista[ind]]
               
            # for indice in range(0,pos):
            #     listaAux = listaAux + [self.lista[indice]] 
            # for indice in range(pos+1,len(self.lista)):
            #     listaAux = listaAux + [self.lista[indice]] 
            # self.lista=listaAux  
            
            return ele
            #return self.lista
       else:
            return None
            #return "Posicion:{} no existe en la lista".format(pos) 
                          #    2   7
    def insertarElemento(self,pos,dato):
        if pos in range(0,len(self.lista)):
            self.lista.insert(pos,dato)
            self.lista +=1
            return self.lista
        else:
            print("No esxiste la posición {}".format(pos))
        #pass
        #[2,4,6,8,10] = [2,4,7,6,8,10] 
        # 0 1 2 3 4
        
    def mostrar(self):
        #return 
        pass
    
    def buscar(self, buscando):
        try:
            dsa=self.lista.index(buscando)
            print("El dato esta en la posición ",dsa+1)
        except ValueError as e:
            print("ERROR: ",e)
    
# numeros = Lista()
# numeros.insertar("Ana")
# numeros.insertar("Daniel")
# numeros.insertar("Jose")
# numeros.insertar("Miguel")
# numeros.insertar("Moises")
# ###numeros=["1","2","3","4","5","6"]
# #print(numeros.obtener())
# print(numeros.lista)
# resp = numeros.eliminarElemento(4)
# print(resp if resp else "posicion:{} no valida".format())
# #print(resp)
# print(numeros.lista)






# ################################################3
# a=["hola","dan","fer"]
# #a=[2,4,6,8,10]
# print (a)

# pos=int(input("ingrese pos: "))
# dato=input("ingrese num: ")

# if pos in range(0,len(a)):
#     #ele = a[pos]
#     a.insert(pos,dato)
#     print(a)
# else:
#     print("no existe la posición {}".format(pos))




# Menu
# 1) Lista
#     1) push    #ingres numero(4)
#     2) pop
#     3) show
#     4) eliminar #ingrese la posicon a eliminar(2)
#     5) insertar
#     6) buscar


