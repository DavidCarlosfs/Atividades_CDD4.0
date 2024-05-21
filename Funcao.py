class Pessoa():

    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.falando = False
        self.dormindo = False

    def comer(self, comida, bebida):
        if self.falando == True or self.dormindo == True:
            print(f"{self.nome} não pode comer, pois está ocupado")
        elif comida == "" and bebida != "":
            print(f"{self.nome} não está comendo, mas está bebendo {bebida}")
            self.comendo = True
        elif comida != "" and bebida == "":
            print(f"{self.nome} está comendo {comida}, mas não está bebendo")
            self.comendo = True
        else:
            print(f"{self.nome} foi comer {comida} e bebeu {bebida}")
            self.comendo = True

    def falar(self, frase):
        if self.comendo == True or self.dormindo == True:
            print(f"{self.nome} não pode falar, pois está ocupado")
        else:
            print(f"{self.nome} está dizendo '{frase}'")
            self.falando = True

    def dormir(self):
        if self.comendo == True or self.falando == True:
            print(f"{self.nome} não pode dormir, pois está ocupado")
        else:
            print(f"{self.nome} está dormindo")
            self.dormindo = True

    def pararcomando(self):
        if self.comendo == True:
            self.comendo = False
            print(f"{self.nome} parou ou terminou de comer")
        elif self.falando == True:
            self.falando = False
            print(f"{self.nome} se calou")
        else:
            self.dormindo = False
            print(f"{self.nome} acordou")