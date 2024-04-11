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

def jogar_jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogadores = ["X", "O"]
    jogador_atual = 0
    jogadas_restantes = 9

    while True:
        imprimir_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogadores[jogador_atual]}")

        linha = int(input("Digite o número da linha (0, 1, 2): "))
        coluna = int(input("Digite o número da coluna (0, 1, 2): "))

        if tabuleiro[linha][coluna] != " ":
            print("Essa posição já foi escolhida. Escolha outra.")
            continue

        tabuleiro[linha][coluna] = jogadores[jogador_atual]
        jogadas_restantes -= 1

        if verificar_vitoria(tabuleiro, jogadores[jogador_atual]):
            imprimir_tabuleiro(tabuleiro)
            print(f"O jogador {jogadores[jogador_atual]} venceu!")
            break
        elif jogadas_restantes == 0:
            imprimir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        jogador_atual = (jogador_atual + 1) % 2

if __name__ == "__main__":
    jogar_jogo_da_velha()