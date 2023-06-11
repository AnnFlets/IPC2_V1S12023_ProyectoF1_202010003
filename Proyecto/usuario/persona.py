class Persona:
    #Método constructor con parámetros
    def __init__(self, nombre, apellido, telefono, correo, contrasena, rol):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.contrasena = contrasena
        self.rol = rol

    #Métodos GET
    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_telefono(self):
        return self.telefono

    def get_correo(self):
        return self.correo

    def get_contrasena(self):
        return self.contrasena

    def get_rol(self):
        return self.rol

    #Métodos SET
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_telefono(self, telefono):
        self.telefono = telefono

    def set_correo(self, correo):
        self.correo = correo

    def set_contrasena(self, contrasena):
        self.contrasena = contrasena

    def set_rol(self, rol):
        self.rol = rol

    #Método para imprimir la información de la persona
    def imprimir(self):
        print("- Nombre: " + str(self.nombre) +
              "\n- Apellido: " + str(self.apellido) +
              "\n- Teléfono: " + str(self.telefono) +
              "\n- Correo: " + str(self.correo) +
              "\n- Contraseña: " + str(self.contrasena) + "\n")