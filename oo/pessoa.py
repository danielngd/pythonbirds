class Pessoa:
    def __init__(self, nome=None, idade=35) -> None:
        self.idade = idade
        self.nome = None
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Luciano')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Daniel'
    print(p.nome)
    print(p.idade)