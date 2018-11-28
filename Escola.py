'''
class Car():
    def __init__(self, Modelo='', Ano=0, Car='', Cilindrada = 0, Fabricante =''):
        self.Modelo=Modelo
        self.Ano=Ano
        self.Car=Car
        self.Cilindrada=Cilindrada
        self.Fabricante=Fabricante

    def diminuirAno(self,Ano=0):
        self.Ano= Ano-1
        print('O ano diminuido é:',self.Ano)
    def aumentarAno(self, Ano=0):
        self.Ano=Ano+1
        print('O ano aumentado é:', self.Ano)
    def carro(self, Modelo='', Ano=0, Fabricante=''):
        self.Ano=Ano
        self.Modelo=Modelo
        self.Fabricante=Fabricante
        print('O modelo do seu carro é um',self.Modelo,'da Fabricante',self.Fabricante,'e é do ano de',self.Ano,'.')


carros=Car()
carros.diminuirAno(1996)
carros.aumentarAno(1996)
carros.carro('Camaro',1996,'Chevrolet')
carros.carro('Uno',2003,'Fiatinho')
'''

'''
class Quadrado:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def quad(self):
        return self.a*self.b
quadrado =  Quadrado(2,2)
print(quadrado.quad())
'''

'''
class concessionaria():
    def __init__(self,carro, cor, cavalos=0,valor=0):
        self.carro=carro
        self.cor=cor
        self.cavalos=cavalos
        self.valor=valor
    def carros(self):
        print('O',self.carro,'da cor',self.cor,'que tem a cavalaria de',self.cavalos,'CVs, está saindo pelo valor de:',self.valor)

loja=concessionaria('Camaro','Azul',18,20000)
print(loja.carros())
'''

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

