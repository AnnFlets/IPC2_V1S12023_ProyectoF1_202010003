#Librería utilizada para la lectura del archivo XML
import xml.dom.minidom as MD
#Librería utilizada para la escritura del archivo XML
import xml.etree.cElementTree as ET

class ListaUsuarios:
    #Método constructor con parámetro
    def __init__(self, cabeza):
        self.cabeza = cabeza

    #Método para leer XML de usuarios y guardar los datos en la lista


    #Método GET
    def get_cabeza(self):
        return self.cabeza

    #Método SET
    def set_cabeza(self, cabeza):
        self.cabeza = cabeza