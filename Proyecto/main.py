from usuarios.lista_enlazada_simple import ListaUsuarios
from usuarios.usuario import Usuario
from salas.lista_doblemente_enlazada import ListaSalas
from salas.sala import Sala
from peliculas.lista_doblemente_circular import ListaPeliculas
from peliculas.pelicula import Pelicula
from facturas.lista_enlazada_simple import ListaFacturas
from facturas.factura import Factura
from boletos.boleto import Boleto

def menu_principal(lista_usuarios, lista_peliculas, lista_salas, lista_facturas):
    menu_principal = True
    while menu_principal:
        print("\n--- MENÚ PRINCIPAL ---\n"
              "1 - Iniciar sesión\n"
              "2 - Registrar usuario\n"
              "3 - Ver listado de películas\n"
              "4 - Salir")
        try:
            opcion = int(input("Ingrese el número correspondiente a la acción a realizar: "))
            if opcion == 1:
                print("\n--- INICIAR SESIÓN ---")
                correo = input("Ingrese su correo: ")
                contrasena = input("Ingrese su contraseña: ")
                if correo == "admin" and contrasena == "admin":
                    menu_administrador(lista_usuarios, lista_peliculas, lista_salas)
                else:
                    usuario_logeado = lista_usuarios.iniciar_sesion_usuario(correo, contrasena)
                    if usuario_logeado != None:
                        if usuario_logeado.get_rol() == "administrador":
                            menu_administrador(lista_usuarios, lista_peliculas, lista_salas)
                        elif usuario_logeado.get_rol() == "cliente":
                            menu_cliente(usuario_logeado, lista_peliculas, lista_salas, lista_facturas)
                    else:
                        print("[ERROR-IS]: Correo o contraseña incorrectos")
            elif opcion == 2:
                registrar_usuario(lista_usuarios)
            elif opcion == 3:
                ver_peliculas(None, lista_peliculas)
            elif opcion == 4:
                print("Saliendo...")
                menu_principal = False
            else:
                print("[ERROR-MP]: La opción ingresada no existe")
        except:
            print("[ERROR-MP]: La opción ingresada es inválida")

def menu_cliente(usuario_logeado, lista_peliculas, lista_salas, lista_facturas):
    menu_cliente = True
    while menu_cliente:
        print("\n--- MENÚ CLIENTE ---\n"
              "1 - Ver listado de películas\n"
              "2 - Listado de películas favoritas\n"
              "3 - Comprar boletos\n"
              "4 - Historial de boletos comprados\n"
              "5 - Salir")
        try:
            opcion = int(input("Ingrese el número correspondiente a la acción a realizar: "))
            if opcion == 1:
                ver_peliculas(usuario_logeado, lista_peliculas)
            elif opcion == 2:
                ver_peliculas_favoritas(usuario_logeado)
            elif opcion == 3:
                comprar_boletos(usuario_logeado, lista_peliculas, lista_salas, lista_facturas)
            elif opcion == 4:
                historial_boletos(usuario_logeado, lista_facturas)
            elif opcion == 5:
                menu_cliente = False
            else:
                print("[ERROR-MC]: La opción ingresada no existe")
        except:
            print("[ERROR-MC]: La opción ingresada es inválida")

