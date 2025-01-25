# criando uma classe


class Pilha:
    """Permite a criação de uma pilha"""
    def __init__(self):
        self.itens = []

    def __repr__(self):
        return str(self.itens)

    def empilha(self, valor):
        # adiciona itens a pilha
        self.itens.append(valor)

    def desempilha(self):
        assert self.itens, "Erro: pilha vazia!"

        """ modifica o valor do topo"""
        return self.itens.pop()

    def busca(self, alvo):
        """ busca por uma alvo na pilha"""

        return alvo in self.itens


def main():

    # cria um novo objeto do tipo Pilha
    familia = Pilha()

    # adiciona membros da família
    familia.empilha("Miguel Silva de Castro")
    familia.empilha("José de Castro")
    familia.empilha("Eugênio de Castro")
    familia.empilha("Pedro Paulo de Castro")

    # sabemos que são primos, mas queremos testar se o sistema os encontram
    nome = input('Digite o seu nome: ')
    alvo = "Miguel Silva de Castro"
    # parentes = familia.busca(nome)

    if familia.busca(nome):
        print(f"{nome} é parentes de {alvo}!")
    else:
        print(f"{nome} não é parentes de {alvo}!")


if __name__ == "__main__":
    main()
