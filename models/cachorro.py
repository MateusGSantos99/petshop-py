from models.animal import Animal

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

    def latir(self):
        return "Latindo feliz!"
