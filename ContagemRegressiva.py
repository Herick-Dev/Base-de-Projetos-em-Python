import time

def contagem_regressiva(segundos):
    for i in range(segundos, 0, -1):
        print(f"Tempo restante: {i} segundos")
        time.sleep(1)
    print("Tempo esgotado! 🎉")

segundos = int(input("Digite a quantidade de segundos para a contagem regressiva: "))
contagem_regressiva(segundos)