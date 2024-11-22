import os
import re
import requests

# URL do arquivo M3U
m3u_url = "https://raw.githubusercontent.com/thomraider12/canaistvpt/main/pt.m3u"

# Prefixos permitidos
valid_prefixes = [
    "https://raw.githubusercontent.com/thomraider12/icones_tv/main/",
    "https://github.com/thomraider12/icones_tv/raw/"
]

# Função para baixar o logo
def download_logo(url, filename):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        with open(filename, "wb") as file:
            file.write(response.content)
        print(f"Logo baixado: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar {url}: {e}")

# Função para baixar o arquivo M3U
def download_m3u(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar o arquivo M3U: {e}")
        return None

# Processamento do arquivo M3U
m3u_content = download_m3u(m3u_url)
if m3u_content:
    lines = m3u_content.splitlines()

    for line in lines:
        # Procura linhas com tvg-logo
        if 'tvg-logo="' in line:
            match_logo = re.search(r'tvg-logo="([^"]+)"', line)
            match_channel = re.search(r',(.+)$', line)
            
            if match_logo and match_channel:
                logo_url = match_logo.group(1)
                channel_name = match_channel.group(1).strip()
                
                # Remove parênteses e o conteúdo interno do nome do canal
                channel_name = re.sub(r'\s*.*?\s*', '', channel_name)
                
                # Verifica se o logo não começa com os prefixos válidos
                if not any(logo_url.startswith(prefix) for prefix in valid_prefixes):
                    print(f"Analisando canal: {channel_name}")
                    
                    # Processa o nome do canal para ficar em minúsculas e sem espaços
                    sanitized_channel_name = re.sub(r'\s+', '', channel_name.lower())
                    
                    # Define o caminho para salvar o logo
                    logo_path = os.path.join(f"{sanitized_channel_name}.png")
                    
                    # Baixa o logo
                    download_logo(logo_url, logo_path)
