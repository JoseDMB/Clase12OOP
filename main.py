"""class Persona:
    pass
#_Protegido
#__Privado
class Dog:

    def __init__(self, raza:str, color:str, duenio:Persona) ->None:
        self.__raza = raza #Este atributo es privado
        self.color = color
        self.duenio = duenio

    def __str__(self):
        return f"Yo soy un perro de raza, {self.__raza} y de color {self.color}"

    def __len__(self):
        return len(self.__raza)

    def __iter__(self):
        for ra in self.__raza:
            yield ra
    def ladrar(self)->str:
        if self.__raza == "doberman":
          return "ggggggg"
        return "woof"
    def caminar(self,cantidad_pasos):
        if cantidad_pasos > 100:
            return "ha caminado mucho"
        return "ha caminado menos de 100 pasos"

per = Persona()
dog_1 = Dog(raza="doberman", color="negro", duenio=per)




print(dog_1.__raza)
print(dog_1.color)
print(dog_1.ladrar())
print(dog_1.caminar(99))
print(len(dog_1))
print(iter(dog_1))
print(str(dog_1))"""

class alumno:

    def __init__(self, nombre:str, nota:float) -> None:
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"El estudiante {self.nombre} sacó como nota un {self.nota}")

    def resultado(self):
        if self.nota < 70:
            print(f"El resultado no es aprobado")
        else:
            print("El resultado ha sido aprobado!")

estudi = alumno("Juan", 67.9)

estudi.imprimir()
estudi.resultado()