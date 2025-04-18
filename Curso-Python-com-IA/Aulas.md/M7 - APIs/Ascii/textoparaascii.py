def criar_ascii_art(texto):
    # Dicionário para normalizar caracteres especiais
    normalize = {
        'Á': 'A', 'À': 'A', 'Ã': 'A', 'Â': 'A', 'Ä': 'A',
        'É': 'E', 'È': 'E', 'Ê': 'E', 'Ë': 'E',
        'Í': 'I', 'Ì': 'I', 'Î': 'I', 'Ï': 'I',
        'Ó': 'O', 'Ò': 'O', 'Õ': 'O', 'Ô': 'O', 'Ö': 'O',
        'Ú': 'U', 'Ù': 'U', 'Û': 'U', 'Ü': 'U',
        'Ý': 'Y', 'Ÿ': 'Y',
        'Ñ': 'N',
        'Ç': 'C',
        # Adicione outros caracteres especiais conforme necessário
    }
    
    # Normaliza o texto antes de processar
    texto_normalizado = ''
    for char in texto.upper():
        texto_normalizado += normalize.get(char, char)
    
    # Definindo a arte ASCII para cada letra
    letras = {
        'A': [
            "      /\\      ",
            "     /  \\     ",
            "    / __ \\    ",
            "   / ____ \\   ",
            "  /_/    \\_\\  ",
            "              "
        ],
        'B': [
            "   ______     ",
            "  |  __  \\    ",
            "  | |__) |    ",
            "  |  _  /     ",
            "  | |_) |     ",
            "  |____/      "
        ],
        'C': [
            "   _____     ",
            "  / ____|    ",
            " | |         ",
            " | |         ",
            " | |____     ",
            "  \\_____|    "
        ],
        'D': [
            "  _____      ",
            " |  __ \\     ",
            " | |  | |    ",
            " | |  | |    ",
            " | |__| |    ",
            " |_____/     "
        ],
        'E': [
            "  ______     ",
            " |  ____|    ",
            " | |__       ",
            " |  __|      ",
            " | |____     ",
            " |______|    "
        ],
        'F': [
            "  ______     ",
            " |  ____|    ",
            " | |__       ",
            " |  __|      ",
            " | |         ",
            " |_|         "
        ],
        'G': [
            "   _____     ",
            "  / ____|    ",
            " | |  __     ",
            " | | |_ |    ",
            " | |__| |    ",
            "  \\_____|    "
        ],
        'H': [
            "  _    _     ",
            " | |  | |    ",
            " | |__| |    ",
            " |  __  |    ",
            " | |  | |    ",
            " |_|  |_|    "
        ],
        'I': [
            "  _____     ",
            " |_   _|    ",
            "   | |      ",
            "   | |      ",
            "  _| |_     ",
            " |_____|    "
        ],
        'J': [
            "       _    ",
            "      | |   ",
            "      | |   ",
            "  _   | |   ",
            " | |__| |   ",
            "  \\____/    "
        ],
        'K': [
            "  _  __     ",
            " | |/ /     ",
            " | ' /      ",
            " |  <       ",
            " | . \\      ",
            " |_|\\_\\     "
        ],
        'L': [
            "  _         ",
            " | |        ",
            " | |        ",
            " | |        ",
            " | |____    ",
            " |______|   "
        ],
        'M': [
            "  __  __    ",
            " |  \\/  |   ",
            " | \\  / |   ",
            " | |\\/| |   ",
            " | |  | |   ",
            " |_|  |_|   "
        ],
        'N': [
            "  _   _     ",
            " | \\ | |    ",
            " |  \\| |    ",
            " | . ` |    ",
            " | |\\  |    ",
            " |_| \\_|    "
        ],
        'O': [
            "   ____     ",
            "  / __ \\    ",
            " | |  | |   ",
            " | |  | |   ",
            " | |__| |   ",
            "  \\____/    "
        ],
        'P': [
            "  _____     ",
            " |  __ \\    ",
            " | |__) |   ",
            " |  ___/    ",
            " | |        ",
            " |_|        "
        ],
        'Q': [
            "   ____     ",
            "  / __ \\    ",
            " | |  | |   ",
            " | |  | |   ",
            " | |__| |   ",
            "  \\___\\_\\   "
        ],
        'R': [
            "  _____     ",
            " |  __ \\    ",
            " | |__) |   ",
            " |  _  /    ",
            " | | \\ \\    ",
            " |_|  \\_\\   "
        ],
        'S': [
            "   _____    ",
            "  / ____|   ",
            " | (___     ",
            "  \\___ \\    ",
            "  ____) |   ",
            " |_____/    "
        ],
        'T': [
            "  _______   ",
            " |__   __|  ",
            "    | |     ",
            "    | |     ",
            "    | |     ",
            "    |_|     "
        ],
        'U': [
            "  _    _    ",
            " | |  | |   ",
            " | |  | |   ",
            " | |  | |   ",
            " | |__| |   ",
            "  \\____/    "
        ],
        'V': [
            " __      __ ",
            " \\ \\    / / ",
            "  \\ \\  / /  ",
            "   \\ \\/ /   ",
            "    \\  /    ",
            "     \\/     "
        ],
        'W': [
            " __          __ ",
            " \\ \\        / / ",
            "  \\ \\  /\\  / /  ",
            "   \\ \\/  \\/ /   ",
            "    \\  /\\  /    ",
            "     \\/  \\/     "
        ],
        'X': [
            " __   __   ",
            " \\ \\ / /   ",
            "  \\ V /    ",
            "   > <     ",
            "  / . \\    ",
            " /_/ \\_\\   "
        ],
        'Y': [
            " __   __   ",
            " \\ \\ / /   ",
            "  \\ V /    ",
            "   | |     ",
            "   | |     ",
            "   |_|     "
        ],
        'Z': [
            "  ______   ",
            " |___  /   ",
            "    / /    ",
            "   / /     ",
            "  / /__    ",
            " /_____|   "
        ],
        ' ': [
            "           ",
            "           ",
            "           ",
            "           ",
            "           ",
            "           "
        ]
    }
    
    # Inicializa as linhas da arte
    linhas_arte = ["", "", "", "", "", ""]
    
    # Para cada letra no texto normalizado
    for letra in texto_normalizado:
        # Se a letra existe no dicionário
        if letra in letras:
            # Adiciona cada linha da letra à linha correspondente da arte
            for i in range(6):
                linhas_arte[i] += letras[letra][i]
        else:
            # Para caracteres não suportados, adiciona espaço
            for i in range(6):
                linhas_arte[i] += letras[' '][i]
    
    return "\n".join(linhas_arte)
