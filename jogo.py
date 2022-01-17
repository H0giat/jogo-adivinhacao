"""
jogo de adivinhar a palavra
"""

palavra = 'friends'
digitadas = []
chances = 3

while True:
    if chances < 1:
        print('Você perdeu!')
        break

    letra = input("Digite uma letra: ")

    if letra > 1:
        print("Digite apenas uma letra.")
        continue

    