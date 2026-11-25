import desenhos as d
import fileHandler as fH
from random import choice

def jogar():
    lista_palavras = list()
    arquivo = fH.abrirArquivoLeitura('palavras.txt')
    if arquivo is None:
        return
    for linha in arquivo:
        palavra = linha.strip().lower()
        lista_palavras.append(palavra)

    palavra_sorteada = choice(lista_palavras)

    for x in range(50):
        print()

    digitadas = []
    acertos = []
    erros = 0

    nome = input('Quem está jogando ? ')

    while True:
        adivinha = d.imprimir_palavra_secreta(palavra_sorteada, acertos)

        #CONDIÇÃO DE VITÓRIA
        if adivinha == palavra_sorteada:
            print('Você acertou ! ')
            break

        #TENTATIVAS
        tentativa = input('\nDigite uma letra: ').lower().strip()

        # validação: exatamente 1 caractere e que seja letra
        if len(tentativa) != 1 or not tentativa.isalpha():
            print('Digite apenas uma letra.')
            continue

        if tentativa in digitadas:
            print('Você já usou está letra, Seu burro ! ')
            continue
        else:
            digitadas += tentativa #ou append
            if tentativa in palavra_sorteada:
                acertos += tentativa
            else:
                erros += 1
                print('Você errou !')

        score = d.desenhar_forca(erros)

        #CONDIÇÃO DE FIM JOGO
        if erros == 6:
            print('Enforcado !')
            print(f'A palavra correta era {palavra_sorteada}.')
            break

        fH.inserir_score('score.txt', nome, score)
