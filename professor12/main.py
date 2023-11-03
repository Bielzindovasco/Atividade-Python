from Atividade import atividade
from disciplina import Disciplina
from professor import Professor
while True:
    print("\nMenu:")
    print("1. Adicionar disciplina")
    print("2. Adicionar atividade")
    print("3. Marcar atividade como concluída")
    print("4. Listar atividades em aberto")
    print("5. Listar atividades concluídas")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        Professor.add_disciplina()
    elif opcao == "2":
        Disciplina.add_atividade()
    elif opcao == "3":
        nome_disciplina = input("Nome da disciplina: ")
        descricao_atividade = input("Descrição da atividade: ")

        for disciplina in Professor.disciplinas:
            if disciplina.nome == nome_disciplina:
                for atividade in disciplina.atividades:
                    if atividade.descricao == descricao_atividade and not atividade.concluida:
                        atividade.marcar_concluida()
                        print("Atividade marcada como concluída.")
                        break
                else:
                    print("Atividade não encontrada ou já concluída.")
                break
        else:
            print("Disciplina não encontrada.")
    elif opcao == "4":
        Disciplina.atividades_em_aberto()
    elif opcao == "5":
        Disciplina.atividades_concluidas()
    elif opcao == "6":
        break
    else:
        print("Opção inválida. Tente novamente.")