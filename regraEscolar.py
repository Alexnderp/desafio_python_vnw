def avaliaNota(nota):
    if nota >= 5:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")

nota = float(input("Informe a nota:")) 

avaliaNota(nota)