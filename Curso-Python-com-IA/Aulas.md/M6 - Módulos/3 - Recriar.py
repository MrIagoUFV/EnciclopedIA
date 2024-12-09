# Importe a função criar_ascii_art da biblioteca AsciiArt.textoparaascii
import Ascii.textoparaascii as ascii

# Receber o nome do usuário:
nome_usuario = input("Digite o nome do usuário: ")

# Dizer oi para o usuário em ascii art usando a função criar_ascii_art
print(ascii.criar_ascii_art(f"Oi, {nome_usuario}!"))


# DRY - Don't Repeat Yourself