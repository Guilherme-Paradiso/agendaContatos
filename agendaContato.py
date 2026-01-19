agenda = {}

while True:
    nome = input("Nome (ou 'Sair'): ")
    if nome == "Sair":
        break

    descricao = input("Informação do Contato ('0' caso não tenha): ")

    telefone = input("Telefone (Sem espaço!!!): ")
    if 8 <= len(telefone) <= 11 and telefone.isdigit():
        agenda[nome] = telefone
        print(f"Sucesso: Contato de: {nome} guardado.")
    else:
        # Se cair aqui, a linha 'agenda[nome] = telefone' não é executada
        print("Erro: Telefone inválido (deve ter entre 8 e 11 dígitos, e não pode ser letras!). Contato não guardado.")

print("\nContatos Salvos:")
for nome, telefone in agenda.items():
    print(nome, "-", telefone, "-", descricao)