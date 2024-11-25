class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido

    def hacer_sonido(self):
        return f"El {self.nombre} hace {self.sonido}."


class Gato(Animal):
    def __init__(self):
        super().__init__("gato", "miaaau")


class Perro(Animal):
    def __init__(self):
        super().__init__("perro", "¡guau, guau!")


class Huron(Animal):
    def __init__(self):
        super().__init__("hurón", "¡Eek Eek!")


class BoaConstrictor(Animal):
    def __init__(self):
        super().__init__("boa constrictor", "¡Tsss!")