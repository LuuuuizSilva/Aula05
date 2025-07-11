# Retornar o maior numero entre os dois numero 

def maior (nun1,nun2):
    if nun1>nun2:
        print(f"{nun1} é maior que {nun2}")
    else: 
        print(f"{nun2} é maior que {nun1}")
nun1 = input("Digite: ")
nun2 = input("Digite: ")
maior(nun1,nun2)

#3 notas 
def notas(n1,n2,n3):
    media = (n1+n2+n3) / 3
    print(media)
n1 = int(input("Digite: "))
n2 = int(input("Digite: "))
n3 = int(input("Digite: "))
notas(n1,n2,n3)