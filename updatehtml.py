import os

def generate_icon_html(icon_name):
    return f'''
        <div class="icon-item">
            <img src="{icon_name}" alt="{icon_name}" title="{icon_name}">
            <div class="icon-name">{icon_name}</div>
        </div>
    '''

def generate_new_index_html():
    # Caminho para a pasta de ícones (pode ser alterado conforme necessário)
    icons = list(set(file for file in os.listdir('.') if file.endswith(('.png', '.jpg', '.jpeg', '.svg'))))

    # Gera o HTML dinâmico para os ícones
    icons_html = '\n'.join(generate_icon_html(icon) for icon in icons)

    # Estrutura base do HTML fornecido
    new_html_content = f'''<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/png" href="logo.png">
    <title>Ícones de Televisão e Rádio</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background-color: #333; /* Preto-claro */
            color: #ffffff;
        }

        footer {
            border-radius: 20px;
            color: black;
            background-color: white;
        }

        .container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
            text-align: center;
        }
        .icon-grid {
            display: grid;
            gap: 10px;
            grid-template-columns: repeat(3, 1fr); 
        }

        @media (min-width: 768px) {
            .icon-grid {
                grid-template-columns: repeat(6, 1fr);
            }
        }

        .icon-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 10px;
            background-color: #444;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            overflow: hidden; /* Impede que o texto saia do quadrado */
        }
        .icon-item img {
            max-width: 80px;
            max-height: 80px;
            margin-bottom: 8px;
        }
        .icon-name {
            font-size: 0.85em;
            color: #ddd;
            text-align: center;
            word-wrap: break-word; /* Quebra o nome em palavras longas */
            overflow: hidden; /* Limita o texto dentro do container */
            text-overflow: ellipsis; /* Adiciona "..." se o texto for muito longo */
            white-space: nowrap; /* Mantém o texto em uma linha */
            width: 100%;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Ícones de Televisão e Rádio</h1>
        <div class="icon-grid" id="icon-grid">
            {icons_html}
        </div>
    </div>
</body>
</html>'''

    # Escreve o novo conteúdo no arquivo index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html_content)

    print("Novo arquivo index.html criado com os ícones encontrados.")

if __name__ == "__main__":
    generate_new_index_html()
