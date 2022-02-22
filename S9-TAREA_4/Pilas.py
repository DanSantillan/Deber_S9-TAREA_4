class Stack:   
     
    def __init__(self,tamanio):
        self.lista=[]
        self.tope=0
        self.size=tamanio
        #pass
     
    def empty(self):
        # if self.tope == 0:
        #     return True
        # else:
        #     return False
        return self.tope == 0
        #pass
    
    def push(self,dato):
        if self.tope < self.size:
            self.lista += [dato]
            self.tope += 1
        else:
            print("La Pila está Llena")
   
    def pop(self):
        if self.empty():
            return "Lista Vacia"
        else:
            top = self.lista[-1]
            self.tope -= 1
            self.lista = self.lista[:-1]
            return top
            
    def longitud(self):
        return self.tope
        #print(length_hint(self.tope))
    
        
    def show(self):
        if self.empty():
            print("Lista vacia")
        else:                    
            for tope in range(self.tope-1,-1,-1):
                print("[{}]".format(self.lista[tope]))    
    
    def buscar(self,buscado):
        try:
            dsa=self.lista[::-1].index(buscado)
            return(dsa+1)
        except ValueError as e:
            return("ERROR: ",e)
        #return "Retorna la posicion del valor buscado"
   
# pila = Stack(6)
# pila.push("4")       
# pila.push("3")       
# pila.push("2")       
# pila.push("5")       
# pila.push("20")       
# pila.push("10")   
# pila.show()    
# print(pila.pop())
# print(pila.pop())
# print(pila.pop())
# print(pila.pop())
# print(pila.pop())
# print(pila.pop())






# class Prueba:
#     def __init__(self):
#         self.lista=["20","30","40","50"]
#         #self.lista=[20,30,40,50,60,70]

#     def buscar(self,numero):
#         try:
#             numero=self.lista[::-1].index(numero)
#             print(numero+1)
#         except ValueError as e:
#             print("Error: ",e)
         
# numero= Prueba()
# numero.buscar("20")
# #numero.buscar(20)





# Menu
# 2) pilas
#     1) push
#     2) pop
#     3) show
#     4) buscar
#     5) longitud


