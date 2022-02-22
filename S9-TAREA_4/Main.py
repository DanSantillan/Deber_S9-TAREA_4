from inspect import stack
from Menu import Menu
from Colas import Colas
from Listas import Lista
from Pilas import Stack 
import os

dato_lis=Lista()
menu= Menu()
men_2= ["1. Lista","2. Pilas", "3. Colas", "4. Salir"]
opcion_men1 = ""

while True:
    os.system("cls")
    opcion_men1 = menu.menu_principal(men_2,"Menu Principal")
    if opcion_men1 == "1":
        menu_o1 = ""
        while True:
            os.system("cls")
            menu_o1 = Menu.menu_principal("",["1. Push", "2. Pop", "3. Show","4. Eliminar","5. Insertar","6. Buscar","7. Salir"],"Menu lista")
            os.system("cls")
            if menu_o1 == "1":
                dat1 = input("Ingrese un dato: ")
                dato_lis.push(dat1)
                input("Presione cualquier tecla para continuar.")
            elif menu_o1 == "2":
                dato_lis.pop()
                input("Se eliminó un dato de la lista, presione cualquier tecla.")
            elif menu_o1 == "3":
                print("█"*10,"Mostrando la lista","█"*10)

                dato_lis.show()
                input("Presione cualquier tecla para continuar.")
            elif menu_o1 == "4":
                posicion = int(input("Ingrese la posición del dato que desea eliminar: "))
                print(dato_lis.eliminarElemento(posicion))
                input("Presione cualquier tecla para continuar.")
            elif menu_o1 ==  "5":
                pos2 = int(input("Ingrese la posición del dato: "))
                dat = input("Ingrese el nuevo dato que desea insertar: ")
                print(dato_lis.insertarElemento(pos2-1,dat))
                input("Presione cualquier tecla para continuar.")
            elif menu_o1 == "6":
                bus = input("Ingrese el dato a buscar: ")
                dato_lis.buscar(bus)
                input("Presione cualquier tecla para continuar.")
            elif menu_o1 == "7":
                    break
                
    elif opcion_men1 == "2":
        menu_op2 = ""
        os.system("cls")
        daniel = int(input("Ingrese el tope máximo de la Pila: "))
        fel = Stack(daniel)
        os.system("cls")
        while True:
            os.system("cls")
            menu_op2 = Menu.menu_principal("",["1. Push", "2. Pop", "3. Show","4. Buscar","5. Longitud","6. Salir"],"Menu Pila")
            os.system("cls")
            if menu_op2 == "1":
                fd2 = input("Ingrese un dato: ")
                fel.push(fd2)
                input("Presione una tecla para continuar.")
            elif menu_op2 == "2":
                fel.pop()
                input("Se eliminó un dato de la Pila, presione cualquier tecla.")
            elif menu_op2 == "3":
                print("█"*10,"Mostrando la Pila","█"*10)
                fel.show()
                input("Presione cualquier tecla para continuar.")
            elif menu_op2 == "4":
                buscar2= input("Ingrese el dato a buscar: ")

                print("El dato se encuentra en la posición ",fel.buscar(buscar2))
                input("Presione cualquier tecla para continuar.")
            elif menu_op2 == "5":
                print("█"*10,"Mostrando la longitud de la Pila","█"*10)
                f5 = Stack(len())
                #f5.longitud()
                #print(f5)
                print(fel.longitud())
               
                input("Presione cualquier tecla para continuar.")
            elif menu_op2 == "6":
                break
            
    elif opcion_men1 == "3":
        menu_op3= ""
        os.system("cls")
        dfsa = int(input("Ingrese el tope máximo de la Cola: "))
        dfs = Colas(dfsa)
        os.system("cls")
        while True:
            os.system("cls")
            menu_op3 = Menu.menu_principal("",["1. Push", "2. Pop", "3. Show","4. Buscar","5. Longitud","6. Salir"],"Menu Cola")
            os.system("cls")
            if menu_op3 == "1":
                adi0 = input("Ingrese un dato: ")
                dfs.push(adi0)

                input("Presione una tecla para continuar.")
            elif menu_op3 == "2":
                dfs.pop()
                input("Se eliminó un dato de la Cola, presione cualquier tecla.")
            elif menu_op3 == "3":
                print("█"*10,"Mostrando la Pila","█"*10)
                dfs.show()
                input("Presione cualquier tecla para continuar.")
                
            elif menu_op3 == "4":
                a_bus2= input("Ingrese el dato a buscar: ")
                print("El dato se encuentra en la posición ",dfs.buscar(a_bus2))
                input("Presione cualquier tecla para continuar.")
                
            elif menu_op3 == "5":
                print("█"*10,"Mostrando la longitud de la Cola","█"*10)
                #a5.longitud()
                print(dfs.longitud())
                #print(a5)
                input("Presione cualquier tecla para continuar.")
                
            elif menu_op3 == "6":              
                break
                
    elif opcion_men1 == "4":
        os.system("cls")
        break
print("Gracias por usar el programa.")



# class Prueba:
#     def __init__(self):
#         self.lista=["20","30","40","50"]
#         #self.lista=[20,30,40,50,60,70]

#     def buscar(self,numero):
#         try:
#             c=self.lista[::-1].index(numero)
#             print(c+1)
#         except ValueError as e:
#             print("Error: ",e)
         
# numero= Prueba()
# numero.buscar("20")
# #numero.buscar(20)





## funciona
# lista=["20","30","40","50"]
# b="20"

# try:
#     c=lista[::-1].index(b)
#     print(c)
# except ValueError as e:
#     print("Error: ",e)


##funciona
# lista=["20","30","40","50"]
# b="20"
# print(lista.index(b))


# Menu
# 1) Lista
#     1) push    ingres numero(4)
#     2) pop
#     3) show
#     4) eliminar ingrese la posicon a eliminar(2)
#     5) insertar
#     6) buscar
# 2) pilas
#     1) push
#     2) pop
#     3) show
#     4) buscar
#     5) longitud

# 3) colas
#     1) push
#     2) pop
#     3) show
#     4) buscar
#     5) lingitud