def menu_administrador(lista_usuarios, lista_peliculas, lista_salas):
    menu_administrador = True
    while menu_administrador:
        menu_secundario = True
        print("\n--- MENÚ ADMINISTRADOR ---\n"
              "1 - Gestionar usuarios\n"
              "2 - Gestionar películas\n"
              "3 - Gestionar salas\n"
              "4 - Gestionar boletos\n"
              "5 - Salir")
        try:
            opcion = int(input("Ingrese el número correspondiente a la acción a realizar: "))
            if opcion == 1:
                while menu_secundario:
                    print("\n--- GESTIONAR USUARIOS ---\n"
                          "1 - Crear usuario\n"
                          "2 - Cargar usuarios\n"
                          "3 - Modificar usuario\n"
                          "4 - Eliminar usuario\n"
                          "5 - Guardar cambios\n"
                          "6 - Regresar")
                    try:
                        opcion_usuario = int(input("Ingrese el número correspondiente a la acción a realizar: "))
                        if opcion_usuario == 1:
                            crear_usuario(lista_usuarios)
                        elif opcion_usuario == 2:
                            cargar_usuarios(lista_usuarios)
                        elif opcion_usuario == 3:
                            modificar_usuario(lista_usuarios)
                        elif opcion_usuario == 4:
                            eliminar_usuario(lista_usuarios)
                        elif opcion_usuario == 5:
                            guardar_usuarios(lista_usuarios)
                        elif opcion_usuario == 6:
                            menu_secundario = False
                        else:
                            print("[ERROR-MAGU]: La opción ingresada no existe")
                    except:
                        print("[ERROR-MAGU]: La opción ingresada es inválida")
            elif opcion == 2:
                while menu_secundario:
                    print("\n--- GESTIONAR PELÍCULAS ---\n"
                          "1 - Crear película\n"
                          "2 - Cargar películas\n"
                          "3 - Modificar película\n"
                          "4 - Eliminar películas\n"
                          "5 - Guardar cambios\n"
                          "6 - Regresar")
                    try:
                        opcion_pelicula = int(input("Ingrese el número correspondiente a la acción a realizar: "))
                        if opcion_pelicula == 1:
                            crear_pelicula(lista_peliculas)
                        elif opcion_pelicula == 2:
                            cargar_peliculas(lista_peliculas)
                        elif opcion_pelicula == 3:
                            modificar_pelicula(lista_peliculas)
                        elif opcion_pelicula == 4:
                            eliminar_pelicula(lista_peliculas)
                        elif opcion_pelicula == 5:
                            guardar_peliculas(lista_peliculas)
                        elif opcion_pelicula == 6:
                            menu_secundario = False
                        else:
                            print("[ERROR-MAGP]: La opción ingresada no existe")
                    except:
                        print("[ERROR-MAGP]: La opción ingresada es inválida")
            elif opcion == 3:
                while menu_secundario:
                    print("\n--- GESTIONAR SALAS ---\n"
                          "1 - Crear sala\n"
                          "2 - Cargar salas\n"
                          "3 - Modificar sala\n"
                          "4 - Eliminar sala\n"
                          "5 - Guardar cambios\n"
                          "6 - Regresar")
                    try:
                        opcion_sala = int(input("Ingrese el número correspondiente a la acción a realizar: "))
                        if opcion_sala == 1:
                            crear_sala(lista_salas)
                        elif opcion_sala == 2:
                            cargar_salas(lista_salas)
                        elif opcion_sala == 3:
                            modificar_sala(lista_salas)
                        elif opcion_sala == 4:
                            eliminar_sala(lista_salas)
                        elif opcion_sala == 5:
                            guardar_salas(lista_salas)
                        elif opcion_sala == 6:
                            menu_secundario = False
                        else:
                            print("[ERROR-MAGS]: La opción ingresada no existe")
                    except:
                        print("[ERROR-MAGS]: La opción ingresada es inválida")
            elif opcion == 4:
                gestionar_boletos(lista_facturas)
            elif opcion == 5:
                menu_administrador = False
            else:
                print("[ERROR-MA]: La opción ingresada no existe")
        except:
            print("[ERROR-MA]: La opción ingresada es inválida")

def crear_usuario(lista_usuarios):
    print("\n--- CREAR USUARIO ---")
    try:
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        telefono = int(input("Ingrese el teléfono: "))
        correo = input("Ingrese el correo: ")
        contrasena = input("Ingrese la contraseña: ")
        rol = input("Ingrese el rol (administrador/cliente): ")
        if not lista_usuarios.verificar_duplicado(telefono, correo):
            usuario = Usuario(nombre, apellido, telefono, correo, contrasena, rol)
            lista_usuarios.agregar_usuario(usuario)
            print("*** Usuario registrado con éxito")
        else:
            print("[ERROR-CU]: Ya existe un usuario con el teléfono y correo ingresados")
    except:
        print("[ERROR-CU]: Ingresó un dato inválido")

def cargar_usuarios(lista_usuarios):
    print("\n--- CARGAR USUARIOS ---")
    lista_usuarios.cargar_usuarios()

