from docx import Document

def extrair_ultimos_strings(caminho_arquivo):
    # Carrega o documento
    doc = Document(caminho_arquivo)
    
    ultimos_strings = []
    
    # Itera por cada parágrafo no documento (cada parágrafo é como uma linha)
    for para in doc.paragraphs:
        texto = para.text.strip()
        if texto:  # Verifica se a linha não está vazia
            # Divide o texto pelos espaços
            palavras = texto.split()
            if palavras:  # Se houver palavras na linha
                ultimo_string = palavras[-1]  # Pega o último elemento
                ultimos_strings.append(ultimo_string)
    
    return ultimos_strings

# Exemplo de uso
caminho = 'MERGE.txt'  # Substitua pelo caminho do seu arquivo
resultados = extrair_ultimos_strings(caminho)

# Imprime os resultados
for i, string in enumerate(resultados, 1):
    print(f"Linha {i}: {string}")

# Opcional: Salvar os resultados em um arquivo de texto
with open('ultimos_strings.txt', 'w', encoding='utf-8') as f:
    for string in resultados:
        f.write(string + '\n')

print("Processamento concluído. Resultados salvos em 'ultimos_strings.txt'")