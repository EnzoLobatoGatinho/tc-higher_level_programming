#!/usr/bin/python3

def islower(c):
    return ord('a') <= ord(c) <= ord('z')

def uppercase(str):
    res = ""
    for ch in str:
        if islower(ch):
            novo = chr(ord(ch) - 32)
        else:
            novo = ch
        res += novo
    print(f"{res}")

# Chamadas de teste
uppercase("best")
uppercase("Best School 98 Battery street")
