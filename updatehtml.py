import os
import json

TEMPLATE_PATH = "index_template.html"
OUTPUT_PATH = "index.html"
ICON_EXTENSIONS = (".png", ".jpg", ".jpeg", ".svg")
PLACEHOLDER = "__ICONS_JSON__"


def collect_icon_names():
    """Lista, ordena (case-insensitive) e remove duplicados dos ficheiros de ícones na pasta atual."""
    icons = {
        file for file in os.listdir(".")
        if file.lower().endswith(ICON_EXTENSIONS)
    }
    return sorted(icons, key=str.lower)


def render_icons_json(icons):
    """Serializa a lista de ícones em JSON seguro para embutir num <script>."""
    # ensure_ascii=False preserva acentos (ex.: "açores.png") de forma legível.
    # A troca de "</" evita que um nome de ficheiro feche a tag <script> prematuramente.
    return json.dumps(icons, ensure_ascii=False).replace("</", "<\\/")


def generate_new_index_html():
    icons = collect_icon_names()
    icons_json = render_icons_json(icons)

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = f.read()

    if PLACEHOLDER not in template:
        raise ValueError(
            f"Placeholder '{PLACEHOLDER}' não encontrado em {TEMPLATE_PATH}. "
            "Verifica se o template ainda corresponde ao esperado pelo script."
        )

    new_html_content = template.replace(PLACEHOLDER, icons_json)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(new_html_content)

    print(f"Novo arquivo {OUTPUT_PATH} criado com {len(icons)} ícones encontrados.")


if __name__ == "__main__":
    generate_new_index_html()