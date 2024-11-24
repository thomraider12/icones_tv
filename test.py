import webbrowser
import re
import os

# Nome do arquivo M3U
arquivo_m3u = "testepg.m3u"
diretorio_logos = "."  # Diretório onde as logos estão armazenadas (diretório atual)

# Função para extrair os nomes dos canais
def extrair_canais(arquivo):
    canais = []
    with open(arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            if "tvg-name=" in linha:
                # Extrair o nome do canal do atributo tvg-name
                match = re.search(r'tvg-name="([^"]+)"', linha)
                if match:
                    canais.append(match.group(1))
    return canais

# Função para gerar o nome do arquivo da logo
def gerar_nome_logo(canal):
    nome_logo = canal.lower().replace(" ", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
    # Adiciona a extensão de imagem
    return f"{nome_logo}.png"

# Função para verificar se a logo já existe no diretório
def logo_ja_existe(canal):
    nome_logo = gerar_nome_logo(canal)
    return os.path.isfile(os.path.join(diretorio_logos, nome_logo))

# Abrir uma aba no navegador para cada canal com pausa para o usuário
def pesquisar_logos_interativo(canais):
    for i, canal in enumerate(canais, start=1):
        if not logo_ja_existe(canal):
            pesquisa = f"{canal} logo"
            url = f"https://www.google.com/search?q={pesquisa.replace(' ', '+')}"
            print(f"[{i}/{len(canais)}] Abrindo pesquisa para: {canal}")
            webbrowser.open_new_tab(url)
            input("Pressione Enter para abrir o próximo canal...")
        else:
            print(f"[{i}/{len(canais)}] Logo de '{canal}' já existe. Pulando...")

# Processar o arquivo e abrir as abas
try:
    canais = extrair_canais(arquivo_m3u)
    if canais:
        print(f"Encontrados {len(canais)} canais. Vamos começar...")
        pesquisar_logos_interativo(canais)
        print("Todas as abas foram abertas.")
    else:
        print("Nenhum canal encontrado no arquivo.")
except FileNotFoundError:
    print(f"Arquivo '{arquivo_m3u}' não encontrado.")