def modificar_usuario(lista_usuarios):
    print("\n--- MODIFICAR USUARIO ---")
    if lista_usuarios.get_tamanio() == 0:
        print("[ERROR-MU]: No hay usuarios disponibles")
    else:
        lista_usuarios.imprimir()
        try:
            id_usuario = int(input("Ingrese el ID correspondiente al usuario a modificar: "))
            if lista_usuarios.verificar_id(id_usuario):
                try:
                    print("--- Datos usuario ---")
                    nombre = input("Ingrese el nombre: ")
                    apellido = input("Ingrese el apellido: ")
                    telefono = int(input("Ingrese el teléfono: "))
                    correo = input("Ingrese el correo: ")
                    contrasena = input("Ingrese la contraseña: ")
                    rol = input("Ingrese el rol (administrador/cliente): ")
                    if not lista_usuarios.verificar_duplicado(telefono, correo):
                        usuario = Usuario(nombre, apellido, telefono, correo, contrasena, rol)
                        lista_usuarios.modificar_usuario(id_usuario, usuario)
                        print("*** Usuario modificado con éxito")
                    else:
                        print("[ERROR-MU]: Ya existe un usuario con el teléfono y correo ingresados")
                except:
                    print("[ERROR-MU]: Ingresó un dato inválido")
            else:
                print("[ERROR-MU]: No existe un usuario con el ID ingresado")
        except:
            print("[ERROR-MU]: Ingresó un ID inválido")

def eliminar_usuario(lista_usuarios):
    print("\n--- ELIMINAR USUARIO ---")
    if lista_usuarios.get_tamanio() == 0:
        print("[ERROR-EU]: No hay usuarios disponibles")
    else:
        lista_usuarios.imprimir()
        try:
            id_usuario = int(input("Ingrese el ID correspondiente al usuario a eliminar: "))
            if lista_usuarios.verificar_id(id_usuario):
                lista_usuarios.eliminar_usuario(id_usuario)
                print("*** Usuario eliminado con éxito")
            else:
                print("[ERROR-EU]: No existe un usuario con el ID ingresado")
        except:
            print("[ERROR-EU]: Ingresó un ID inválido")

def guardar_usuarios(lista_usuarios):
    print("\n--- GUARDAR CAMBIOS ---")
    lista_usuarios.guardar_usuarios()

def crear_pelicula(lista_peliculas):
    print("\n--- CREAR PELÍCULA ---")
    try:
        titulo = input("Ingrese el título: ")
        director = input("Ingrese el director: ")
        anio = int(input("Ingrese el año: "))
        fecha = input("Ingrese la fecha: ")
        hora = input("Ingrese la hora: ")
        categoria = input("Ingrese la categoría: ")
        if not lista_peliculas.verificar_duplicado(categoria, titulo, director, anio, fecha, hora):
            pelicula = Pelicula(categoria, titulo, director, anio, fecha, hora)
            lista_peliculas.agregar_pelicula(pelicula)
            print("*** Película registrada con éxito")
        else:
            print("[ERROR-CP]: Ya existe una película con los datos ingresados")
    except:
        print("[ERROR-CP]: Ingresó un dato inválido")

def cargar_peliculas(lista_peliculas):
    print("\n--- CARGAR PELÍCULAS ---")
    lista_peliculas.cargar_peliculas()

def modificar_pelicula(lista_peliculas):
    print("\n--- MODIFICAR PELÍCULA ---")
    if lista_peliculas.get_tamanio() == 0:
        print("[ERROR-MP]: No hay películas disponibles")
    else:
        lista_peliculas.imprimir()
        try:
            id_pelicula = int(input("Ingrese el ID correspondiente a la película a modificar: "))
            if lista_peliculas.verificar_id(id_pelicula):
                try:
                    print("--- Datos película ---")
                    titulo = input("Ingrese el título: ")
                    director = input("Ingrese el director: ")
                    anio = int(input("Ingrese el anio: "))
                    fecha = input("Ingrese la fecha: ")
                    hora = input("Ingrese la hora: ")
                    categoria = input("Ingrese la categoría: ")
                    if not lista_peliculas.verificar_duplicado(categoria, titulo, director, anio, fecha, hora):
                        pelicula = Pelicula(categoria, titulo, director, anio, fecha, hora)
                        lista_peliculas.modificar_pelicula(id_pelicula, pelicula)
                        print("*** Película modificada con éxito")
                    else:
                        print("[ERROR-MP]: Ya existe una película con los datos ingresados")
                except:
                    print("[ERROR-MP]: Ingresó un dato inválido")
            else:
                print("[ERROR-MP]: No existe una película con el ID ingresado")
        except:
            print("[ERROR-MP]: Ingresó un ID inválido")

