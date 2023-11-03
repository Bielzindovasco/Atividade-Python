from disciplina import Disciplina

class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.disciplinas = []
        
    def add_disciplina(self):
        nome_disciplina = input("Nome da disciplina: ")
        disciplina = Disciplina(nome_disciplina)
        Professor.disciplinas.append(disciplina)