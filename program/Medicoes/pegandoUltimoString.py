def salvar_ultimo_string_por_letra(arquivo_entrada, arquivo_saida):
    # Dicionário para armazenar o último string de cada letra
    ultimos_strings = {}

    with open(arquivo_entrada, 'r', encoding='utf-8') as f:
        for linha in f:
            linha = linha.strip()  # Remove espaços em branco
            if linha:  # Verifica se a linha não está vazia
                ultimo_char = linha[-1]  # Pega o último caractere (minúsculo)
                ultimos_strings[ultimo_char] = linha  # Atualiza o último string para essa letra

    # Salva os resultados no arquivo de saída
    with open(arquivo_saida, 'w', encoding='utf-8') as f:
        for letra, string in sorted(ultimos_strings.items()):
            f.write(f"{letra}: {string}\n")

    print(f"Arquivo processado! Resultados salvos em: {arquivo_saida}")

# Exemplo de uso:
arquivo_entrada = "C:/Users/valderez/Documents/ADS/ADS4/Avalia-o-de-Desempenho-de-Sistema/program/Medicoes/Tamanho9400000.txt"  # Substitua pelo seu arquivo de entrada
arquivo_saida = "Tamanho9400000Final.txt"  # Arquivo de saída
salvar_ultimo_string_por_letra(arquivo_entrada, arquivo_saida)