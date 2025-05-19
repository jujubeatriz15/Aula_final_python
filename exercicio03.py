with open ("nomes.txt", "a") as  arquivo:
    nome = input("Digite um nome: ")
    arquivo.write(f"{nome}\n")