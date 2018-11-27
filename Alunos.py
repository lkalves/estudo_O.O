class escolar():
    def __init__(self,aluno,nota=0,nota1=0,falta=0):
        self.aluno=aluno
        self.nota=nota
        self.nota1 = nota1
        self.falta=falta
    def controle(self):
        if (self.nota+self.nota1)/2 < 7:
            print('O aluno',self.aluno,' foi reprovado por não atingir a pontuação necessária de 14 pontos')
            if self.falta > 25:
                print('O aluno',self.aluno,'reprovou pelo total de',self.falta,'faltas, e também por causa da nota.')
        else:
            if self.falta > 25:
                print('O aluno', self.aluno, 'tem o total de pontos exigida, porém repetiu por falta.')
            else:
                print('O aluno', self.aluno, 'foi aprovado por atingir a pontuação necessária de 14 pontos')
                print('O aluno', self.aluno, 'tem o total de', self.falta, 'faltas.')


aluno=input('Nome do aluno: ')
nota=float(input('Entre com a primeira nota: '))
nota1=float(input('Entre com a segunda nota: '))
falta=int(input('Entre com o total de faltas: '))

escola=escolar(aluno,nota,nota1,falta)
escola.controle()
