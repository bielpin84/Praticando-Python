import os

restaurantes = [
      {"nome": "Zen Sushi", "categoria": "Japonesa", "ativo": False},
      {"nome": "Mama Mia", "categoria": "Italiana", "ativo": True},
      {"nome": "Na Real", "categoria": "Brasileira", "ativo": False}
]

def exibir_nome_do_programa():
    """Essa função exibe o nome do programa na tela"""
    # Título retirado de fsymbols.com
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)

def exibir_opcoes():
      """Essa função exibe as opções do menu principal"""
      print("Menu Principal - Escolha uma opção:\n")
      print("1. Cadastrar um Novo Restaurante")
      print("2. Exibir a Lista de Restaurantes")
      print("3. Alternar Estado do Restaurante")
      print("4. Sair do Programa\n")

def finalizar_app():
    """Essa função finaliza o aplicativo"""
    exibir_subtitulo("Finalizando o aplicativo.")

def opcao_invalida():
      """Essa função trata opções inválidas inseridas no menu
      e retorna ao menu principal
      """
      print("Opção inválida. Por favor, escolha uma opção válida.\n")
      voltar_ao_menu_principal()

def limpar_tela():
      """Essa função limpa a tela do console"""
      os.system("cls")

def exibir_subtitulo(subtitulo):
      """Essa função limpa a tela e exibe um subtítulo
      
      Parâmetros:
      - subtitulo: string contendo o subtítulo a ser exibido
      
      Outputs:
      - Tela limpa através do comando 'cls'
      - Subtítulo recebido por parâmetro exibido na tela
      - Linha de separação antes e depois do subtítulo
      
      """
      limpar_tela()
      linha_de_separacao = "-" * len(subtitulo)
      print(linha_de_separacao)
      print(f"{subtitulo}")
      print(linha_de_separacao)
      print()

def voltar_ao_menu_principal():
      """Essa função aguarda o usuário pressionar uma tecla para voltar ao menu principal
      
      Inputs:
      - Tecla pressionada pelo usuário
      
      Outputs:
      - Retorna ao menu principal após o usuário pressionar uma tecla

      """
      input("\nDigite uma tecla para voltar ao menu ")
      main()

def cadastrar_novo_restaurante():
      """Essa função é responsável por cadastrar um novo restaurante
      
      Inputs:
      - Nome do restaurante
      - Categoria do restaurante

      Outputs:
      - Limpa a tela e exibe um subtítulo
      - Solicita o nome e a categoria do restaurante ao usuário
      - Adiciona um novo restaurante à lista de restaurantes
      - Mensagem de sucesso após o cadastro
      - Retorna ao menu principal após o cadastro

      """
      exibir_subtitulo("Cadastro de Novo Restaurante")
      nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
      categoria_restaurante = input(f"Digite a categoria do restaurante {nome_restaurante}: ")
      dados_do_restaurante = {
            "nome": nome_restaurante,
            "categoria": categoria_restaurante,
            "ativo": False
      }
      restaurantes.append(dados_do_restaurante)
      print(f"\nRestaurante '{nome_restaurante}' cadastrado com sucesso!\n")
      voltar_ao_menu_principal()
      
def listar_restaurantes():
      """Essa função exibe a lista de restaurantes cadastrados
      
      Outputs:
      - Limpa a tela e exibe um subtítulo
      - Verifica se há restaurantes cadastrados
      - Lista formatada de restaurantes com nome, categoria e estado (ativo/inativo)
      - Retorna ao menu principal após exibir a lista
      
      """
      exibir_subtitulo("Lista de Restaurantes Cadastrados:")
      if len(restaurantes) == 0:
            print("Nenhum restaurante cadastrado.\n")
            voltar_ao_menu_principal()
      else:
            print(f"{'Nome'.ljust(20)} | {'Categoria'.ljust(20)} | {'Estado'}")
            print("-" * 60)
            for restaurante in restaurantes:
                  nome_restaurante = restaurante["nome"]
                  categoria_restaurante = restaurante["categoria"]
                  ativo_restaurante = "Ativo" if restaurante["ativo"] else "Inativo"
                  print(f"{nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}")
            voltar_ao_menu_principal()

def alternar_estado_restaurante():
      """Essa função alterna o estado de um restaurante entre ativo e inativo
      
      Inputs:
      - Nome do restaurante a ser alterado

      Outputs:
      - Limpa a tela e exibe um subtítulo
      - Verifica se o restaurante existe na lista
      - Altera o estado do restaurante e exibe o novo estado
      - Mensagem de erro se o restaurante não for encontrado
      - Retorna ao menu principal após a alteração

      """
      exibir_subtitulo("Alterando Estado do Restaurante")
      nome_restaurante = input("Digite o nome do restaurante que deseja ativar/inativar: ")
      restaurante_encontrado = False
      for restaurante in restaurantes:
            if restaurante["nome"].lower() == nome_restaurante.lower():
                  restaurante_encontrado = True
                  restaurante["ativo"] = not restaurante["ativo"]
                  estado_atual = "Ativo" if restaurante["ativo"] else "Inativo"
                  print(f"\nO restaurante '{restaurante['nome']}' agora está {estado_atual}.\n")
                  break
      if not restaurante_encontrado:
            print(f"\nRestaurante '{nome_restaurante}' não encontrado.\n")
      voltar_ao_menu_principal()

def escolher_opcao():
      """Essa função permite ao usuário escolher uma opção do menu
      
      Inputs:
      - Opção escolhida pelo usuário

      Outputs:
      - Executa a função correspondente à opção escolhida
      - Trata opções inválidas com mensagem de erro
      
      """
      try:
            opcao_escolhida = int(input("Escolha uma opção: "))

            match opcao_escolhida:
                  case 1:
                        cadastrar_novo_restaurante()
                  case 2:
                        listar_restaurantes()
                  case 3:
                        alternar_estado_restaurante()
                  case 4:
                        finalizar_app()
                  case _:
                        opcao_invalida()
      except:
            opcao_invalida()

def main():
    """Essa é a função principal do aplicativo, responsável por iniciar o programa e exibir o menu
    
    Outputs:
    - Limpa a tela
    - Exibe o nome do programa
    - Exibe as opções do menu principal
    - Permite ao usuário escolher uma opção
    
    """
    limpar_tela()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    """Essa condição verifica se o script está sendo executado diretamente"""
    main()