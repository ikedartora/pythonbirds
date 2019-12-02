class Pessoa:                                    # classe
    def __init__(self, *filhos, nome=None, idade=35):     # atributos de instância, criados através de __init__  Atributo de dado, de instância e objeto são a mesma coisa
        self.idade = idade
        self.nome = nome                         # o método self.nome retorna o parâmetro nome (por default None)
        self.filhos = list(filhos)
    def cumprimentar(self):                      # método é uma 'função' atribuída a um classe, repare a diferença entre os atributos criados com init e sem, som init precisa de ()
        return f'olá {id(self)}'


if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    eu = Pessoa(nome='Eu')
    luciano = Pessoa(renzo, eu, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'
    del luciano.filhos
    print(luciano.__dict__)
    print(renzo.__dict__)