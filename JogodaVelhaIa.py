import random

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)

def verificar_vitoria(tabuleiro, jogador):
    # Verifica linhas
    for linha in tabuleiro:
        if all(posicao == jogador for posicao in linha):
            return True

    # Verifica colunas
    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True

    # Verifica diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2-i] == jogador for i in range(3)):
        return True

    return False

def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True

def jogada_ia(tabuleiro, jogador):
    # Verifica se há uma posição para ganhar
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = jogador
                if verificar_vitoria(tabuleiro, jogador):
                    return True
                tabuleiro[linha][coluna] = " "

    # Verifica se o oponente pode ganhar na próxima jogada e bloqueia
    adversario = "O" if jogador == "X" else "X"
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = adversario
                if verificar_vitoria(tabuleiro, adversario):
                    tabuleiro[linha][coluna] = jogador
                    return False
                tabuleiro[linha][coluna] = " "

    # Caso nenhum dos jogadores possa ganhar na próxima rodada, faz uma jogada aleatória
    vazias = [(linha, coluna) for linha in range(3) for coluna in range(3) if tabuleiro[linha][coluna] == " "]
    linha, coluna = random.choice(vazias)
    tabuleiro[linha][coluna] = jogador
    return False

def jogar_jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

    while True:
        imprimir_tabuleiro(tabuleiro)

        # Vez do jogador
        linha = int(input("Digite o número da linha (0, 1, 2): "))
        coluna = int(input("Digite o número da coluna (0, 1, 2): "))

        if tabuleiro[linha][coluna] != " ":
            print("Essa posição já foi escolhida. Escolha outra.")
            continue

        tabuleiro[linha][coluna] = "X"

        if verificar_vitoria(tabuleiro, "X"):
            imprimir_tabuleiro(tabuleiro)
            print("Você venceu!")
            break
        elif verificar_empate(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        # Vez da IA
        print("Vez da IA...")
        if jogada_ia(tabuleiro, "O"):
            imprimir_tabuleiro(tabuleiro)
            print("A IA venceu!")
            break
        elif verificar_empate(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("Empate!")
            break

if __name__ == "__main__":
    jogar_jogo_da_velha()