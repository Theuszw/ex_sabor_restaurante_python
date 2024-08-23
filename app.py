import os
import json
import sys
from modelos.restaurante import Restaurante
from modelos.avaliacao import Avaliacao

def get_data_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))
   
ARQUIVO_DADOS = os.path.join(get_data_dir(), 'dados_restaurante.json')

def carregar_dados():
    try:
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            Restaurante.restaurantes.clear()
            for restaurante_dados in dados:
                restaurante = Restaurante (
                    restaurante_dados ['nome'],
                    restaurante_dados['categoria']
                )
                restaurante._ativo = restaurante_dados['ativo']
                restaurante._avaliacao = [Avaliacao(**avaliacao) for avaliacao in restaurante_dados
                ['avaliacao']]
    except FileNotFoundError:
        print(f"Arquivo de dados não encontrado. Criando um novo arquivo em {ARQUIVO_DADOS}")
        salvar_dados()

def salvar_dados():
    dados = []
    for restaurante in Restaurante.restaurantes:
        dados.append({
            'nome': restaurante._nome,
            'categoria': restaurante._categoria,
            'ativo': restaurante._ativo,
            'avaliacao': [avaliacao.__dict__() for avaliacao in restaurante._avaliacao]
        })
    with open (ARQUIVO_DADOS, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def main():
    carregar_dados()
   
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=-=-=-=-= Restaurante Expresso =-=-=-=-=")
        print("\n1. Cadastrar restaurante")
        print("2. Listar restaurantes")
        print("3. Habilitar restaurante")
        print("4. Avaliar restaurante")
        print("5. Alterar restaurante")
        print("6. Excluir restaurante")
        print("7. Sair")

        opcao = input("\nEscolha uma opção: ")

       
        if opcao == '1':
            cadastrar_restaurante()
        elif opcao == '2':
            listar_restaurante()
        elif opcao == '3':
            habilitar_restaurante()
        elif opcao == '4':
            avaliar_restaurante()
        elif opcao == '5':
            alterar_restaurante()
        elif opcao == '6':
            excluir_restaurante()
        elif opcao == '7':
            salvar_dados()
            print("\nDados salvos. Obrigado por usar o sistema. Até logol")
            break
        else:
            print("Opção inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")

def cadastrar_restaurante():
    nome = input("Digite o nome do restaurante: ")
    categoria = input("Digite a categoria do restaurante: ")
    novo_restaurante = Restaurante (nome, categoria)
    print(f"\nRestaurante {nome} cadastrado com sucesso!")
    salvar_dados ()

def listar_restaurante():
    print("Lista de Restaurantes:")
    Restaurante.listar_restaurantes()

def habilitar_restaurante():
    nome = input("Digite o nome do restaurante que deseja habilitar/desabilitar: ")
    for restaurante in Restaurante.restaurantes:
        if restaurante._nome.lower() == nome.lower():
            restaurante.alternar_estado()
            print(f"Estado do restaurante {restaurante._nome} alterado para {restaurante.ativo}")
            salvar_dados()
            return
    print("Restaurante não encontrado.")

def avaliar_restaurante():
    nome = input("Digite o nome do restaurante que deseja avaliar: ")
    for restaurante in Restaurante.restaurantes:
        if restaurante._nome.lower() == nome.lower():
            cliente = input("Digite seu nome: ")
            while True:
                try:
                    nota = float(input("Digite a nota (de 0 a 10): "))
                    if 0 <= nota <= 10:
                        restaurante.receber_avaliacao(cliente, nota)
                        print(f"Avaliação de realizada com sucesso!")
                        salvar_dados()
                        return
                    else:
                        print("A nota deve estar entre 0 e 10.")
                except ValueError:
                    print("Por favor, digite um número válido.")

    print("Restaurante não encontrado.")

def alterar_restaurante():
    nome = input("Digite o nome do restaurante que deseja alterar: ")
    for restaurante in Restaurante.restaurantes:
        if restaurante._nome.lower() == nome.lower():
            novo_nome = input(f"Digite o novo nome do restaurante (atual: (restaurante._nome)): ")
            nova_categoria = input(f"Digite a nova categoria do restaurante (atual: (restaurante._categoria)): ")

        if novo_nome:
            restaurante._nome = novo_nome.title()
        if nova_categoria:
            restaurante._categoria = nova_categoria.upper()

        print(f"Restaurante alterado com sucesso para: {restaurante}")
        salvar_dados()
        return
    print("Restaurante não encontrado.")

def excluir_restaurante():
    nome = input("Digite o nome do restaurante que deseja excluir: ")
    for restaurante in Restaurante.restaurantes:
        if restaurante._nome.lower() == nome.lower():
            confirmacao = input(f"Tem certeza que deseja excluir o restaurante '(restaurante._nome)'? (S/N): ")
            if confirmacao.lower() == 's':
                Restaurante.restaurantes.remove(restaurante)
                print(f"Restaurante '{restaurante._nome}' excluído com sucesso!")
                salvar_dados()
            else:
                print("Operação de exclusão cancelada.")
            return
    print("Restaurante não encontrado.")

if __name__ == '__main__':
    main()