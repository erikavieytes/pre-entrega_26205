productos=[] #Creo la lista donde se almacenaran las listas con los datos de cada producto.

#MENU PRINCIPAL.
while True:
    #Menu de Opciones
    print("="*62)
    print("\t*** SISTEMA DE GESTION BASICA DE PRODUCTOS ***")
    print("="*62)
    print("\n\n1. Agregar Producto")
    print("\n2. Mostrar Productos")
    print("\n3. Buscar Producto")
    print("\n4. Eliminar Producto")
    print("\n5. Salir")
    #dentro del Bucle voy a solicitar al usuario que ingrese la opcion a ejecutar.
    opcion = input(f"\n\nSelecciona la opción que desea realizar: ").strip()
#------------------------------------------------------------------------------------------------------

#A partir de aca voy a evaluar que opcion elige el usuario y continua con las acciones correspondientes.
    # OPCION 1 - ALTA DE PRODUCTO
    if opcion == "1":
        while True:
            print("\n" + "="*40)
            print("\t*** AGREGAR PRODUCTO ***")
            print("="*40)
            #Validacion el PRODUCTO que va a ingresar el usuario.
            while True:
                nombre = input("\nIngrese el nombre del producto: ").strip().upper() #Quiero que borre los espacios en blanco y que ademas pase la palabra completa a MAYUSCULA.
                if len(nombre) == 0:
                    print("\nERROR: Este campo no puede estar vacío.")
                else:
                    break
        
            #Si ingreso dato en el campo PRODUCTO debe solicitar la CATEGORIA del mismo, con las mismas validaciones.
            while True:
                categoria = input("\nIngrese la Categoria del producto: ").strip().upper()
                if len(categoria) == 0:
                    print("\nERROR: Este campo no puede estar vacío.")
                else:
                    break

            #Ingresado el producto y su categoria, se pedira el precio, que sera un str primero. Voy a validar que no este vacio. Para despues convertirlo en int.
            while True:
                precio_str = input("\nIngrese el precio del producto (sin centavos): ").strip()
                #ahora voy a validar que solo ingresen numeros enteros y sin comas ni decimales (dato numerico entero positivo)
                if precio_str.isdigit():
                    precio = int(precio_str)
                    if precio >0: # Si es menor a 0, no se permite porque estamos hablando de precios. $
                        break
                    else:
                        print("\nERROR: El precio debe ser mayor a 0.")
                else:
                    print("\nERROR: Ingrese un precio entero válido, sin letras ni decimales.")
            #Con los tres datos, creo una lista que voy a guardar en la primer lista creada producto[].
            nuevo_producto =[nombre,categoria,precio]
            productos.append(nuevo_producto)
            print("\n\t*** PRODUCTO REGISTRADO CON EXITO ***")

            while True:
                print("\n" + "="*46)
                print("\t*** MENU ALTA DE PRODUCTOS ***")
                print("="*46)
                print("\n1. Agregar otro producto")
                print("\n2. Volver al menú anterior")
                sub_opcion = input("\n\nSelecciona una opción (1 o 2): ").strip()
                
                # Validamos que elija una opción correcta
                if sub_opcion == "1" or sub_opcion == "2":
                    break
                else:
                    print("\nERROR: Opción inválida. Por favor ingresa 1 o 2.")
            
            if sub_opcion == "2":
                # Si elige 2, sale del bucle de "Agregar Producto" y vuelve al menú principal
                break
    
    # OPCION 2 - MOSTRAR PRODUCTOS REGISTRADOS
    elif opcion == "2":
        while True:
            print("="*54)
            print("\t*** LISTA DE PRODUCTOS REGISTRADOS ***")
            print("="*54)
            if len(productos) == 0: 
                print("\nNo hay productos registrados en el Sistema.")
                break #Como no hay productos, vuelve al menu principal para que elija otra opcion.

            else: 
                for i in range(len(productos)):
                    producto_muestra = productos[i]
                    print(f"\n{i+1}. Nombre del Producto: {producto_muestra[0]} | Categoría: {producto_muestra[1]} | Precio: ${producto_muestra[2]}")
                    break
            #SUB-MENU DE MOSTRAR PRODUCTOS - aparece directamente cuando luego de mostrar mensaje de produtos            

            print("\n" + "="*46)
            print("\t*** MENU MOSTRAR PRODUCTOS ***")
            print("="*46)
            print("\n1. Volver al menú principal")
            print("\n2. Salir del sistema")
            
            sub_opcion = input("\n\nSelecciona una opción (1 o 2): ").strip()
            
            if sub_opcion == "1":
                #Vuelve al MENU PRINCIPAL
                break 
            elif sub_opcion == "2":
                #SALE del SISTeMA completamente
                print("\n\t*** SALIENDO DEL SISTEMA ***")
                print("\nGracias por trabajar con Talento by Eri.")
                exit() 
            else:
                #Solicita que vuelva a ingresar Opcion valida.
                print("\nERROR: Opción inválida. Por favor ingresa 1 o 2.")
                    
    # OPCION 3 - MOTOR DE BUSQUEDA DE PRODUCTOS
    elif opcion == "3":
        while True:
            # Si la lista está vacía antes de mostrar el menú, le dice al usuario que no hay prod y vuelve al MENU PRINCIPAL.
            if len(productos) == 0:
                print("\nNo hay productos registrados en el Sistema.")
                break # VUELVE AL MENU PRINCIPAL

            #SUB-MENU DE LA OPCION 3
            print("\n" + "="*45)
            print("\t*** BUSQUEDA DE PRODUCTOS ***")
            print("="*45)
            print("\n1. Busqueda por Producto")
            print("\n2. Busqueda por Categoría")
            print("\n3. Volver al menú principal")
            print("\n4. Salir del sistema")

            sub_opcion = input("\nSelecciona una opción: ").strip()
            
            if sub_opcion == "1":
            # BÚSQUEDA POR PRODUCTO
                busqueda = input("\nIngrese el Nombre del producto a buscar: ").strip().upper()
                encontrado = False # para saber si encontramos algo
                
                for prod in productos:
                    # Comparamos con el índice 0 de la lista (Nombre)
                    if prod[0] == busqueda:
                        print(f"\n-> Nombre del Producto: {prod[0]} | Categoría: {prod[1]} | Precio: ${prod[2]}")
                        encontrado = True
                        
                if not encontrado:
                    print("\nNo se encontraron resultados para ese producto.")

            elif sub_opcion == "2":
            # BÚSQUEDA POR CATEGORÍA
                busqueda_cat = input("\nIngrese la Categoría a buscar: ").strip().upper()
                encontrado = False # para saber si encontre o no alguna coicidencia.
                
                print(f"\n\t*** Productos en la categoría '{busqueda_cat}' ***")
                for prod in productos:
                    # Busco en la lista en la posicion 1, donde se ubican las categorias.
                    if prod[1] == busqueda_cat:
                        # Solo muestro el nombre del Producto y su precio.
                        print(f"\n-> Nombre: {prod[0]} | Precio: ${prod[2]}")
                        encontrado = True #Como encontró valor coincidente entonces cambio a true.
                        
                if not encontrado:
                    print("\nNo se encontraron productos registrados en esa categoría.")

            elif sub_opcion == "3":
            # Volver al MENU PRINCIPAL
                break 
                
            elif sub_opcion == "4":
                # Cierra el programa por completo, saltándose el menú principal
                print("\n\t*** SALIENDO DEL SISTEMA ***")
                print("\nGracias por trabajar con Talento by Eri.")
                exit() 
                
            else:
                # Actualicé el mensaje de error para que incluya 3 y 4
                print("\nERROR: Opción inválida. Por favor ingresa 1, 2, 3 o 4.")

    #OPCION 4 - ELIMINAR PRODUCTOS
    elif opcion == "4":
        while True:
            # Si la lista está vacía antes de mostrar el menú, le dice al usuario que no hay prod y vuelve al MENU PRINCIPAL.
            if len(productos) == 0:
                print("\nNo hay productos registrados en el Sistema para eliminar.")
                break # VUELVE AL MENU PRINCIPAL
        
            #SUB-MENU DE LA OPCION 4
            print("\n" + "="*45)
            print("\t*** ELIMINAR PRODUCTO ***")
            print("="*45)
            print("\n1. Buscar Producto para eliminar")
            print("\n2. Volver al menú principal")
            print("\n3. Salir del sistema")
        
            sub_opcion = input("\nSelecciona una opción: ").strip()

            if sub_opcion == "1":
                while True:
                    # Aca muestro la lista de productos añadidos
                    print("\n\t--- Lista de Productos ---")
                    for i in range(len(productos)):
                        print(f"{i+1}. {productos[i][0]}")

                    # la opción de ingresar 0 para cancelar 
                    id_eliminar = input("\nIngrese el número de Producto que desea eliminar (o '0' para cancelar): ").strip()
                    
                    if id_eliminar == "0":
                        print("\n*** OPERACION CANCELADA ***. \n Volviendo al Menú Principal.")
                        break # Sale y vuelve al sub-menú de la opción 4.

                    if id_eliminar.isdigit():
                    # verifica si el usuario ingreso un numero
                        pos = int(id_eliminar)
                        # VALIDACION DE LA OPCION INGRESADA
                        if 1 <= pos <= len(productos):
                            nombre_a_eliminar = productos[pos - 1][0]# aca guardo el nombre del producto temporalmente
                            # Que el usuario confirme con: S/N
                            confirmacion = input(f"\n¿Está seguro que desea eliminar '{nombre_a_eliminar}'? (S/N): ").strip().upper()
                            
                            if confirmacion == "S":
                                producto_eliminado = productos.pop(pos - 1)
                                print(f"\n\t*** El producto '{producto_eliminado[0]}' ha sido eliminado correctamente. ***")
                                break # Se eliminó con éxito, rompemos el bucle y volvemos al sub-menú
                            
                            elif confirmacion == "N":
                                print("\nOperación cancelada. El producto no fue eliminado.")
                                break # El usuario canceló, rompemos el bucle y volvemos al sub-menú
                            
                            else:
                                print("\nERROR: Opción inválida. Debes ingresar 'S' para confirmar o 'N' para cancelar.")
                                # Como aquí NO hay un break, el bucle se reinicia y vuelve a mostrar la lista
                                
                        else:
                            print("\nERROR: El número ingresado no corresponde a ningún producto de la lista.")
                            # Como NO hay break, vuelve a mostrar la lista
                    else:
                        print("\nERROR: Entrada inválida. Debes ingresar el número de la lista (ej: 1, 2, 3).")
                        # Como NO hay break, vuelve a mostrar la lista

            elif sub_opcion == "2":
                # Volver al MENU PRINCIPAL
                break 
                
            elif sub_opcion == "3":
                #PARA SALIR DEL PROGRAMA COMPLETAMENTE.
                print("\n\t*** SALIENDO DEL SISTEMA ***")
                print("\nGracias por trabajar con Talento by Eri.")
                exit() 
                
            else:
                print("\nERROR: Opción inválida. Por favor ingresa 1, 2 o 3.")

    #OPCION 5 - SALIR DEL SISTEMA
    elif opcion == "5":
        print("\n\t*** SALIENDO DEL SISTEMA ***")
        print("\nGracias por trabajar con Talento by Eri.")
        break
    
    #CUANDO EL USUARIO INGRESA UNA OPCION INVALIDA
    else:
        print("Opción inválida. Por favor, selecciona un número del 1 al 5.")