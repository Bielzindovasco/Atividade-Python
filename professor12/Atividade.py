class atividade:
    def __init__(self, nome, data):
        self.nome = nome
        self.data = data
        self.concluida = False
        
    def marcar_concluida(self):
        self.concluida = True
        
    def __str__(self):
      estado = "Concluída" if self.concluida else "Em aberto"
      return f"{self.nome}\n{self.data}\n{estado}"
