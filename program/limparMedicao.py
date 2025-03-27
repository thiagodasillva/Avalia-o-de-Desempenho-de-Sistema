# Nome do arquivo de entrada e saída
input_file = "program/esseMesmo9400000.txt"
output_file = "resultados_processadosValorMaximo.txt"

# Abre o arquivo de entrada para leitura e o arquivo de saída para escrita
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    # Variável para armazenar a última linha útil de cada medição
    last_line = None
    
    for line in infile:
        # Remove espaços em branco no início e fim da linha
        stripped_line = line.strip()
        
        # Se a linha não estiver vazia, armazena como última linha útil
        if stripped_line:
            last_line = stripped_line
        else:
            # Quando encontra uma linha vazia, escreve a última linha útil no arquivo de saída
            if last_line:
                outfile.write(last_line + '\n')
                last_line = None
    
    # Escreve a última linha útil do arquivo, caso não tenha sido escrita
    if last_line:
        outfile.write(last_line + '\n')

print("Processamento concluído. Os resultados foram salvos em", output_file)