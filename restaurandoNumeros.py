def soma():
    try:
        n1 = int(input("Informe o primeiro valor: "))
        n2 = int(input("Informe o segundo valor: "))
        print(n1 + n2)
    except ValueError:
        print("Número inválido")

soma()
