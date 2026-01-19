import json
import os

arquivo = "agenda.json"

def carregar_dados(): 
    if os.path.exists(arquivo):
        with open(arquivo, "r") as f:
            return json.load(f) # Retorna o texto do JSON em objeto do python
    return {} # Retorna dicionário vazio se o arquivo não existir

def salvar_dados(agenda):
    with open(arquivo, "w") as f:
        json.dump(agenda, f, indent=4) # Retorna o objeto e despeja no JSON

def validar_telefone(tel): 
    return 8 <= len(tel) <= 11 and tel.isdigit()

agenda = carregar_dados()

try:
    while True:
        print("\n--- AGENDA TELEFÔNICA ---")
        print("1. Adicionar/Atualizar Contato")
        print("2. Remover Contato")
        print("3. Listar Contatos")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        # Corrigido: Comparando com string "1"
        if opcao == "1": 
            nome = input("Nome: ")
            descricao = input("Informação do Contato ('0' caso não tenha): ")
            telefone = input("Telefone (Apenas números): ")

            if validar_telefone(telefone):
                # Salvando telefone e descrição como um par
                agenda[nome] = {"telefone": telefone, "descricao": descricao}
                salvar_dados(agenda)
                print(f"Contato {nome} salvo com sucesso!")
            else:
                print("Erro: Telefone inválido (deve ter entre 8 e 11 dígitos numéricos).")

        elif opcao == "2":
            nome = input("Nome do contato para remover: ")
            if nome in agenda:
                agenda.pop(nome) # Uma das forma de remover item, a outra é o del "del agenda[nome]"
                salvar_dados(agenda)
                print(f"Contato {nome} removido.")
            else:
                print("Contato não encontrado.")

        elif opcao == "3":
            print("\n--- MEUS CONTATOS ---")
            if not agenda:
                print("Agenda vazia.")
            else:
                for nome, dados in agenda.items():
                    # Buscando os dados dentro do dicionário interno
                    print(f"Nome: {nome} | Tel: {dados['telefone']} | Obs: {dados['descricao']}")

        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

except KeyboardInterrupt:
    print("\n\nPrograma interrompido. Dados salvos.")
    salvar_dados(agenda)