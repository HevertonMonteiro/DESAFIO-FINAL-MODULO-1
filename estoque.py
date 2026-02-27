# 2.Sistema de Controle de Estoque para Loja

'''1.Criar um sistema para cadastrar produtos, controlar estoque (entradas/saídas), buscar produtos e 
listar produtos em falta. Organização em modelo/controle/interface e menu interativo.'''

# Deve conter (mínimo obrigatório)

# ✔ Classe Produto com atributos (nome, código, preço, quantidade) — quantidade encapsulada
# ✔ Getters/setters ou @property para acessar/alterar quantidade com validação (não negativa)
# ✔ Métodos adicionar_estoque(qtd) e remover_estoque(qtd) que atualizam evalidam estoque
# ✔ Lista de produtos cadastrados e consulta por nome
# ✔ Menu interativo para: cadastrar produto, atualiza estoque (entrada/saída), listar todos, listar produtos com estoque baixo, remover produto



class Produtos:
    def __init__ (self, nome, codigo, preco, quantidade):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.__quantidade = quantidade

    def __str__(self):
        return (
            f"Nome: {self.nome} | "
            f"Código: {self.codigo} | "
            f"Preço: R$ {self.preco} | "
            f"Quantidade: {self.__quantidade}"
        )    

    def get_quantidade(self): #Criado para conseguir acessar a quantidade tendo em vista que ela é privada
        return self.__quantidade
    
    def set_quantidade(self, nova_quantidade): #Criado para conseguir acessar a quantidade tendo em vista que ela é privada
        if nova_quantidade >= 0:
            self.__quantidade = nova_quantidade
        else:
            print("Erro a quantidade tem que ser maior que zero! ")

    def adicionar_quantidade(self, valor):
        if valor >= 0:
            self.__quantidade += valor
        else:
            print("Quantidade Invalida. ")

    def remover_quantidade(self, valor):
        if valor > 0 and valor <= self.__quantidade:
            self.__quantidade -= valor
            return True
        else:
            print(
                f"Quantidade maior que o estoque disponível "
                f"\nEstoque disponivel de:({self.get_quantidade()}) Unidades."
            )
            return False
                
    def alterar_quantidade(self, valor):
        nova_quantidade = self.__quantidade + valor

        if nova_quantidade >= 0:
            self.__quantidade = nova_quantidade

        else:
            print('Quantidade Invalida. ')


produtos = []

#Função criada para realização de cadastro do produto, utilizando o tratamento de erro
def cadastrar_produto():
    try:
        nome = input("Digite o nome do produto: ").upper()
        for p in produtos:
            if p.nome == nome:
                print("Já existe um produto com esse nome.")
                return    
        codigo = int(input("Digite o codigo do produto: "))
        for p in produtos:
            if p.codigo == codigo:
                print("Já existe um produto com esse código.")
                return
        preco_input = input("Digite o preço do produto: ").replace(',', '.') #Utilizei o replace para caso o usuario utilize a pontução incorreta na hora do preencheminte do preco o codigo nao quebre
        preco = float(preco_input)
        quantidade = int(input("Digite o quantidade do produto: "))

        produto = Produtos (nome, codigo, preco, quantidade)
        produtos.append(produto)

        print("Produtos cadastrado com sucesso")

    except ValueError:
        print("Erro: digite valores numéricos válidos para código, preço e quantidade.")

#Para buca de possiveis itens com estoque baixo usei condicoes boleanas para conseguir indentificar se existe ou nao
def estoque_baixo():
    estoque_insuficiente = 5
    encontrou = False

    for produto in produtos:
        if produto.get_quantidade() <= estoque_insuficiente:
            print(produto)
            encontrou = True
    if not encontrou:
        print("Não há produtos com esroque baixo")
            
#Para saber se existe o item usei condicoes boleanas para conseguir indentificar se existe ou nao            
def buscar_por_nome():
    termo = input("Digite o nome do produto: ").strip().lower() #ultilizei o .strip para buscar por semelhança e o .lower para converter independente de ser maiusculo ou nao
    encontrou = False

    for produto in produtos:
        if termo in produto.nome.lower():
            print("--- PRODUTO ENCONTRADO ---")
            print(produto)
            encontrou = True

    if not encontrou:
        print("Nenhum produto encontrado com esse nome.")

def listar_tudo():
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
    else:
        print("\n--- LISTA DE PRODUTOS ---")
        for produto in produtos:
            print(produto)

def dar_entrada():
    codigo = int(input("Digite o código do produto: "))
    quantidade = int(input("Digite a quantidade de entrada: "))

    for produto in produtos:
        if produto.codigo == codigo:
            produto.adicionar_quantidade(quantidade)
            print(
                f"\nEntrada realizada com sucesso! "
                f"\nO estoque de {produto.nome} agora é {produto.get_quantidade()}"
            )
            return

    print("Produto não encontrado.")

def dar_saida():
    codigo = int(input("Digite o código do produto: "))
    quantidade = int(input("Digite a quantidade de saída: "))

    for produto in produtos:
        if produto.codigo == codigo:
            if produto.remover_quantidade(quantidade):
                print(
                    f"Saída realizada com sucesso! "
                    f"O estoque de {produto.nome} agora é {produto.get_quantidade()}"
                )
            return

    print("Produto não encontrado.")

def remover_produto():
    codigo = int(input("Qual o codigo do produto a remover? "))
    for produto in produtos:
        if produto.codigo == codigo:
            produtos.remove(produto)
            print("Produto removido com sucesso! ")
            return
    
    print("Não existe esse produto no estoque! ")

def produto_zerado():
    encontrado = False
    
    for zerados in produtos:
        if zerados.get_quantidade() == 0:
            print(f"O produto {zerados.nome} está zerado") 
            encontrado = True

    if not encontrado:
            print("Não existe nenhum produto zerado! ")

while True:

    try:
        print('\n============MENU============\n')
        menu = int(input('Digite um numero de 1 a 9'    
        '\n1 - Cadastrar Produto ' 
        '\n2 - Dar Entrada ' 
        '\n3 - Dar Saida ' 
        '\n4 - Buscar Por Nome ' 
        '\n5 - Listar Produtos '
        '\n6 - Estoque Baixo '
        '\n7 - Remover Produto '
        '\n8 - Estoque Zerado '
        '\n9 - Sair \n'))

        if menu == 1:
            cadastrar_produto()
        elif menu == 2:
            dar_entrada()
        elif menu == 3:
            dar_saida()
        elif menu == 4:
            buscar_por_nome()
        elif menu == 5:
            listar_tudo()
        elif menu == 6:
            estoque_baixo()
        elif menu == 7:
            remover_produto()
        elif menu == 8:
            produto_zerado()    
        elif menu == 9:
            break
        else:
            print("Opção inválida. Digite um número de 1 a 9.")
    except ValueError:
            print("Digite uma opção de 1 a 9")
            continue
    
   