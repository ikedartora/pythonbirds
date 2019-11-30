class Pessoa:                                    # classe
    def __init__(self, nome=None, idade=35):     # atributos de instância, criados através de __init__
        self.idade = idade
        self.nome = nome                         # o método self.nome retorna o parâmetro nome (por default None)

    def cumprimentar(self):                      # método é uma 'função' atribuída a um classe
        return f'olá {id(self)}'
                                                # Atributo de dado, instância e objeto são a mesma coisa

if __name__ == '__main__':
    p = Pessoa("Henrique")
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Ike'
    print(p.nome)
    print(p.idade)