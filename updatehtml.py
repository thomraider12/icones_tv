import os
import re

def generate_icon_html(icon_name):
    return f'''
        <div class="icon-item">
            <img src="{icon_name}" alt="{icon_name}" title="{icon_name}">
            <div class="icon-name">{icon_name}</div>
        </div>
    '''

def update_index_html():
    # Caminho do arquivo index.html
    index_file = 'index.html'

    # Lista de ícones na pasta principal
    icons = [file for file in os.listdir('.') if file.endswith(('.png', '.jpg', '.jpeg', '.svg'))]

    # Gera o HTML dinâmico para os ícones
    icons_html = '\n'.join(generate_icon_html(icon) for icon in icons)

    # Lê o conteúdo atual do arquivo index.html
    with open(index_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Substitui toda a div pelo novo conteúdo, usando expressão regular
    new_content = re.sub(
        r'<div class="icon-grid" id="icon-grid">.*?</div>',
        f'<div class="icon-grid" id="icon-grid">\n{icons_html}\n</div>',
        html_content,
        flags=re.DOTALL
    )

    # Salva o arquivo atualizado
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("index.html atualizado com os ícones encontrados.")

if __name__ == "__main__":
    update_index_html()
