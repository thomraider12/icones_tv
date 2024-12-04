import webbrowser
import re
import os
import requests

# Nome ou URL do arquivo M3U
arquivo_m3u = "https://github.com/thomraider12/canaistvpt/raw/main/pt.m3u"
diretorio_logos = "."  # Diretório onde as logos estão armazenadas (diretório atual)

# Função para carregar o conteúdo do arquivo M3U (local ou remoto)
def carregar_conteudo_m3u(arquivo):
    if arquivo.startswith("http://") or arquivo.startswith("https://"):
        # Caso seja um link, faz o download do conteúdo
        response = requests.get(arquivo)
        response.raise_for_status()  # Lança uma exceção se o download falhar
        return response.text.splitlines()  # Retorna as linhas do arquivo
    else:
        # Caso seja um arquivo local
        with open(arquivo, "r", encoding="utf-8") as f:
            return f.readlines()

# Função para extrair os pares de nome de canal e link de logo
def extrair_canais_dados(conteudo):
    canais = []
    for linha in conteudo:
        # Imprime as primeiras linhas para verificar o formato
        print(f"Linha: {linha}")
        
        # Verifica se há uma vírgula (indicando a presença do nome do canal)
        if ',' in linha:
            partes = linha.split(',')
            if len(partes) >= 2:
                nome = partes[1].strip()  # O nome do canal está após a vírgula
                logo_match = re.search(r'tvg-logo="([^"]+)"', linha)
                if logo_match:
                    logo_link = logo_match.group(1)
                    canais.append((nome, logo_link))
    return canais

# Função para gerar o nome do arquivo da logo a partir do link
def gerar_nome_logo(link):
    # Extrai apenas o nome do arquivo no final do link
    nome_logo = os.path.basename(link).lower()
    return nome_logo

# Função para verificar se a logo já existe no diretório
def logo_ja_existe(link):
    nome_logo = gerar_nome_logo(link)
    return os.path.isfile(os.path.join(diretorio_logos, nome_logo))

# Abrir uma aba no navegador para cada nome de canal com pausa para o usuário
def pesquisar_logos_interativo(canais):
    for i, (nome, logo_link) in enumerate(canais, start=1):
        if not logo_ja_existe(logo_link):
            pesquisa = f"{nome} logo"
            url = f"https://www.google.com/search?q={pesquisa.replace(' ', '+')}"
            print(f"[{i}/{len(canais)}] Abrindo pesquisa para: {nome}")
            webbrowser.open_new_tab(url)
            input("Pressione Enter para abrir o próximo canal...")
        else:
            print(f"[{i}/{len(canais)}] Logo de '{nome}' já existe. Pulando...")

# Processar o arquivo e abrir as abas
try:
    conteudo = carregar_conteudo_m3u(arquivo_m3u)
    canais = extrair_canais_dados(conteudo)
    if canais:
        print(f"Encontrados {len(canais)} canais com logos. Vamos começar...")
        pesquisar_logos_interativo(canais)
        print("Todas as abas foram abertas.")
    else:
        print("Nenhum canal com nome e logo encontrado no arquivo.")
except FileNotFoundError:
    print(f"Arquivo local '{arquivo_m3u}' não encontrado.")
except requests.RequestException as e:
    print(f"Erro ao baixar o arquivo M3U: {e}")