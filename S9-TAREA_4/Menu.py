class Menu:
    def __init__(self):
        pass

    def menu_principal(self,opcion_DS,titulo_DS):
        print("█"*10,titulo_DS,"█"*10)
        for i in opcion_DS:
            print(i)
        print("█"*10,"█"*(len(titulo_DS)),"█"*10)
        opc= input("Elija una de las opciones[1 - {}]: ".format(len(opcion_DS)))
        return opc

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