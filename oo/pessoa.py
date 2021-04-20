class Pessoa:
    # atributo de classe
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        # atributos de instância
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Old {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


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
    alexandre.olhos = 1
    del alexandre.olhos
    print(akio.__dict__)
    print(alexandre.__dict__)  #dunder dict
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(alexandre.olhos)
    print(akio.olhos)
    print(id(Pessoa.olhos), id(alexandre.olhos), id(akio.olhos))
    print(Pessoa.nome_e_atributos_de_classe(), alexandre.nome_e_atributos_de_classe())