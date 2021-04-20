class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Old {id(self)}'


if __name__ == '__main__':  #dunder main
    akio = Pessoa(nome='Akio')
    alexandre = Pessoa(akio, nome='Alexandre')
    print(Pessoa.cumprimentar(alexandre))
    print(id(alexandre))
    print(alexandre.cumprimentar())
    print(alexandre.nome)
    print(alexandre.idade)
    for filho in alexandre.filhos:
        print(filho.nome)
    alexandre.sobrenome = 'Sonehara'
    del alexandre.filhos
    print(alexandre.__dict__)   #dunder dict
    print(akio.__dict__)