def eliminar_pelicula(lista_peliculas):
    print("\n--- ELIMINAR PELÍCULA ---")
    if lista_peliculas.get_tamanio() == 0:
        print("[ERROR-EP]: No hay películas disponibles")
    else:
        lista_peliculas.imprimir()
        try:
            id_pelicula = int(input("Ingrese el ID correspondiente a la película a eliminar: "))
            if lista_peliculas.verificar_id(id_pelicula):
                lista_peliculas.eliminar_pelicula(id_pelicula)
                print("*** Película eliminada con éxito")
            else:
                print("[ERROR-EP]: No existe una película con el ID ingresado")
        except:
            print("[ERROR-EP]: Ingresó un ID inválido")

def guardar_peliculas(lista_peliculas):
    print("\n--- GUARDAR CAMBIOS ---")
    lista_peliculas.guardar_peliculas()

def crear_sala(lista_salas):
    print("\n--- CREAR SALA ---")
    try:
        cine = input("Ingrese el nombre del cine: ")
        numero = input("Ingrese el número de sala: ")
        asientos = int(input("Ingrese la cantidad de asientos: "))
        if not lista_salas.verificar_duplicado(numero):
            sala = Sala(cine, numero, asientos)
            lista_salas.agregar_sala(sala)
            print("*** Sala registrada con éxito")
        else:
            print("[ERROR-CS]: Ya existe una sala con el número ingresado")
    except:
        print("[ERROR-CS]: Ingresó un dato inválido")

def cargar_salas(lista_salas):
    print("\n--- CARGAR SALAS ---")
    lista_salas.cargar_salas()

def modificar_sala(lista_salas):
    print("\n--- MODIFICAR SALA ---")
    if lista_salas.get_tamanio() == 0:
        print("[ERROR-ES]: No hay salas disponibles")
    else:
        lista_salas.imprimir()
        try:
            id_sala = int(input("Ingrese el ID correspondiente a la sala a modificar: "))
            if lista_salas.verificar_id(id_sala):
                try:
                    print("--- Datos sala ---")
                    cine = input("Ingrese el nombre del cine al que pertenece la sala: ")
                    numero = input("Ingrese el número de sala: ")
                    asientos = int(input("Ingrese la cantidad de asientos: "))
                    if not lista_salas.verificar_duplicado(numero):
                        sala = Sala(cine, numero, asientos)
                        lista_salas.modificar_sala(id_sala, sala)
                        print("*** Sala modificada con éxito")
                    else:
                        print("[ERROR-MS]: Ya existe una sala con el número ingresado")
                except:
                    print("[ERROR-MS]: Ingresó un dato inválido")
            else:
                print("[ERROR-MS]: No existe una sala con el ID ingresado")
        except:
            print("[ERROR-MS]: Ingresó un ID inválido")

def eliminar_sala(lista_salas):
    print("\n--- ELIMINAR SALA ---")
    if lista_salas.get_tamanio() == 0:
        print("[ERROR-ES]: No hay salas disponibles")
    else:
        lista_salas.imprimir()
        try:
            id_sala = int(input("Ingrese el ID correspondiente a la sala a eliminar: "))
            if lista_salas.verificar_id(id_sala):
                lista_salas.eliminar_sala(id_sala)
                print("*** Sala eliminada con éxito")
            else:
                print("[ERROR-ES]: No existe una sala con el ID ingresado")
        except:
            print("[ERROR-ES]: Ingresó un ID inválido")

def guardar_salas(lista_salas):
    print("\n--- GUARDAR CAMBIOS ---")
    lista_salas.guardar_salas()

