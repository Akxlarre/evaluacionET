import os

precio_platinum = 120000
precio_gold = 80000
precio_silver = 50000

def mostrar_menu ():
    print("menu")
    print("1-comprar entradas ")
    print("2-mostrar ubicaciones disponibles")
    print("3-ver listado de asistentes ")
    print("4-mostrar ganancias totales")

lista_entradas = [[1, 'comprado', 120000, 201790204], [2, 'comprado', 12000, 201790522], [3, 'disponible', 120000, 0], [4, 'disponible', 120000, 0], [5, 'disponible', 120000, 0], [6, 'disponible', 120000, 0], [7, 'disponible', 120000, 0], [8, 'disponible', 120000, 0], [9, 'disponible', 120000, 0], [10, 'disponible', 120000, 0], [11, 'disponible', 120000, 0], [12, 'disponible', 120000, 0], [13, 'disponible', 120000, 0], [14, 'disponible', 120000, 0], [15, 'disponible', 120000, 0], [16, 'disponible', 120000, 0], [17, 'disponible', 120000, 0], [18, 'disponible', 120000, 0], [19, 'disponible', 120000, 0], [20, 'disponible', 120000, 0], [21, 'disponible', 80000, 0], [22, 'disponible', 80000, 0], [23, 'disponible', 80000, 0], [24, 'disponible', 80000, 0], [25, 'disponible', 80000, 0], [26, 'disponible', 80000, 0], [27, 'disponible', 80000, 0], [28, 'disponible', 80000, 0], [29, 'disponible', 80000, 0], [30, 'disponible', 80000, 0], [31, 'disponible', 80000, 0], [32, 'disponible', 80000, 0], [33, 'disponible', 80000, 0], [34, 'disponible', 80000, 0], [35, 'disponible', 80000, 0], [36, 'disponible', 80000, 0], [37, 'disponible', 80000, 0], [38, 'disponible', 80000, 0], [39, 'disponible', 80000, 0], [40, 'disponible', 80000, 0], [41, 'disponible', 80000, 0], [42, 'disponible', 80000, 0], [43, 'disponible', 80000, 0], [44, 'disponible', 80000, 0], [45, 'disponible', 80000, 0], [46, 'disponible', 80000, 0], [47, 'disponible', 80000, 0], [48, 'disponible', 80000, 0], [49, 'disponible', 80000, 0], [50, 'disponible', 80000, 0], [51, 'disponible', 50000, 0], [52, 'disponible', 50000, 0], [53, 'disponible', 50000, 0], [54, 'disponible', 50000, 0], [55, 'disponible', 50000, 0], [56, 'disponible', 50000, 0], [57, 'disponible', 50000, 0], [58, 'disponible', 50000, 0], [59, 'disponible', 50000, 0], [60, 'disponible', 50000, 0], [61, 'disponible', 50000, 0], [62, 'disponible', 50000, 0], [63, 'disponible', 50000, 0], [64, 'disponible', 50000, 0], [65, 'disponible', 50000, 0], [66, 'disponible', 50000, 0], [67, 'disponible', 50000, 0], [68, 'disponible', 50000, 0], [69, 'disponible', 50000, 0], [70, 'disponible', 50000, 0], [71, 'disponible', 50000, 0], [72, 'disponible', 50000, 0], [73, 'disponible', 50000, 0], [74, 'disponible', 50000, 0], [75, 'disponible', 50000, 0], [76, 'disponible', 50000, 0], [77, 'disponible', 50000, 0], [78, 'disponible', 50000, 0], [79, 'disponible', 50000, 0], [80, 'disponible', 50000, 0], [81, 'disponible', 50000, 0], [82, 'disponible', 50000, 0], [83, 'disponible', 50000, 0], [84, 'disponible', 50000, 0], [85, 'disponible', 50000, 0], [86, 'disponible', 50000, 0], [87, 'disponible', 50000, 0], [88, 'disponible', 50000, 0], [89, 'disponible', 50000, 0], [90, 'disponible', 50000, 0], [91, 'disponible', 50000, 0], [92, 'disponible', 50000, 0], [93, 'disponible', 50000, 0], [94, 'disponible', 50000, 0], [95, 'disponible', 50000, 0], [96, 'disponible', 50000, 0], [97, 'disponible', 50000, 0], [98, 'disponible', 50000, 0], [99, 'disponible', 50000, 0], [100, 'disponible', 50000, 0]]

def mostrar_entradas_disponibles():

    for entradas in lista_entradas:
        if entradas[1] == "disponible":
            print(f"[{entradas[0]}]", end="")
        elif entradas[1] == "comprada":
            print("[X]", end="")

