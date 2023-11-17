class Pessoa:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.falando = False
        self.dormindo = False

    def comer(self):
        if self.comendo == True:
            print(f"{self.nome} já está comendo!")
        elif self.falando == True:
            print(f"{self.nome} não pode comer porque está falando!")
        elif self.dormindo == True:
            print(f"{self.nome} não pode comer porque está dormindo!")
        else:
            print(f"{self.nome} está comendo!")
            self.comendo = True

    def falar(self):
        if self.falando == True:
            print(f"{self.nome} já está falando!")
        elif self.comendo == True:
            print(f"{self.nome} não pode falar porque está comendo!")
        elif self.dormindo == True:
            print(f"{self.nome} não pode falar porque está dormindo!")
        else:
            print(f"{self.nome} está falando!")
            self.falando = True

    def dormir(self):
        if self.dormindo == True:
            print(f"{self.nome} já está dormindo!")
        elif self.falando == True:
            print(f"{self.nome} não pode dormir porque está falando!")
        elif self.comendo == True:
            print(f"{self.nome} não pode dormir porque está comendo!")
        else:
            print(f"{self.nome} Lali!")
            self.dormindo = True

    def apresenta(self):
        print(f" Meu nome é {self.nome}, estou pesando {self.peso}Kg e tenho {self.idade} anos!")

    def pararDeComer(self):
        self.comendo = False
        print(f"{self.nome} Parou de Comer!")

    def acordar(self):
        self.dormindo = False
        print(f"{self.nome}Acordou!")

    def pararDeFalar(self):
        self.falando = False
        print(f"{self.nome} Parou de falar!")