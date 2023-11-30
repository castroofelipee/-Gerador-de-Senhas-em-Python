import random
import string

def gerar_senha(comprimento, usa_numeros=True, usa_maiusculas=True, usa_simbolos=True):
    caracteres = string.ascii_letters
    if usa_numeros:
        caracteres += string.digits
    if usa_maiusculas:
        caracteres += string.ascii_uppercase
    if usa_simbolos:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha


comprimento_senha = int(input("Digite o comprimento da senha desejada: "))
usar_numeros = input("Incluir números na senha? (sim/não): ").lower() == 'sim'
usar_maiusculas = input("Incluir letras maiúsculas na senha? (sim/não): ").lower() == 'sim'
usar_simbolos = input("Incluir símbolos na senha? (sim/não): ").lower() == 'sim'

senha_gerada = gerar_senha(comprimento_senha, usar_numeros, usar_maiusculas, usar_simbolos)
print(f"Sua senha gerada: {senha_gerada}")

