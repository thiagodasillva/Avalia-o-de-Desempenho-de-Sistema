# Nome do arquivo de entrada
input_file = "C:/Users/valderez/Documents/ADS/ADS4/Avalia-o-de-Desempenho-de-Sistema/resultados_processadosValorMaximo.txt"  # Substitua pelo seu arquivo de entrada

# Nomes dos arquivos de saída
output_odd = "Tamanho9400000.txt"  # Linhas ímpares (1ª, 3ª, 5ª, ...)
output_even = "Tamanho94000000.txt"   # Linhas pares (2ª, 4ª, 6ª, ...)

# Abre o arquivo de entrada e os arquivos de saída
with open(input_file, 'r', encoding='utf-8') as infile, \
     open(output_odd, 'w', encoding='utf-8') as odd_file, \
     open(output_even, 'w', encoding='utf-8') as even_file:
    
    for index, line in enumerate(infile, start=1):
        if index % 2 == 1:  # Linha ímpar (1ª, 3ª, 5ª, ...)
            odd_file.write(line)
        else:  # Linha par (2ª, 4ª, 6ª, ...)
            even_file.write(line)

print("Processamento concluído!")
print(f"Linhas ímpares salvas em: {output_odd}")
print(f"Linhas pares salvas em: {output_even}")