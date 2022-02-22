class Colas:                
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
    
    def push(self,dato):
        if self.tope < self.size:
            self.lista += [dato]
            self.tope += 1
        else:
            print("La Cola está Llena")
   
    def pop(self):
        if self.empty():
            return "Lista Vacia"
        else:
            top = self.lista
            self.tope -= 1
            self.lista = self.lista[1:]
            return top

                    
    def longitud(self):
        return self.tope
        
    def show(self):
        if self.empty():
            print("Lista vacia")
        else:                    
            for tope in range(self.tope):
                print("[{}]".format(self.lista[tope]))    
    
    def buscar(self,buscado):
        try:
            dsa=self.lista.index(buscado)
            return(dsa+1)
        except ValueError as e:
            return("ERROR: ",e)
        
   
# pila = Colas(5)
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





# 3) colas
#     1) push
#     2) pop
#     3) show
#     4) buscar
#     5) lingitud
