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

    if len(letra) > 1:
        print("Digite apenas uma letra.")
        continue

    if not letra in palavra:
        print("Perdeu uma vida")
        chances -= 1
    
    digitadas.append(letra)
    palavra_temporaria = ''

    if not letra in palavra:
        digitadas.pop()

    for letra in digitadas:
        if letra == palavra:
            palavra_temporaria += letra
        
    if palavra_temporaria == palavra:
        print('Parabéns, você ganhou o jogo.')
        break