def mostrar_precios():
            print(f"""
                Precios
            ----------------------
            1- platium = {precio_platinum} / asientos del 1 al 20
            2-gold    = {precio_gold}     / asientos del 21 al 50
            3- silver  = {precio_silver}   / asientos del 51 al 100
            """)

def comprar_entradas():
    
    def ingresar_cantidad_entradas():

        def verificador_cantidad(cantidad):
            if cantidad >=1 and cantidad <= 3:
                return True
            else:
                return False

        while True:
            try:
                cantidad = int(input("ingrese la cantidad de entradas "))
                if verificador_cantidad(cantidad):
                    return cantidad
                else:
                    print("ingrese una opcion correcta")
            except:
                print("ocurrio un error")
    
    
    def ingresar_tipo_entrada():
            
        def ingresar_lugar():

            def verificador_lugar(lugar):
                    if lugar > 0 and lugar <=100:
                        return True
                    else: 
                        return False
            
            def ingresar_rut():
            
                def validador_rut(rut):
                    if rut >= 7 and rut <=8:
                        return True
                    else:
                        return False

                while True:
                    try:
                        rut = int(input("ingresa un rut para registrarlo con la entrada"))
                        if validador_rut(rut):
                            lista_entradas[lugar].append(rut)
                            break
                        else:
                            print("rut invalido")
                    except:
                        print("exepcion")
                
            while True:
                try:
                    lugar = int(input("ingresa el lugar que quieres"))
                    if verificador_lugar(lugar):
                        lugar -= 1
                        ingresar_rut()
                        cambiar_estado_entrada(lista_entradas,lugar)                        
                        
                        break
                    else:
                        print("ingrese una opcion validad")
            
                except:
                    print("exepcion")
                    
        def cambiar_estado_entrada(lista,lugar):

            if lista[lugar,1] == "comprada":
                print("ese asiento ya esta comprado, ingrese otro")
            else :
                lista[lugar,1] = "comprada"
                lista_entradas[lugar].append()
                

        def ingresar_tipo():
            
            def verificador_tipo(tipo):
                if tipo > 0 and tipo <=3:
                    return True
                else:
                    return False
            entradas = ingresar_cantidad_entradas()
            while entradas != 0:
                try:
                    tipo_entrada = int(input("ingrese tipo de entrada: "))
                    if verificador_tipo(tipo_entrada):
                        ingresar_lugar()
                        entradas -= 1
                        break
                    else:
                        print("ingrese una opcion valida")
                except:
                    print("excepcion")

        ingresar_cantidad_entradas()
        mostrar_entradas_disponibles()
        mostrar_precios()
        
        ingresar_tipo()

    ingresar_tipo_entrada()


def ver_listado_asistentes():
    lista_asistentes = []
    print("asistentes por rut")
    for entrada in lista_entradas:
        if entrada[3] != 0 :
            asistente = entrada[3]
            lista_asistentes.append(asistente)
    print(f"{lista_asistentes.sort()}")

def mostrar_ganancias():

    cantidad_platinum = 0
    cantidad_gold = 0
    cantidad_silver = 0
    total= 0
    for tipo in lista_entradas:
        if tipo[1] == 'comprado':
            if tipo[2] == 120000:
                cantidad_platinum +=1
                total += 120000
            elif tipo[2] == 80000:
                cantidad_gold += 1
                total += 80000
            else:
                cantidad_silver +=2
                total += 50000
    print("/tipo de entrada        /  cantidad            /  total  ")
    print(f"platinum 120.000       /  {cantidad_platinum} /  {cantidad_platinum * 120000} " )
    print(f"platinum 120.000       /  {cantidad_gold}     /  {cantidad_gold * 80000} " )
    print(f"platinum 120.000       /  {cantidad_silver}   /  {cantidad_silver * 50000} " )
    print(f"total                 /  {cantidad_platinum + cantidad_gold + cantidad_silver} /  {cantidad_platinum * 120000 + cantidad_gold * 80000 + cantidad_silver * 50000} " )

def main ():

    while True:
        try:
            mostrar_menu()
            opcion = int(input("ingrese una opcion"))
            if opcion == 1:
                comprar_entradas()
                input("enter para continuar")
                os.system("cls")
            elif opcion == 2:
                mostrar_entradas_disponibles()
                input("enter para continuar")
                os.system("cls")
            elif opcion == 3:
                ver_listado_asistentes()
                input("enter para continuar")
                os.system("cls")
            elif opcion == 4:
                mostrar_ganancias()
                input("enter para continuar")
                os.system("cls")
            elif opcion == 5:
                print("nombre: Benjamin Rebolled... fecha = 10/07/2023")
                exit()
            else:
                print("ingrese una opcion correcta")
        except:
            print("error")

main()
