from usuario import *
from carrinho import *
import json
import os

# Criação das Listas, dicionário e IDs iniciais
lista_usuarios = []
lista_produtos = []
estoque = {}
id_usuario = 0
id_mercadoria = 0

# Menu do programa
while True:
    print("MENU:\n")
    print("(1) Cadastrar Usuario")
    print("(2) Ver Usuarios")
    print("(3) Cadastrar Produtos")
    print("(4) Ver Produtos")
    print("(5) Vender")
    print("(6) Apagar Usuarios")
    print("(7) Apagar Produtos") 
    print("(0) Sair")
    resp = int(input("Selecione uma opção: "))
    os.system('cls')
    match resp:
        case 1:
            print("CADASTRO:\n")
            print("1. Pessoa Física\n2. Pessoa Jurídica\n3. Voltar")
            op = int(input("Selecione uma opção: "))
            print()
            arquivo = open('usuario.txt', 'a')

            if op == 1:
                email = input("Email: ")
                arquivo.write("Email: " + email + '\n')
                nome = input("Nome: ")
                arquivo.write("Nome: " + nome + '\n')
                idade = int(input("Idade: "))
                arquivo.write("Idade: " + str(idade) + '\n')
                cpf = input("CPF: ")
                arquivo.write("CPF: " + cpf + '\n')

                for usuarioExistente in lista_usuarios:
                    if cpf == usuarioExistente.get_doc():
                        print("\nCPF já registrado!")
                        break
                else:
                    cep = input("CEP: ")
                    arquivo.write("CEP: " + cep + '\n')

                    endereço = Endereço(cep)
                    carrinho = CarrinhoDeCompras()
                    id_usuario += 1
                    arquivo.write("id do usuario: " + str(id_usuario) + '\n')

                    usuario = PessoaFisica(
                        id_usuario, cpf, nome, idade, email, endereço, carrinho)
                    lista_usuarios.append(usuario)
                    print("Pessoa Física cadastrada com sucesso!")
                    print(f"ID = {usuario.get_id()}\n")
                    arquivo.close()
                    os.system("pause")
                    os.system('cls')

            elif op == 2:
                email = input("Email: ")
                arquivo.write("Email: " + email + '\n')
                nome = input("Nome: ")
                arquivo.write("Nome: " + nome + '\n')
                cnpj = input("CNPJ: ")
                arquivo.write("CNPJ: " + cnpj + '\n')
                arquivo.write("------------------------------------" + '\n')

                for usuarioExistente in lista_usuarios:
                    if cnpj == usuarioExistente.get_doc():
                        print("\nCNPJ já registrado!")
                        break
                else:
                    idade = 0
                    carrinho = CarrinhoDeCompras()
                    id_usuario += 1
                    arquivo.write("id do usuario: " + str(id_usuario) + '\n')

                    usuario = PessoaJuridica(
                        id_usuario, cnpj, nome, idade, email, carrinho)
                    lista_usuarios.append(usuario)

                    print("Pessoa Jurídica cadastrada com sucesso!")
                    print(f"ID = {usuario.get_id()}\n")
                    arquivo.close()
                    os.system("pause")
                    os.system('cls')
                    
            elif op == 3:
                os.system('cls')
                exit
            else:
                print("Opção inválida!")
                os.system('pause')
                os.system('cls')
                exit
                
        case 2:
            arquivo = open('usuario.txt', 'r')
            print(arquivo.readlines())
            arquivo.close()
            os.system("pause")
            os.system('cls')
            
        case 3:
            id_mercadoria += 1
            nome = input("Nome do produto: ")
            arquivo2 = open('produto.txt', 'a')
            arquivo2.write("Nome do produto: " + nome + '\n')

            quantidade = int(input("Quantidade: "))
            arquivo2.write("Quantidade: " + str(quantidade) + '\n')

            valor = float(input("Preço: "))
            arquivo2.write("Preço: " + str(valor) + '\n')

            produto = Mercadoria(id_mercadoria, nome, quantidade, valor)
            lista_produtos.append(produto)

            if nome not in estoque:
                estoque[nome] = quantidade
            else:
                print("Produto já registrado\n")
            arquivo2.close()
            os.system("pause")
            os.system('cls')
            
        case 4:
            arquivo2 = open('produto.txt', 'r')
            print(arquivo2.readlines())
            arquivo2.close()
            os.system("pause")
            os.system('cls')

        #    print("ESTOQUE:\n")
        #     for produto in estoque:
        #         for mercadoria in lista_produtos:
        #             if produto == mercadoria.get_nome():
        #                 print(
        #                     f"Produto: {produto} Preço: R$ {mercadoria.get_valor()} Quantidade: {estoque[produto]}")
        case 5:
            print("ESTOQUE:\n")
            for produto in estoque:
                for mercadoria in lista_produtos:
                    if produto == mercadoria.get_nome():
                        print(
                            f"ID = {mercadoria.get_id()} Produto = {produto} Preço = R$ {mercadoria.get_valor()} Quantidade = {estoque[produto]}")
            while True:
                id_produto = int(input(
                    "Digite o ID do produto que deseja comprar, caso contrário, digite '0' para sair da compra: "))
                if id_produto == 0:
                    os.system('cls')
                    break
                else:
                    for mercadoria in lista_produtos:
                        if id_produto == mercadoria.get_id():
                            quantidade = int(input(
                                f"Digite a quantidade de '{mercadoria.get_nome()}' que deseja mover para o carrinho: "))
                            usuario.carrinho.inserirProduto(
                                mercadoria, quantidade)
                print("Itens para compra:\n")
                usuario.carrinho.listarProdutos(
                    lista_produtos, usuario)
                op = input(
                    "Deseja efetuar a compra desses itens? [S/N]: ").upper()
                if op == 'S':
                    usuario.carrinho.realizarCompra(
                        lista_produtos, estoque)
                    os.system("pause")
                    os.system('cls')
                    break
                elif op == 'N':
                    os.system("pause")
                    os.system('cls')
                    break
                else:
                    print("Valor inválido\n")
                    os.system("pause")
                    os.system('cls')      
        
        case 6:
            arquivo = open("usuario.txt","w")
            arquivo.close()
            print("Usuarios apagados com sucesso!")
            os.system("pause")
            os.system('cls')
            
        case 7:
            arquivo2 = open("produto.txt","w")
            arquivo2.close()
            print("Produtos apagados com sucesso!")
            os.system("pause")
            os.system('cls')
            
        case 0:
            print("Finalizando programa...")
            os.system("pause")
            exit()
        
        case _:
            print("Opção inválida")
            os.system("pause")
            os.system('cls')
            exit
