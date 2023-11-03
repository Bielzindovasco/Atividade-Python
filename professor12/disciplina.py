from professor import Professor

class Disciplina:
    def __init__(self, nome):
        self.nome = nome
        self.atividades = []
        
    def add_atividade(self, atividade):
        datas_existentes = [a.data for a in self.atividades]
        if atividade.data not in datas_existentes:
            self.atividades.append(atividade)
        else:
            print("Já existe uma atividade nesta data.")
        
    def atividades_em_aberto():
        for disciplina in Professor.disciplinas:
            print(f"Disciplina: {disciplina.nome}")
            for atividade in disciplina.atividades:
                if not atividade.concluida:
                    print(atividade)

    def atividades_concluidas():
        for disciplina in Professor.disciplinas:
            print(f"Disciplina: {disciplina.nome}")
            for atividade in disciplina.atividades:
                if atividade.concluida:
                    print(atividade)
