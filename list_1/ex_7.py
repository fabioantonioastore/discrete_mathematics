def factorial(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


def circular_permutation(n: int) -> int:
    return factorial(n - 1)


"""
Na permutacao circular as posicoes de A nao importa se vai ser no inicio, no meio ou no final do arranjo, diferente da permutacao linear onde e calculado todas as 
combinacoes possiveis de arranjos incluindo a posicao no mesmo, sendo assim basta retirarmos o calculo adicional das posicoes dado pela formula:
n!/n = (n - 1)!
"""