def registrar_usuario(lista_usuarios):
    print("\n--- REGISTRAR USUARIO ---")
    try:
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        telefono = int(input("Ingrese el teléfono: "))
        correo = input("Ingrese el correo: ")
        contrasena = input("Ingrese la contraseña: ")
        if not lista_usuarios.verificar_duplicado(telefono, correo):
            usuario = Usuario(nombre, apellido, telefono, correo, contrasena, "cliente")
            lista_usuarios.agregar_usuario(usuario)
            print("*** Usuario registrado con éxito")
    except:
        print("[ERROR-RU]: Ingresó un dato inválido")

def ver_peliculas(usuario_logeado, lista_peliculas):
    menuPeliculas = True
    while menuPeliculas:
        print("\n--- VER PELÍCULAS ---\n"
              "1 - Categoría\n"
              "2 - Listado general\n"
              "3 - Agregar película a favorito\n"
              "4 - Regresar")
        try:
            opcion = int(input("Ingrese el número correspondiente a la opción a realizar: "))
            if opcion == 1:
                if lista_peliculas.esta_vacia():
                    print("[ERROR-VP]: No hay películas disponibles")
                else:
                    print("\n--- Categorías ---")
                    for categoria in lista_peliculas.devolver_categorias():
                        print("*", categoria)
                    categoria_buscar = input("Ingrese la categoría a buscar: ")
                    lista_peliculas.imprimir_segun_categoria(categoria_buscar)
            elif opcion == 2:
                if lista_peliculas.esta_vacia():
                    print("[ERROR-VP]: No hay películas disponibles")
                else:
                    print("\n--- Películas ---")
                    lista_peliculas.imprimir_id_titulo()
                    id_pelicula = int(input("Ingrese el número de la película para ver los detalles: "))
                    lista_peliculas.imprimir_segun_id(id_pelicula)
            elif opcion == 3:
                if usuario_logeado == None:
                    print("[ERROR-VP]: Debe iniciar sesión para acceder a esta característica")
                else:
                    if not lista_peliculas.esta_vacia():
                        print("\n--- Películas ---")
                        lista_peliculas.imprimir_id_titulo()
                        try:
                            id_pelicula = int(input("Ingrese el número de la película para agregarla a favoritos: "))
                            pelicula_encontrada = lista_peliculas.devolver_pelicula(id_pelicula)
                            if pelicula_encontrada != None:
                                usuario_logeado.agregar_pelicula_favorita(pelicula_encontrada)
                            else:
                                print("[ERROR-APF]: No existe la película con ID ingresado")
                        except:
                            print("[ERROR-APF]: Ingresó una opción inválida")
                    else:
                        print("[ERROR-VP]: No hay películas disponibles")
            elif opcion == 4:
                menuPeliculas = False
            else:
                print("[ERROR-VP]: No existe la opción ingresada")
        except:
            print("[ERROR-VP]: Ingresó una opción inválida")

def ver_peliculas_favoritas(usuario_logeado):
    menu_peliculas_favoritas = True
    while menu_peliculas_favoritas:
        print("\n--- PELÍCULAS FAVORITAS ---\n"
              "1 - Ver favoritas\n"
              "2 - Eliminar de favoritas\n"
              "3 - Salir")
        try:
            opcion = int(input("Ingrese el número correspondiente a la acción a realizar: "))
            if opcion == 1:
                if len(usuario_logeado.get_peliculas_fav()) == 0:
                    print("[ERROR-VPF]: No se han agregado películas como favoritas")
                else:
                    print("\n--- VER PELÍCULAS FAVORITAS ---")
                    usuario_logeado.imprimir_peliculas_fav()
            elif opcion == 2:
                if len(usuario_logeado.get_peliculas_fav()) == 0:
                    print("[ERROR-EPF]: No se han agregado películas como favoritas")
                else:
                    print("\n--- ELIMINAR PELÍCULA DE FAVORITOS ---")
                    usuario_logeado.imprimir_peliculas_fav()
                    try:
                        id_pelicula = int(input("Ingrese el ID de la película a quitar de favoritos: "))
                        usuario_logeado.eliminar_pelicula_favorita(id_pelicula)
                    except:
                        print("[ERROR-EPF]: Ingresó una opción inválida")
            elif opcion == 3:
                menu_peliculas_favoritas = False
            else:
                print("[ERROR-VPF]: No existe la opción ingresada")
        except:
            print("[ERROR-VPF]: Ingresó una opción inválida")

