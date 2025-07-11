#Até 4 linhas python só guardou a informacao 
def soma (numero1, numero2):
    som = numero1 + numero2
    print(som)
numero1 = int(input("Digite: "))
numero2 = int(input("Digite: "))
soma(numero1,numero2)


lista = []

def sub (lista):
    subtr = lista[0] - lista[1]
    print(subtr)

nun1 = input("Digite: ")
lista.append(nun1)
nun2 = input("Digite: ")
lista.append(nun2)

sub([0,1])