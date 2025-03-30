import subprocess

# Função para executar o programa Java
def executar_java(algoritmo, tamanho, valor_maximo):
    comando = [
        "java",
        "MedidorDeOrdenacao",
        algoritmo,
        str(tamanho),
        str(valor_maximo)
    ]
    print(f"Executando: {' '.join(comando)}")
    resultado = subprocess.run(comando, capture_output=True, text=True)
    
    # Exibir a saída do programa Java
    if resultado.returncode == 0:
        print(resultado.stdout)
    else:
        print("Erro ao executar o programa Java:")
        print(resultado.stderr)

# Função principal
def main():
    algoritmos = ["QUICK", "MERGE", "COUNTING"]
    tamanhos = [940000]
    valores_maximos = [94000000,940000]

    # Loop para testar todas as combinações
    for algoritmo in algoritmos:
        for i in range(39):
            for tamanho in tamanhos:
                for valor_maximo in valores_maximos:
                    print(f"\nTestando {algoritmo} com tamanho {tamanho} e valor máximo {valor_maximo}")
                    executar_java(algoritmo, tamanho, valor_maximo)

if __name__ == "__main__":
    main()