def comprar_boletos(usuario_logeado, lista_peliculas, lista_salas, lista_facturas):
    menu_compra_boletos = True
    print("\n--- COMPRAR BOLETOS ---")
    if lista_peliculas.get_tamanio() == 0:
        print("[ERROR-CB]: No hay películas disponibles")
    else:
        print("\n--- Películas ---")
        lista_peliculas.imprimir()
        try:
            id_pelicula = int(input("Ingrese el ID de la película a seleccionar: "))
            pelicula_elegida = lista_peliculas.devolver_pelicula(id_pelicula)
            if pelicula_elegida != None:
                if lista_salas.get_tamanio() == 0:
                    print("[ERRRO-CB]: No hay salas disponibles")
                else:
                    print("\n--- Salas ---")
                    lista_salas.imprimir_info_estado()
                    id_sala = int(input("Ingrese el ID de la sala a seleccionar: "))
                    sala_elegida = lista_salas.devolver_sala(id_sala)
                    if sala_elegida != None:
                        if len(sala_elegida.get_asientos()) != 0:
                            print("\n--- Información de la película y sala ---\n"
                                  "PELÍCULA:", pelicula_elegida.get_titulo(), "| FECHA Y HORA:",
                                  pelicula_elegida.get_fecha(), pelicula_elegida.get_hora(),
                                  "\nCINE:", sala_elegida.get_cine(), "| SALA:", sala_elegida.get_numero(),
                                  "| ASIENTOS DISPONIBLES:", len(sala_elegida.get_asientos()))
                            cantidad_boletos = int(input("Ingrese la cantidad de boletos a comprar: "))
                            if cantidad_boletos < 1:
                                print("[ERROR-CB]: Ingresó una cantidad de boletos incorrecta")
                            elif cantidad_boletos > len(sala_elegida.get_asientos()):
                                print("[ERROR-CB]: Ingresó una cantidad de boletos que excede la capacidad de la sala")
                            else:
                                print("\n--- Asientos disponibles---")
                                cadena_asientos = ""
                                for asiento in range(sala_elegida.get_cantidad_asientos() + 1):
                                    if asiento in sala_elegida.get_asientos():
                                        cadena_asientos = cadena_asientos + "| " + str(asiento) + " |"
                                print(cadena_asientos)
                                numero_asientos = []
                                while len(numero_asientos) < cantidad_boletos:
                                    try:
                                        numero = int(input("Ingrese el número de asiento a elegir: "))
                                        if numero in sala_elegida.get_asientos():
                                            if numero not in numero_asientos:
                                                numero_asientos.append(numero)
                                            else:
                                                print(
                                                    "[ERROR-CB]: El número de asiento ingresado ya se ha seleccionado")
                                        else:
                                            print(
                                                "[ERROR-CB]: El número de asiento ingresado no se encuentra disponible")
                                    except:
                                        print("[ERROR-CB]: Ingresó una opción inválida")
                                print("*** Asientos elegidos:", numero_asientos)
                                while menu_compra_boletos:
                                    print("\n--- Datos de facturación ---\n"
                                          "1 - Ingresar información (nombre, nit, dirección)\n"
                                          "2 - Consumidor final (CF)\n"
                                          "3 - Cancelar compra de boletos")
                                    try:
                                        opcion = int(
                                            input("Ingrese el número correspondiente a la opción a realizar: "))
                                        if opcion == 1 or opcion == 2:
                                            nombre = "-"
                                            nit = "CF"
                                            direccion = "-"
                                            if opcion == 1:
                                                nombre = input("Ingrese el nombre del consumidor: ")
                                                nit = input("Ingrese el NIT del consumidor: ")
                                                direccion = input("Ingrese la dirección de domicilio: ")
                                            factura = Factura(usuario_logeado.get_correo(), usuario_logeado.get_telefono(), nombre, nit, direccion)
                                            lista_facturas.agregar_factura(factura)
                                            for asiento_elegido in numero_asientos:
                                                boleto = Boleto(pelicula_elegida.get_titulo(), pelicula_elegida.get_fecha(),
                                                                pelicula_elegida.get_hora(), sala_elegida.get_cine(),
                                                                sala_elegida.get_numero(), asiento_elegido)
                                                lista_facturas.agregar_boleto(factura, boleto)
                                            print("\n--- Resumen de la compra ---\n"
                                                  "Factura No.", factura.get_id(),
                                                  "\nNombre:", nombre, "NIT:", nit, "Dirección:", direccion)
                                            for boleto_comprado in factura.get_boletos():
                                                boleto_comprado.imprimir()
                                                sala_elegida.get_asientos().remove(boleto_comprado.get_asiento())
                                            print("Total: Q.", factura.get_total())
                                            print("*** Boletos comprados con éxito")
                                            menu_compra_boletos = False
                                        elif opcion == 3:
                                            menu_compra_boletos = False
                                            print("*** Compra de boletos cancelada")
                                        else:
                                            print("[ERROR-CBDF]: No existe la opción ingresada")
                                    except:
                                        print("[ERROR-CBDF]: Ingresó una opción inválida")
                        else:
                            print("[ERROR-CB]: La sala no cuenta con asientos disponibles")
                    else:
                        print("[ERROR-CB]: No existe una sala con el ID ingresado")
            else:
                print("[ERROR-CB]: No existe una película con el ID ingresado")
        except:
            print("[ERROR-CB]: Ingresó una opción inválida")

