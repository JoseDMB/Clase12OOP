class Animal():

    def __init__(self, cantidad_ojos: int, tipo_piel: str) -> None:
        self.cantidad_ojos = cantidad_ojos
        self.tipo_piel = tipo_piel

    def respirar(self) -> int:#cantidad de veces que respira por minuto
        return 30

#
    def correr(self) ->str:

        return "Corre normal"

    def moverse(self):
        ...

class Mamifero:
    def respirar(self)->str:
        return "estamos respirando por la nariz"

