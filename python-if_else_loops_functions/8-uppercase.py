#!/usr/bin/python3

def islower(c):
    """Verifica se um caractere é minúsculo."""
    return ord('a') <= ord(c) <= ord('z')


def uppercase(str):
    """Imprime a string em maiúsculas seguida por uma nova linha."""
    res = ""
    for ch in str:  # único loop permitido
        if islower(ch):
            novo = chr(ord(ch) - 32)  # converte minúscula para maiúscula
        else:
            novo = ch  # mantém outros caracteres iguais
        res += novo
    print(f"{res}")  # imprime o resultado em uma linha

uppercase("best")
# Saída: BEST

uppercase("Best School 98 Battery street")
# Saída: BEST SCHOOL 98 BATTERY STREET
