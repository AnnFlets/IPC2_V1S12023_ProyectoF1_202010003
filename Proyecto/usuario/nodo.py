from persona import Persona

class NodoUsuarios:

    def __init__(self, usuario, siguiente):
        self.usuario = usuario
        self.siguiente = siguiente

    #Métodos GET
    def get_nombre_usuario(self):
        return self.usuario.get_nombre

    def get_apellido_usuario(self):
        return self.usuario.get_apellido

    def get_telefono_usuario(self):
        return self.usuario.get_telefono

    def get_correo_usuario(self):
        return self.usuario.get_correo

    def get_contrasena_usuario(self):
        return self.usuario.get_contrasena

    def get_rol_usuario(self):
        return self.usuario.get_rol

    #Métodos SET
    def set_nombre_usuario(self, nombre):
        self.usuario.set_nombre(nombre)

    def set_apellido_usuario(self, apellido):
        self.usuario.set_apellido(apellido)

    def set_telefono_usuario(self, telefono):
        self.usuario.set_telefono(telefono)

    def set_correo_usuario(self, correo):
        self.usuario.set_correo(correo)

    def set_contrasena_usuario(self, contrasena):
        self.usuario.set_contrasena(contrasena)

    def set_rol_usuario(self, rol):
        self.usuario.set_rol(rol)