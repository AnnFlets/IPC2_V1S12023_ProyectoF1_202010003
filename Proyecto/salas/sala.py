class Sala:
    #Método constructor con parámetros
    def __init__(self, numero, asientos):
        self.numero = numero
        self.asientos = asientos

    #Métodos GET
    def get_numero(self):
        return self.numero

    def get_asientos(self):
        return self.asientos

    #Métodos SET
    def set_numero(self, numero):
        self.numero = numero

    def set_asientos(self, asientos):
        self.asientos = asientos