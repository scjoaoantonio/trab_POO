# Classe do Produto (Mercadoria)
class Mercadoria():
    def __init__(self, id, nome, quantidade, valor):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor

    # Reduz a quantidade de produtos na classe
    def reproduzirProduto(self, quantidade):
        self.quantidade -= quantidade

    # Imprime os dados do produto
    def mostrarDados(self):
        print("ID = {} Nome = {} Quantidade = {} Valor = R$ {}" .format(
            self.id, self.nome, self.quantidade, self.valor))

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_valor(self):
        return self.valor

    def get_quantidade(self):
        return self.quantidade


# Sistema do Carrinho de compras
class CarrinhoDeCompras():
    def __init__(self):
        self.produtos = {}

    # Insere produtos no carrinho
    def inserirProduto(self, mercadoria, quantidade):
        if mercadoria.get_nome() not in self.produtos:
            self.produtos[mercadoria.get_nome()] = quantidade
        else:
            self.produtos[mercadoria.get_nome()] += quantidade

    # Mostra os produtos do carrinho de compras
    def listarProdutos(self, lista_produtos, usuario):
        if len(self.produtos) == 0:
            print("Carrinho vazio\n")
        else:
            for produto in self.produtos:
                for mercadoria in lista_produtos:
                    if produto == mercadoria.get_nome():
                        print(
                            f"ID = {mercadoria.get_id()} {produto} =  R$ {mercadoria.get_valor()} Quantidade = {self.produtos[produto]}")
                        soma = usuario.carrinho.soma_total(lista_produtos)
            print(f"Soma total dos preços = R$ {soma}\n")

    # Faz a soma de preços dos produtos do carrinho
    def soma_total(self, lista_produtos):
        soma = 0
        for produto in self.produtos:
            for mercadoria in lista_produtos:
                if produto == mercadoria.get_nome():
                    quantidade = self.produtos[produto]
                    preço = mercadoria.get_valor()
                    soma += (preço*quantidade)
        return soma

    # Realiza a compra
    def realizarCompra(self, lista_produtos, estoque):
        flag = 0
        for produto in self.produtos:
            for mercadoria in lista_produtos:
                for mercadoria_est in estoque:
                    if produto == mercadoria.get_nome() and produto == mercadoria_est:
                        if self.produtos[produto] > estoque[mercadoria_est]:
                            print("Quantidade não existente no estoque! ")
                            print("Você deve retirar produto do seu carrinho!\n")
                        else:
                            flag = 1
                            # mercadoria.reduzirProduto(self.produtos[produto])
                            # estoque[mercadoria_est] -= (self.produtos[produto])
                            pass
        if flag == 1:
            self.produtos = {}
            print("Compra realizada com sucesso.\n")
