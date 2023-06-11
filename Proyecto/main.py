from usuario.persona import Persona

menuPrincipal = True
menuSecundario = True
opcionPrincipal = 0
opcionSecundaria = 0
opcionTerciaria = 0


while(menuPrincipal):
    print("*----- USAC-CINEMA -----*\n"
          "--- MENÚ PRINCIPAL ---\n"
          "1 - Iniciar sesión\n"
          "2 - Registrar usuario\n"
          "3 - Ver listado de películas\n"
          "4 - Salir")
    try:
        opcionPrincipal = int(input("Ingrese el número correspondiente a la opción a realizar:"))
        if opcionPrincipal == 1:
            print("\n- Iniciar sesión -")
            correo = input("Ingrese el correo electrónico:")
            contrasena = input("Ingrese la contraseña:")
            if correo == "admin" and contrasena == "admin":
                try:
                    while(menuSecundario):
                        print("--- MENÚ ADMINISTRADOR ---\n"
                              "1 - Gestionar usuarios\n"
                              "2 - Gestionar películas\n"
                              "3 - Gestionar salas\n"
                              "4 - Salir")
                        opcionSecundaria = int(input("Ingrese el número correspondiente a la opción a realizar:"))
                        if opcionSecundaria == 1:
                            print("- GESTIONAR USUARIOS -\n"
                                  "1 - Crear usuario\n"
                                  "2 - Leer usuarios\n"
                                  "3 - Modificar usuario\n"
                                  "4 - Eliminar usuario\n")
                            opcionTerciaria = int(input("Ingrese el número correspondiente a la opción a realizar:"))
                            if opcionTerciaria == 1:
                                print("- CREAR USUARIO -")
                            elif opcionTerciaria == 2:
                                print("- LEER USUARIOS -")
                            elif opcionTerciaria == 3:
                                print("- MODIFICAR USUARIO -")
                            elif opcionTerciaria == 4:
                                print("- ELIMINAR USUARIO -")
                except:
                    print("[ERROR-MA]: La opción ingresada no es válida\n")
            elif correo == "cliente" and contrasena == "cliente":
                print("--- MENÚ CLIENTE ---")
            else:
                print("[ERROR]: No existe el usuario")
        elif opcionPrincipal == 2:
            print("\n- REGISTRAR USUARIO -")
            try:
                nombre = input("Ingrese su nombre:")
                apellido = input("Ingrese su apellido:")
                telefono = int(input("Ingrese su teléfono:"))
                correo = input("Ingrese su correo:")
                contrasena = input("Ingrese su contraseña:")
                persona = Persona(nombre, apellido, telefono, correo, contrasena, "cliente")
                print("*** Datos del usuario registrado:")
                persona.imprimir()
            except:
                print("[ERROR-RU]: Ingresó un dato inválido\n")

        elif opcionPrincipal == 3:
            print("\n- Ver listado de películas -")
        elif opcionPrincipal == 4:
            print("\nSaliendo...")
            menuPrincipal = False
        else:
            print("[ERROR-MP]: No ingresó una opción existente\n")
    except:
        print("[ERROR-MP]: La opción ingresada no es válida\n")