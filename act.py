carro = input("Nombre carro: ")
modelo = input("Modelo carro: ")

class Mascota(object):
    def __init__(self, carro, modelo):
        self.carro = carro
        self.modelo = modelo

    def darNombre(self):
        return self.carro
    
    def darEspecie(self):
        return self.modelo
    
    def __str__(self):
        return "%s es un %s" % (self.carro, self.modelo)

print (Total(carro, modelo))
