class Pessoa:                   # classe
    def cumprimentar(self):     # método é uma 'função' atribuída a um classe
        return f'olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(p.cumprimentar())
    print(id(p))
    print(Pessoa.cumprimentar(p))