def historial_boletos(usuario_logeado, lista_facturas):
    print("\n--- HISTORIAL BOLETOS COMPRADOS ---")
    print("\n--- Facturas ---")
    if lista_facturas.imprimir_facturas_usuario(usuario_logeado.get_correo(), usuario_logeado.get_telefono()):
        try:
            id_factura = int(input("Ingrese el ID correspondiente a la factura para ver el detalle: "))
            print("\n--- Boletos ---")
            if not lista_facturas.verificar_id(id_factura):
                print("[ERROR-HB]: No existe una factura con el ID ingresado")
        except:
            print("[ERROR-HB]: Ingresó una opción inválida")
    else:
        print("[ERROR-HB]: El usuario no ha comprado boletos")

def gestionar_boletos(lista_facturas):
    menu_boletos = True
    while menu_boletos:
        print("\n--- GESTIONAR BOLETOS ---\n"
              "1 - Cancelar boleto\n"
              "2 - Activar boleto\n"
              "3 - Regresar")
        try:
            opcion = int(input("Ingrese la opción a realizar: "))
            if opcion == 1:
                print("\n--- Cancelar boleto ---")
                if lista_facturas.imprimir_boletos_estado("activo"):
                    try:
                        id_boleto = int(input("Ingrese el ID del boleto a cancelar: "))
                        if lista_facturas.verificar_cambio_estado_boleto(id_boleto, "cancelado"):
                            print("*** Boleto cancelado con éxito")
                        else:
                            print("[ERROR-GB]: No existe un boleto con el ID ingresado")
                    except:
                        print("[ERROR-GB]: Ingresó una opción inválida")
                else:
                    print("[ERROR-GB]: No hay boletos activos")
            elif opcion == 2:
                print("\n--- Activar boleto ---")
                if lista_facturas.imprimir_boletos_estado("cancelado"):
                    try:
                        id_boleto = int(input("Ingrese el ID del boleto a activar: "))
                        if lista_facturas.verificar_cambio_estado_boleto(id_boleto, "activo"):
                            print("*** Boleto activado con éxito")
                        else:
                            print("[ERROR-GB]: No existe un boleto con el ID ingresado")
                    except:
                        print("[ERROR-GB]: Ingresó una opción inválida")
                else:
                    print("[ERROR-GB]: No hay boletos cancelados")
            elif opcion == 3:
                menu_boletos = False
            else:
                print("[ERROR-GB]: La opción ingresada no existe")
        except:
            print("[ERROR-GB]: Ingresó una opción inválida")

if __name__ == '__main__':
    lista_usuarios = ListaUsuarios()
    lista_peliculas = ListaPeliculas()
    lista_salas = ListaSalas()
    lista_facturas = ListaFacturas()
    menu_principal(lista_usuarios, lista_peliculas, lista_salas, lista_facturas)