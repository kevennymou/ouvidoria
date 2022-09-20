listaOcorrencias = []
listaSugestoes = []

isTrue = True


def linhas():
    print("-=" * 29)


class Usuario:
    matricula = 0
    nome = ""

    def _init_(self, mat, nome):
        self.matricula = mat
        self.nome = nome

        print("\nBem vindo %s\nSua matricula é: %d" % (self.nome, self.matricula))


class Reclamacao:
    valor = ""

    def _init_(self, v):
        self.valor = v

    def mostrarValor(self):
        return self.valor

    def alterarValor(self, v):
        self.valor = v


class Sugestoes:
    valor = ""

    def _init_(self, v):
        self.valor = v

    def mostrarValor(self):
        return self.valor

    def alterarValor(self, v):
        self.valor = v


def cadastraUsuario():
    nome = input("Digite seu nome: ")
    matricula = int(input("Digite sua matricula: "))

    Usuario(matricula, nome)


def menu():

    print("            \033[4;31mBEM VINDO AO SISTEMA DE OUVIDORIA!" "\033[m")
    cadastraUsuario()
    print()
    linhas()
    print()
    print("Menu do Sistema")
    print()
    print("Opções:")
    print()
    print("1-) Cadastrar Ocorrencias: ")
    print("2-) Listar Ocorrencias existentes: ")
    print("3-) Apagar Ocorrencias:  ")
    print("4-) Sugestoes: ")
    print("5-) Sair: ")
    print()
    linhas()


def titulo(sugestoes, ocorrencias):
    if titulo in ocorrencias:
        print("Cadastro de novas Ocorrencias: ")
        titulo = input("Cadastrar suas Ocorrencias: \n")
        listaOcorrencias.append(ocorrencias)
    elif titulo in sugestoes:
        print("Cadastro de novas Sugestoes: ")
        titulo = input("Cadastrar suas Sugestoes: \n ")
        listaSugestoes.append(sugestoes)


opc = 0
while opc != 5:
    menu()
    print()
    opc = int(input("Digite a Opção desejada: "))
    linhas()

    if opc == 1:
        print("Cadastre sua ocorrencias: ")
        rec = input("Digite sua nova reclamacao: ")
        listaOcorrencias.append(Reclamacao(rec))

    elif opc == 2:
        print("Listar de Ocorrências existentes ")
        for item in listaOcorrencias:
            print(item.mostrarValor())
        print("Lista de Sugestoes existentes ")
        for item in listaSugestoes:
            print(item.mostrarValor())
        print("Fim na lista de Ocorrência ")

    elif opc == 3:
        confirmacao = int(
            input("O que deseja apagar?\n 1 - Ocorrencias\n 2 - Sugestoes:\n")
        )
        if confirmacao == 1:
            print("Apagar Ocorrência")
            for item in listaOcorrencias:
                print("-" + item.mostrarValor())
            indice = int(input("Posição a ser apagada: "))
            listaOcorrencias.pop(indice - 1)
            print("Posicao apagada com sucesso!")
        elif confirmacao == 2:
            print("Apagar Sugestões")
            for item in listaSugestoes:
                print("-" + item.mostrarValor())
            indice = int(input("Posição a ser apagada: "))
            listaSugestoes.pop(indice - 1)
            print("Posicao apagada com sucesso! ")

    elif opc == 4:
        print("Sugestoes")
        escreva = input("Escrever sua sugestao: ")
        listaSugestoes.append(Sugestoes(escreva))
