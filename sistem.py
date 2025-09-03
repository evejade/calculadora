import numpy as np

def resolver_sistema_linear():
    print("=== Calculadora de Sistemas Lineares ===")
    
 
    n = int(input("Digite o número de variáveis (ex: 2, 3): "))

    #matriz 
    A = []
    print("\nDigite os coeficientes das equações (linha por linha):")
    for i in range(n):
        linha = list(map(float, input(f"Coeficientes da equação {i+1} (separados por espaço): ").split()))
        if len(linha) != n:
            print("Número de coeficientes inválido!")
            return
        A.append(linha)
    
    b = list(map(float, input("\nDigite os termos independentes (separados por espaço): ").split()))
    if len(b) != n:
        print("Número de termos independentes inválido!")
        return

    # Converter listas para arrays do NumPy
    A = np.array(A)
    b = np.array(b)

    try:
        x = np.linalg.solve(A, b)
        print("\nSolução do sistema:")
        for i in range(n):
            print(f"x{i+1} = {x[i]}")
    except np.linalg.LinAlgError as e:
        print(f"\nErro ao resolver o sistema: {e}")

resolver_sistema_linear()
