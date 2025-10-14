from models.petshop import PetShop
from models.cliente import Cliente
from models.cachorro import Cachorro
from models.gato import Gato
from models.passaro import Passaro

def menu():
    print("\n=== PET SHOP SYSTEM ===")
    print("1. Cadastrar Animal")
    print("2. Cadastrar Cliente")
    print("3. Vender Animal")
    print("4. Listar Animais Disponíveis")
    print("5. Relatório de Vendas")
    print("6. Sair")

pet_shop = PetShop("Bichinhos & Cia")

while True:
    menu()
    opcao = input("Escolha: ")

    if opcao == "1":
        tipo = input("Tipo de animal (cachorro/gato/passaro): ").lower()
        nome = input("Nome do animal: ")
        idade = int(input("Idade: "))
        preco = float(input("Preço: R$ "))
        
        if tipo == "cachorro":
            animal = Cachorro(nome, idade, preco)
        elif tipo == "gato":
            animal = Gato(nome, idade, preco)
        elif tipo == "passaro":
            animal = Passaro(nome, idade, preco)
        else:
            print("Tipo inválido.")
            continue

        pet_shop.adicionar_animal(animal)
        print(f"{tipo.capitalize()} cadastrado com sucesso!")

    elif opcao == "2":
        nome = input("Nome do cliente: ")
        telefone = input("Telefone: ")
        cliente = Cliente(nome, telefone)
        pet_shop.cadastrar_cliente(cliente)
        print("Cliente cadastrado com sucesso!")

    elif opcao == "3":
        nome_animal = input("Nome do animal: ")
        nome_cliente = input("Nome do cliente: ")
        pet_shop.vender_animal(nome_animal, nome_cliente)

    elif opcao == "4":
        print("\n=== ANIMAIS DISPONÍVEIS ===")
        pet_shop.listar_animais_disponiveis()

    elif opcao == "5":
        pet_shop.relatorio_vendas()

    elif opcao == "6":
        print("Saindo do sistema. Até mais!")
        break

    else:
        print("Opção inválida. Tente novamente.")
