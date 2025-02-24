def recuperarNota(nota):
    if 60 <= nota <= 69:
        print("Fique atento, você tirou D.")
    elif 70 <= nota <= 79:
        print("Bom trabalho, você tirou C.")
    elif 80 <= nota <= 89:
        print("Muito bem, você tirou B.")
    elif 90 <= nota <= 100:
        print("Parabéns, você tirou A!")
    elif nota < 60:
        print("Estude um pouco mais, você tirou F.")
    else:
        print("Nota inválida")


nota = float(input("Informe a nota:"))
recuperarNota(nota)
