class Pessoa:                                    # classe
    olhos = 2       # atributos de classe, ocupa só 1 espaço na memória diferente dos de instância (1 para cada objeto criado)
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
    luciano.sobrenome = 'Ramalho'       #atributo dinâmico criado em tempo de execução
    del luciano.filhos                  # atribtuto dinâmico deletado em tempo de execução
    print(luciano.__dict__)     #__dict__ mostra quais são os atributos de instância de um objeto
    print(renzo.__dict__)
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))  #atributo de classe é o mesmo, ocupa só 1 espaço na memória