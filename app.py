# import da biblioteca os
import os

# Lista de dicionarios representando os restaurantes
restaurantes = [{'nome': 'Praça','categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Pizza Suprema','categoria': 'Pizza', 'ativo': True},
                {'nome': 'Cantina','categoria': 'Italiano', 'ativo': False}]

def exibir_nome_do_programa():
    print("""
          🅢🅐🅑🅞🅡 🅔🅧🅟🅡🅔🅢🅢
          """)
   
def exibir_opcoes():
    print('1. Cadastrar restaurantes')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurantes')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app\n')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls') #limpa a tela (funciona apenas no Windows)
    linha = '*' * (len(texto))
    print (linha)
    print (texto)
    print (linha)
    print ()
   
def main():
    """
    Funçao principal que inincial o programa
    """
    os.system('cls') #Limpa a tela (Funciona apenas no Windows)
    exibir_nome_do_programa()
    exibir_opcoes()
    # escolher_opcao()

if __name__=='__main__':
   main()