""" chat - módulo tal que faz isso.

o módulo main faz isso e aquilo. Ele de vez em quando,quase nunca, mais com frequência, parece que não é.

areaq = 1*1

"""




def calcula_area_quadrado():

    lado_do_quadrado: float = 0.0

    lado_do_quadrado =float(input('informe o lado do quadrado'))

    print(lado_do_quadrado*lado_do_quadrado)

class Aluno:

    def __init__(self):
        self.nome =''
        self.matricula =''
        self.telefone =''

    def set__nome(self, novo__nome):
        if novo__nome != '':
            self.nome = novo__nome 
    
    def get__nome(self):
        return self.nome
    
    def descreva__aluno(self):
        return f'Nome: {self.nome} - telefone: {self.telefone} - matricula: {self.matricula}'
    

class Alunoexten (Aluno):
    def __init__(self):
        super().__init__()
        self.curso = ''

        
aluno1 = Aluno()
aluno1.set__nome("carlos")
aluno1.matricula = '1234'
aluno1.telefone = '85 9999 11 44'
print(aluno1.descreva__aluno())


        
   
   










    



