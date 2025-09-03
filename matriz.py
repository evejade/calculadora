import numpy as np

def menu():
    print("\n=== Calculadora de Matrizes ===")
    print("1 - Somar matrizes")
    print("2 - Subtrair matrizes")
    print("3 - Multiplicar matrizes")
    print("4 - Determinante de uma matriz")
    print("5 - Transposta de uma matriz")
    print("0 - Sair")

def ler_matriz():
    linhas = int(input("Digite o número de linhas: "))
    colunas = int(input("Digite o número de colunas: "))
    print("Digite os elementos da matriz linha por linha:")
    matriz = []
    for i in range(linhas):
        linha = list(map(float, input().split()))
        matriz.append(linha)
    return np.array(matriz)

while True:
    menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 0:
        print("Saindo...")
        break

    if opcao in [1, 2, 3]:
        print("\n--- Matriz A ---")
        A = ler_matriz()
        print("\n--- Matriz B ---")
        B = ler_matriz()

        if opcao == 1:
            print("\nResultado da soma:\n", A + B)
        else:
            if opcao == 2:
                print("\nResultado da subtração:\n", A - B)
            else:
             if opcao == 3:
                print("\nResultado da multiplicação:\n", A @ B)

    else:
        if opcao == 4:
            A = ler_matriz()
            print("\nDeterminante = ", np.linalg.det(A))
        else:
          if opcao == 5:
            A = ler_matriz()
            print("\nTransposta:\n", A.T)

          else:
              print("Opção inválida!")
