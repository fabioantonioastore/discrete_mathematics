factorial_cache = {1: 1}


def factorial(n: int) -> int:
    if n in factorial_cache:
        return factorial_cache[n]
    factorial_cache[n] = n * factorial(n - 1)
    return factorial_cache[n]


def total_passwords(size: int, n: int, repeat: bool) -> int:
    if repeat:
        return n**size
    return factorial(n) // factorial(n - size)


print(f"Total passwords with repeated:\t{total_passwords(8, 26 + 10, True)}")
print(f"Total passwords without repeated:\t{total_passwords(8, 26 + 10, False)}")

"""
O primeiro, pois como podemos repetir os caracteres, temos que o total sera de 36^8,
ja que cada digito pode repetir, assim mantendo o nosso arranjo de possibilidades constante para a proxima casa, ao contrario do que nao pode repetir, pois cada digito podera ser usado uma
unica vez 36! / (36 - 8)!, reduzido assim o nosso arranjo de possibilidades para o proximo digito
"""
