def pode_votar(idade:int):
    if idade >= 16:
        print ("Elegivel para votar")
    else:
        print ("Não está elegivel para votar")


idade = int(input("Informe sua idade:"))

pode_votar(idade)